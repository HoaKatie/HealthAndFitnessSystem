-- Member Table
DROP TABLE IF EXISTS Member;
CREATE TABLE Member (
    MemberID SERIAL PRIMARY KEY,
    Name VARCHAR(100) Not null,
    ContactInfo VARCHAR(100)
);

-- Trainer Table
DROP TABLE IF EXISTS Trainer;
CREATE TABLE Trainer (
    TrainerID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Specialization VARCHAR(100)
);

-- Administrative Staff Table
DROP TABLE IF EXISTS AdministrativeStaff;
CREATE TABLE AdministrativeStaff (
    StaffID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Role VARCHAR(100)
);

-- Training Session Table
DROP TABLE IF EXISTS TrainingSession;
CREATE TABLE TrainingSession (
    SessionID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    TrainerID INT REFERENCES Trainer(TrainerID),
    Date DATE,
    Notes TEXT
);

-- Activity Table
DROP TABLE IF EXISTS Activity;
CREATE TABLE Activity (
    ActivityID SERIAL PRIMARY KEY,
    ActivityName VARCHAR(100),
    Date DATE,
    Description TEXT
);

-- Fitness Goal Table
DROP TABLE IF EXISTS FitnessGoal;
CREATE TABLE FitnessGoal (
    GoalID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    GoalDescription TEXT
);

-- Billing Table
DROP TABLE IF EXISTS Billing;
CREATE TABLE Billing (
    BillID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    Amount DECIMAL(10, 2),
    Date DATE
);

-- Loyalty Program Table
DROP TABLE IF EXISTS LoyaltyProgram;
CREATE TABLE LoyaltyProgram (
    LoyaltyID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID),
    PointsEarned INT,
    PointsRedeemed INT
);


-- Room Table
DROP TABLE IF EXISTS Room;
CREATE TABLE Room (
    RoomID SERIAL PRIMARY KEY,
    RoomName VARCHAR(100),
    Capacity INT
);


-- Equipment Table
DROP TABLE IF EXISTS Equipment;
CREATE TABLE Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    EquipmentName VARCHAR(100),
    RoomID INT REFERENCES Room(RoomID),
    MaintenanceStatus BOOLEAN
);

-- Organize Table
DROP TABLE IF EXISTS Organize;
CREATE TABLE Organize (
    StaffID SERIAL REFERENCES Staff(StaffID),
    ActivityID SERIAL REFERENCES Activity(ActivityID)
);

-- Manage Table
DROP TABLE IF EXISTS Manage;
CREATE TABLE Manage (
    StaffID SERIAL REFERENCES Staff(StaffID),
    MemberID SERIAL REFERENCES Member(MemberID)
);

-- SessionTrainer Table
DROP TABLE IF EXISTS SessionTrainer;
CREATE TABLE SessionTrainer (
    TrainerID SERIAL REFERENCES Trainer(Name)
);

-- Schedule Table
DROP TABLE IF EXISTS Schedule;
CREATE TABLE Schedule (
    SessionID SERIAL REFERENCES Session(SessionID),
    MemberID SERIAL REFERENCES Member(MemberID)
);