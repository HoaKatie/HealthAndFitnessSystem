import psycopg2
import tkinter as tk

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

# Function to add a new member
def add_member():
    name = name_entry.get()
    contact_info = contact_entry.get()
    fitness_goals = goals_entry.get()

    # Insert new member into the Members table
    cur.execute("INSERT INTO Members (Name, ContactInfo, FitnessGoals) VALUES (%s, %s, %s)",
                (name, contact_info, fitness_goals))
    conn.commit()
    result_label.config(text="Member added successfully!")

# Function to display members
def display_members():
    cur.execute("SELECT * FROM Members")
    rows = cur.fetchall()
    members_info = ""
    for row in rows:
        members_info += f"MemberID: {row[0]}, Name: {row[1]}, Contact Info: {row[2]}, Fitness Goals: {row[3]}\n"
    result_label.config(text=members_info)

# Create tkinter window
root = tk.Tk()
root.title("Health and Fitness Club Management")

# Create tkinter widgets
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

contact_label = tk.Label(root, text="Contact Info:")
contact_label.pack()
contact_entry = tk.Entry(root)
contact_entry.pack()

goals_label = tk.Label(root, text="Fitness Goals:")
goals_label.pack()
goals_entry = tk.Entry(root)
goals_entry.pack()

add_button = tk.Button(root, text="Add Member", command=add_member)
add_button.pack()

display_button = tk.Button(root, text="Display Members", command=display_members)
display_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

# Close cursor and connection
cur.close()
conn.close()
