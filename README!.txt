SWISS TOURNAMENT application readme file

About application:
This application simulates a Swiss-style tournament in which players compete each round and pairings are based on the win-loss record of players. 

Instructions for running the application:

1. SETUP: Navigate to via changing directories (cd) to the appropriate folder storing the application files. Run vagrant environment (or setup a new vagrant environment using "vagrant init" and the virtualbox preferred--in this case "ubuntu/trusty32"). Type "vagrant init ubuntu/trusty32". If you are just setting up a vagrant environment be sure to adjust the Vagrantfile and add the following provisioning and configuration information:

  config.vm.provision "shell", path: "pg_config.sh"
  config.vm.box = "ubuntu/trusty32"

Note that the file "pg_config.sh" is the Udacity-provided shell script that installs python and Postgresql on your box.


2. VAGRANT SSH: Type vagrant ssh to enter the shell. Once the secure shell has booted, navigate to the folder containing the project files: "cd /vagrant" is likely the command and location but please make sure this is where you have the files stored. 


3.SETUP DATABASE: Now that your virtual machine is setup, you can stand up the database for the application. 
	a. Type "psql" to start the postegresql application.
	b. Type "CREATE DATABASE tournament;" to create your database.
	c. Exit psql by typing "Ctrl + D". Now re-enter and connect to your database by typing "psql tournament"
	c. Type "\i tournament.sql" to use the existing file to setup your tables and views. After you are done you can exit psql again.


4. RUN APPLICATION: In the vagrant command line type: "python tournament_test.py". This should run a test of the application. You will receiving a message verifying whether or not it worked. If for some reason it did not work, please close the application, return to the vagrant command line and try once more to make sure you typed everything correctly.
