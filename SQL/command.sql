-- Inserting a new member
INSERT INTO Member (MemberName, ContactInfo) VALUES ('Hoa Nguyen', 'hoa@gmail.com');
INSERT INTO Member (MemberName, ContactInfo) VALUES ('Katie Chan', 'katie@gmail.com');
INSERT INTO Member (MemberName, ContactInfo) VALUES ('John Cena', '12345678');
INSERT INTO Member (MemberName, ContactInfo) VALUES ('Mac Donald', 'donald@hotmail.com');


-- Inserting a new trainer
INSERT INTO Trainer (TrainerName, Specialization) VALUES ('Sarah Smith', 'Yoga');
INSERT INTO Trainer (TrainerName, Specialization) VALUES ('Julia En', 'Zumba');
INSERT INTO Trainer (TrainerName, Specialization) VALUES ('Sandy Mai', 'Boxing');
INSERT INTO Trainer (TrainerName, Specialization) VALUES ('Charlie Puth', 'Muay Thai');


-- Inserting a training session
INSERT INTO TrainingSession (MemberID, TrainerID, Date, Notes) VALUES (1, 1, '2023-01-10', 'Morning session');
INSERT INTO TrainingSession (MemberID, TrainerID, Date, Notes) VALUES (1, 2, '2023-01-19', 'Afternoon session');
INSERT INTO TrainingSession (MemberID, TrainerID, Date, Notes) VALUES (2, 3, '2023-11-11', 'Evening session');
INSERT INTO TrainingSession (MemberID, TrainerID, Date, Notes) VALUES (3, 4, '2023-12-10', 'Night session');



-- Inserting an Activity
INSERT INTO Activity (ActivityName, Date, Description) VALUES ('Fitness Workshop', '2023-02-20', 'Workshop on nutrition and exercise');
INSERT INTO Activity (ActivityName, Date, Description) VALUES ('Networking', '2023-03-20', 'Get to know each other');
INSERT INTO Activity (ActivityName, Date, Description) VALUES ('Tea and Talk', '2023-04-20', 'Enjoy biscuits not just exercise');
INSERT INTO Activity (ActivityName, Date, Description) VALUES ('Swim Class', '2023-05-20', 'Float to not die');

-- Deleting an Activity
DELETE FROM Activity WHERE ActivityID = 1;

-- Inserting a fitness goal for a member
INSERT INTO FitnessGoal (MemberID, GoalDescription) VALUES (1, 'Lose 10 pounds in 2 months');
INSERT INTO FitnessGoal (MemberID, GoalDescription) VALUES (1, 'Get taller in 10 days');
INSERT INTO FitnessGoal (MemberID, GoalDescription) VALUES (2, 'Lose eyesight');
INSERT INTO FitnessGoal (MemberID, GoalDescription) VALUES (3, 'Gain 10kg  of muscle');



-- Updating member's contact info
UPDATE Member SET ContactInfo = 'new@gmail.com' WHERE MemberID = 1;

-- Updating a training session notes
UPDATE TrainingSession SET Notes = 'Afternoon session' WHERE SessionID = 1;

-- Listing all members with their fitness goals
SELECT Member.MemberName, FitnessGoal.GoalDescription FROM Member LEFT JOIN FitnessGoal ON Member.MemberID = FitnessGoal.MemberID;

-- Listing all trainers
SELECT * FROM Trainer;


