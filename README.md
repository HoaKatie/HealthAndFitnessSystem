# HealthAndFitnessSystem


- Entities:

Member
Trainer
Administrative Staff
Training Session
Activity
Fitness Goal
Billing
Loyalty Program
Equipment
Room


- Relationships:

Members can have personal training sessions, attend classes/events.
Trainers conduct personal training sessions and track member progress.
Administrative Staff manages rooms, equipment, schedules, billing, and the loyalty program.


- Features: GUI interaction and Console Interaction

displayUI.py will display a GUI that has the functionality of adding people into the system. Hence, adding or displayign members, trainers and staff.

server.py will let user modify, delete, add and change the query data through prompts.

-> open pgadmin for postgres
-> create new database
-> open students.sql in the database you created
-> execute to get query, else code will output error as there is no data yet to work open
-> open python file
-> pip install psycopg2 -> install python package to connect the postgres service (if not yet installed)


Steps to compile and run your application: 

(make sure to have python3 installed)
-> open command line / terminal in the same directory of the files
-> run: python ./displayUI.py or python ./server.py

***NOTE*** You might not be able to run from the cloned directory from GitHub. Hence, copy the file to your local directory and run python command.