-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (	player_id SERIAL PRIMARY KEY,
						player_name varchar,
						match_outcomes_wins int,
						no_matches int);

CREATE TABLE matches (	round int,
						player_1_winner varchar(80),
						player_2_loser varchar(80)
						);

CREATE VIEW standings_view AS
	SELECT players.player_id, players.player_name from players ORDER BY match_outcomes_wins ASC;