

DROP TABLE IF EXISTS Equipment;
DROP TABLE IF EXISTS FitnessGoal;
DROP TABLE IF EXISTS Room;
DROP TABLE IF EXISTS Organize;
DROP TABLE IF EXISTS Equipment;
DROP TABLE IF EXISTS SessionTrainer;
DROP TABLE IF EXISTS Manage;
DROP TABLE IF EXISTS Schedule;
DROP TABLE IF EXISTS Billing;
DROP TABLE IF EXISTS LoyaltyProgram;
DROP TABLE IF EXISTS AdministrativeStaff;
DROP TABLE IF EXISTS TrainingSession;
DROP TABLE IF EXISTS Activity;
DROP TABLE IF EXISTS Trainer;
DROP TABLE IF EXISTS Member;

-- Member Table
CREATE TABLE Member (
    MemberID SERIAL PRIMARY KEY,
    Name VARCHAR(100) Not null,
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
    MemberID INT REFERENCES Member(MemberID) ON DELETE CASCADE,
    TrainerID INT REFERENCES Trainer(TrainerID)ON DELETE CASCADE,
    Date DATE,
    Notes TEXT
);

-- Activity Table
CREATE TABLE Activity (
    ActivityID SERIAL PRIMARY KEY,
    ActivityName VARCHAR(100),
    Date DATE,
    Description TEXT
);

-- Fitness Goal Table
CREATE TABLE FitnessGoal (
    GoalID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID)ON DELETE CASCADE,
    GoalDescription TEXT
);

-- Billing Table
CREATE TABLE Billing (
    BillID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID)ON DELETE CASCADE,
    Amount DECIMAL(10, 2),
    Date DATE
);

-- Loyalty Program Table
CREATE TABLE LoyaltyProgram (
    LoyaltyID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Member(MemberID)ON DELETE CASCADE,
    PointsEarned INT,
    PointsRedeemed INT
);


-- Room Table
CREATE TABLE Room (
    RoomID SERIAL PRIMARY KEY,
    RoomName VARCHAR(100),
    Capacity INT
);


-- Equipment Table
CREATE TABLE Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    EquipmentName VARCHAR(100),
    RoomID INT REFERENCES Room(RoomID)ON DELETE CASCADE,
    MaintenanceStatus BOOLEAN
);

-- Organize Table
CREATE TABLE Organize (
    StaffID SERIAL REFERENCES AdministrativeStaff(StaffID)ON DELETE CASCADE,
    ActivityID SERIAL REFERENCES Activity(ActivityID)ON DELETE CASCADE
);

-- Manage Table
CREATE TABLE Manage (
    StaffID SERIAL REFERENCES AdministrativeStaff(StaffID)ON DELETE CASCADE,
    MemberID SERIAL REFERENCES Member(MemberID)ON DELETE CASCADE
);

-- SessionTrainer Table
CREATE TABLE SessionTrainer (
    TrainerID SERIAL REFERENCES Trainer(Name)ON DELETE CASCADE
);

-- Schedule Table
CREATE TABLE Schedule (
    SessionID SERIAL REFERENCES Session(SessionID)ON DELETE CASCADE,
    MemberID SERIAL REFERENCES Member(MemberID)ON DELETE CASCADE
);