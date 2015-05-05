This file contains instructions for running the Swiss Tournament project.

1. Stand up the PostgreSQL database using the file "tournament.sql". This file contain the necessary sql commands to create the two tables--players and matches-- needed to store data relating to the swiss tournament.

2. Once the database is standing, run the "tournament.py" file. This file contains all of the methods necessary for the function to operate. 

3. Run this file in your development environment to view individual methods. (I used a vagrant Ubuntu environment with ipython and psql. If you go this route, you will need to stand up the database using the appropriate psql commands and running the afore-mentioned "tournament.sql" file. Once your tables have been created, using ipython "-i tournament.py" to test indvidual methods or elements of the tournament such as deleting players or reporting winners of matches.

4. To run and test the full application, use the tournament_test.py file with ipython (in the vagrant ssh environment). Running this file with the commando "ipython -i tournament_test.py" will run through the unit tests that demonstrate the capabilities of the program.