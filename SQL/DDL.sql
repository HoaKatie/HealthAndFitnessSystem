-- Member Table
CREATE TABLE Member (
    MemberID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    ContactInfo VARCHAR(100)
);

-- Trainer Table
CREATE TABLE Trainer (
    TrainerID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Specialization VARCHAR(100)
);

-- Administrative Staff Table
CREATE TABLE AdministrativeStaff (
    StaffID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Role VARCHAR(100)
);

-- Training Session Table
CREATE TABLE TrainingSession (
    SessionID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    TrainerID INT REFERENCES Trainer(TrainerID),
    Date DATE,
    Notes TEXT
);

-- Event Table
CREATE TABLE Event (
    EventID SERIAL PRIMARY KEY,
    EventName VARCHAR(100),
    Date DATE,
    Description TEXT
);

-- Fitness Goal Table
CREATE TABLE FitnessGoal (
    GoalID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    GoalDescription TEXT
);

-- Billing Table
CREATE TABLE Billing (
    BillID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    Amount DECIMAL(10, 2),
    Date DATE
);

-- Loyalty Program Table
CREATE TABLE LoyaltyProgram (
    LoyaltyID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    PointsEarned INT,
    PointsRedeemed INT
);

-- Equipment Table
CREATE TABLE Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    EquipmentName VARCHAR(100),
    RoomID INT REFERENCES Room(RoomID),
    MaintenanceStatus BOOLEAN
);

-- Room Table
CREATE TABLE Room (
    RoomID SERIAL PRIMARY KEY,
    RoomName VARCHAR(100),
    Capacity INT
);



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
