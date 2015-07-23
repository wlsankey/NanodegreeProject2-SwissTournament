#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament


import psycopg2
import math


def connect():
    # Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    # Remove all the match records from the database.
    connection = connect()
    c = connection.cursor()
    c.execute("DELETE FROM matches")
    connection.commit()
    c.close()
    connection.close()


def test():
    print "This is a test."


def deletePlayers():
    # Remove all the player records from the database.
    connection = connect()
    c = connection.cursor()
    c.execute("DELETE from players")
    connection.commit()
    c.close()
    connection.close()


def countPlayers():
    # Returns the number of players currently registered.
    connection = connect()
    c = connection.cursor()
    c.execute("""SELECT COUNT(*) FROM players;""")
    no_players = c.fetchone()[0]
    no_players = int(no_players)
    c.close()
    connection.close()
    return no_players


def registerPlayer(name):
    """
    Adds a player to the tournament database.
      c = connection.cursor()

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    connection = connect()
    c = connection.cursor()
    query = """INSERT INTO players (player_name, match_outcomes_wins, no_matches) VALUES(%s, %s, %s)"""
    params = (name, int(0), int(0))
    c.execute(query, params)
    connection.commit()
    c.close()
    connection.close()


def playerStandings():

    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    connection = connect()
    c = connection.cursor()
    c.execute("""SELECT * from players ORDER BY match_outcomes_wins ASC""")
    player_list = c.fetchall()
    c.close()
    connection.close()
    return_list = []
    for e in player_list:
        return_list.append(e)
    return return_list


def reportMatch(winner, loser):
    connection = connect()
    c = connection.cursor()
    c.execute("INSERT INTO matches (player_1_winner, player_2_loser) VALUES (%s, %s)", (winner, loser))
    c.execute("UPDATE players SET match_outcomes_wins = (match_outcomes_wins + 1), no_matches = (no_matches + 1) WHERE player_id = (%s)", (winner,))
    c.execute("UPDATE players SET no_matches = (no_matches + 1) WHERE player_id = (%s)", (loser,))
    connection.commit()
    c.close()
    connection.close()

    """
    Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    connection = connect()
    c = connection.cursor()
    offset_amount = 0
    matches = []    
    no_players = countPlayers()
    no_matches_per_round = (no_players/2)
    
    while (offset_amount/2) < no_matches_per_round:
        c.execute("""SELECT * from standings_view LIMIT 2 OFFSET (%s)""", (offset_amount,))
        standings_output = c.fetchall()
        first_seed = standings_output[0]
        second_seed = standings_output[1]
        individual_match = first_seed + second_seed
        matches.append(individual_match)
        offset_amount = offset_amount + 2

    c.close()
    connection.close()
    return matches
