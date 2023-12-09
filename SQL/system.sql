-- SQL commands to create tables for the Health and Fitness Club Management System

CREATE TABLE Members (
    MemberID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    ContactInfo VARCHAR(100),
    FitnessGoals TEXT
);

CREATE TABLE Trainers (
    TrainerID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Specialization VARCHAR(100)
);

CREATE TABLE PersonalTrainingSessions (
    SessionID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Members(MemberID),
    TrainerID INT REFERENCES Trainers(TrainerID),
    Date DATE,
    Notes TEXT
);

CREATE TABLE GroupFitnessClasses (
    ClassID SERIAL PRIMARY KEY,
    ClassName VARCHAR(100),
    Schedule VARCHAR(100),
    TrainerID INT REFERENCES Trainers(TrainerID)
);

CREATE TABLE Events (
    EventID SERIAL PRIMARY KEY,
    EventName VARCHAR(100),
    Date DATE,
    Description TEXT
);

CREATE TABLE ExerciseRoutines (
    RoutineID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Members(MemberID),
    Description TEXT,
    Duration INT -- Assuming duration in minutes
);

CREATE TABLE HealthMetrics (
    MetricID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Members(MemberID),
    MetricType VARCHAR(100),
    Value FLOAT, -- Assuming numerical value
    Date DATE
);

CREATE TABLE Rooms (
    RoomID SERIAL PRIMARY KEY,
    RoomName VARCHAR(100),
    Capacity INT
);

CREATE TABLE Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    EquipmentName VARCHAR(100),
    RoomID INT REFERENCES Rooms(RoomID),
    MaintenanceStatus BOOLEAN -- Assuming maintenance status as a boolean
);

CREATE TABLE Billing (
    BillID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Members(MemberID),
    Amount DECIMAL(10, 2), -- Assuming currency amount
    Description TEXT,
    Date DATE
);
