import psycopg2

# Establish connection to PostgreSQL
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Create a cursor object using the connection
cur = conn.cursor()

def add_member():
    print("Add a new member:")
    name = input("Enter member's name: ")
    contact_info = input("Enter contact info: ")
    fitness_goals = input("Enter fitness goals: ")

    # Insert new member into the Members table
    cur.execute("INSERT INTO Members (Name, ContactInfo, FitnessGoals) VALUES (%s, %s, %s)",
                (name, contact_info, fitness_goals))
    conn.commit()
    print("Member added successfully!")

def display_members():
    print("Listing all members:")
    cur.execute("SELECT * FROM Members")
    rows = cur.fetchall()
    for row in rows:
        print(f"MemberID: {row[0]}, Name: {row[1]}, Contact Info: {row[2]}, Fitness Goals: {row[3]}")

# Add functions for other tables similarly (Trainers, PersonalTrainingSessions, GroupFitnessClasses, Events, ExerciseRoutines, HealthMetrics, Rooms, Equipment, Billing)

# Function to display trainers
def display_trainers():
    print("Listing all trainers:")
    cur.execute("SELECT * FROM Trainers")
    rows = cur.fetchall()
    for row in rows:
        print(f"TrainerID: {row[0]}, Name: {row[1]}, Specialization: {row[2]}")

# Function to display personal training sessions
def display_personal_training_sessions():
    print("Listing all personal training sessions:")
    cur.execute("SELECT * FROM PersonalTrainingSessions")
    rows = cur.fetchall()
    for row in rows:
        print(f"SessionID: {row[0]}, MemberID: {row[1]}, TrainerID: {row[2]}, Date: {row[3]}, Notes: {row[4]}")

# Add functions for other tables similarly

# User interaction
while True:
    print("\nMenu:")
    print("1. Add a new member")
    print("2. Display all members")
    print("3. Display all trainers")
    print("4. Display all personal training sessions")
    # Add options for other tables

    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    if choice == "1":
        add_member()
    elif choice == "2":
        display_members()
    elif choice == "3":
        display_trainers()
    elif choice == "4":
        display_personal_training_sessions()
    # Add elif blocks for other tables

    elif choice == "10":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# Close cursor and connection
cur.close()
conn.close()
