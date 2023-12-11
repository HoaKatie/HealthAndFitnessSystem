import psycopg2
import tkinter as tk

# Establish connection to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    port=5432,
    database="health&fitness"
)

# Create a cursor object using the connection
cur = conn.cursor()

# Function to add a new member
def add_member():
    name = name_entry.get()
    contact_info = contact_entry.get()

    # Insert new member into the Members table
    cur.execute("INSERT INTO Member (MemberName, ContactInfo) VALUES (%s, %s)", (name, contact_info))
    conn.commit()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Member added successfully!")

# Function to display members
def display_members():
    cur.execute("SELECT * FROM Member")
    rows = cur.fetchall()
    members_info = ""
    for row in rows:
        members_info += f"MemberID: {row[0]}, MemberName: {row[1]}, Contact Info: {row[2]}\n"
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, members_info)

# Function to add a new trainer
def add_trainer():
    trainer_name = trainer_name_entry.get()
    specialization = trainer_specialization_entry.get()

    # Insert new trainer into the Trainer table
    cur.execute("INSERT INTO Trainer (TrainerName, Specialization) VALUES (%s, %s)", (trainer_name, specialization))
    conn.commit()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Trainer added successfully!")

# Function to display trainers
def display_trainers():
    cur.execute("SELECT * FROM Trainer")
    rows = cur.fetchall()
    trainers_info = ""
    for row in rows:
        trainers_info += f"TrainerID: {row[0]}, TrainerName: {row[1]}, Specialization: {row[2]}\n"
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, trainers_info)

# Function to add a new fitness goal
def add_fitness_goal():
    member_id = goal_member_id_entry.get()
    goal_description = goal_description_entry.get()

    # Insert new fitness goal into the FitnessGoal table
    cur.execute("INSERT INTO FitnessGoal (MemberID, GoalDescription) VALUES (%s, %s)", (member_id, goal_description))
    conn.commit()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Fitness goal added successfully!")

# Function to display fitness goals
def display_fitness_goals():
    cur.execute("SELECT * FROM FitnessGoal")
    rows = cur.fetchall()
    fitness_goals_info = ""
    for row in rows:
        fitness_goals_info += f"GoalID: {row[0]}, MemberID: {row[1]}, Goal Description: {row[2]}\n"
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, fitness_goals_info)

# Create tkinter window
root = tk.Tk()
root.title("Health and Fitness Club Management")

# Create tkinter widgets for adding members
name_label = tk.Label(root, text="Member Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

contact_label = tk.Label(root, text="Contact Info:")
contact_label.pack()
contact_entry = tk.Entry(root)
contact_entry.pack()

add_member_button = tk.Button(root, text="Add Member", command=add_member)
add_member_button.pack()

# Create tkinter widgets for displaying members
display_members_button = tk.Button(root, text="Display Members", command=display_members)
display_members_button.pack()

# Create tkinter widgets for adding trainers
trainer_name_label = tk.Label(root, text="Trainer Name:")
trainer_name_label.pack()
trainer_name_entry = tk.Entry(root)
trainer_name_entry.pack()

trainer_specialization_label = tk.Label(root, text="Trainer Specialization:")
trainer_specialization_label.pack()
trainer_specialization_entry = tk.Entry(root)
trainer_specialization_entry.pack()

add_trainer_button = tk.Button(root, text="Add Trainer", command=add_trainer)
add_trainer_button.pack()

# Create tkinter widgets for displaying trainers
display_trainers_button = tk.Button(root, text="Display Trainers", command=display_trainers)
display_trainers_button.pack()

# Create tkinter widgets for adding fitness goals
goal_member_id_label = tk.Label(root, text="Member ID:")
goal_member_id_label.pack()
goal_member_id_entry = tk.Entry(root)
goal_member_id_entry.pack()

goal_description_label = tk.Label(root, text="Goal Description:")
goal_description_label.pack()
goal_description_entry = tk.Entry(root)
goal_description_entry.pack()

add_goal_button = tk.Button(root, text="Add Fitness Goal", command=add_fitness_goal)
add_goal_button.pack()

# Create tkinter widgets for displaying fitness goals
display_goals_button = tk.Button(root, text="Display Fitness Goals", command=display_fitness_goals)
display_goals_button.pack()

result_text = tk.Text(root, height=15, width=100)
result_text.pack()

root.mainloop()

# Close cursor and connection
cur.close()
conn.close()
