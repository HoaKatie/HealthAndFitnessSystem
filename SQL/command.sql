

-- Inserting a new member
INSERT INTO Member (Name, ContactInfo) VALUES ('John Doe', 'john@example.com');

-- Inserting a new trainer
INSERT INTO Trainer (Name, Specialization) VALUES ('Sarah Smith', 'Yoga');

-- Inserting a training session
INSERT INTO TrainingSession (MemberID, TrainerID, Date, Notes) VALUES (1, 1, '2023-01-10', 'Morning session');

-- Inserting an event
INSERT INTO Event (EventName, Date, Description) VALUES ('Fitness Workshop', '2023-02-20', 'Workshop on nutrition and exercise');

-- Inserting a fitness goal for a member
INSERT INTO FitnessGoal (MemberID, GoalDescription) VALUES (1, 'Lose 10 pounds in 2 months');

-- Updating member's contact info
UPDATE Member SET ContactInfo = 'newemail@example.com' WHERE MemberID = 1;

-- Updating a training session notes
UPDATE TrainingSession SET Notes = 'Afternoon session' WHERE SessionID = 1;

-- Listing all members with their fitness goals
SELECT Member.Name, FitnessGoal.GoalDescription FROM Member LEFT JOIN FitnessGoal ON Member.MemberID = FitnessGoal.MemberID;

-- Listing all trainers
SELECT * FROM Trainer;

-- Deleting an event
DELETE FROM Event WHERE EventID = 1;
