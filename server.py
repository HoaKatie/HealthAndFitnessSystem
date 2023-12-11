import psycopg2
from psycopg2 import Error
from datetime import datetime

# Function to establish a connection to the PostgreSQL database
def connect():
    try:
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgres",
            port=5432,
            database="health&fitness"
        )
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to PostgreSQL: {e}")
        return None
#Member functions
def getAllMembers():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Member")
            members = cursor.fetchall()

            for member in members:
                print(member)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all members: {e}")
    finally:
        if connection:
            connection.close()

def addMember(name, contact_info):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO Member (Name, ContactInfo) VALUES (%s, %s)"
            cursor.execute(insert_query, (name, contact_info))
            connection.commit()
            print("Member added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add member: {e}")

    finally:
        if connection:
            connection.close()

def updateMemberContactInfo(member_id, new_contact_info):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE Member SET ContactInfo = %s WHERE MemberID = %s"
            cursor.execute(update_query, (new_contact_info, member_id))
            connection.commit()
            print("Contact information updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update contact information: {e}")

    finally:
        if connection:
            connection.close()

def deleteMember(member_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM Member WHERE MemberID = %s"
            cursor.execute(delete_query, (member_id,))
            connection.commit()
            print("Member deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete member: {e}")

    finally:
        if connection:
            connection.close()

# Trainer functions
def getAllTrainers():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Trainer")
            trainers = cursor.fetchall()

            for trainer in trainers:
                print(trainer)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all trainers: {e}")
    finally:
        if connection:
            connection.close()

def addTrainer(name, specialization):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO Trainer (Name, Specialization) VALUES (%s, %s)"
            cursor.execute(insert_query, (name, specialization))
            connection.commit()
            print("Trainer added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add trainer: {e}")

    finally:
        if connection:
            connection.close()

def updateTrainerSpecialization(trainer_id, new_specialization):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE Trainer SET Specialization = %s WHERE TrainerID = %s"
            cursor.execute(update_query, (new_specialization, trainer_id))
            connection.commit()
            print("Trainer specialization updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update trainer specialization: {e}")

    finally:
        if connection:
            connection.close()

def deleteTrainer(trainer_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM Trainer WHERE TrainerID = %s"
            cursor.execute(delete_query, (trainer_id,))
            connection.commit()
            print("Trainer deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete trainer: {e}")

    finally:
        if connection:
            connection.close()

# AdministrativeStaff functions
def getAllAdministrativeStaff():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM AdministrativeStaff")
            admin_staff = cursor.fetchall()

            for staff in admin_staff:
                print(staff)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all administrative staff: {e}")
    finally:
        if connection:
            connection.close()

def addAdministrativeStaff(name, role):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO AdministrativeStaff (Name, Role) VALUES (%s, %s)"
            cursor.execute(insert_query, (name, role))
            connection.commit()
            print("Administrative staff added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add administrative staff: {e}")

    finally:
        if connection:
            connection.close()

def updateAdministrativeStaffRole(staff_id, new_role):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE AdministrativeStaff SET Role = %s WHERE StaffID = %s"
            cursor.execute(update_query, (new_role, staff_id))
            connection.commit()
            print("Administrative staff role updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update administrative staff role: {e}")

    finally:
        if connection:
            connection.close()

def deleteAdministrativeStaff(staff_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM AdministrativeStaff WHERE StaffID = %s"
            cursor.execute(delete_query, (staff_id,))
            connection.commit()
            print("Administrative staff deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete administrative staff: {e}")

    finally:
        if connection:
            connection.close()


# TrainingSession functions
def getAllTrainingSessions():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM TrainingSession")
            training_sessions = cursor.fetchall()

            for session in training_sessions:
                print(session)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all training sessions: {e}")
    finally:
        if connection:
            connection.close()

def addTrainingSession(member_id, trainer_id, date, notes):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO TrainingSession (MemberID, TrainerID, Date, Notes) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (member_id, trainer_id, date, notes))
            connection.commit()
            print("Training session added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add training session: {e}")

    finally:
        if connection:
            connection.close()

def updateTrainingSessionNotes(session_id, new_notes):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE TrainingSession SET Notes = %s WHERE SessionID = %s"
            cursor.execute(update_query, (new_notes, session_id))
            connection.commit()
            print("Training session notes updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update training session notes: {e}")

    finally:
        if connection:
            connection.close()

def deleteTrainingSession(session_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM TrainingSession WHERE SessionID = %s"
            cursor.execute(delete_query, (session_id,))
            connection.commit()
            print("Training session deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete training session: {e}")

    finally:
        if connection:
            connection.close()

# LoyaltyProgram functions
def getAllLoyaltyPrograms():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM LoyaltyProgram")
            loyalty_programs = cursor.fetchall()

            for program in loyalty_programs:
                print(program)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all loyalty programs: {e}")
    finally:
        if connection:
            connection.close()

def addLoyaltyProgram(member_id, points_earned, points_redeemed):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO LoyaltyProgram (MemberID, PointsEarned, PointsRedeemed) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (member_id, points_earned, points_redeemed))
            connection.commit()
            print("Loyalty program added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add loyalty program: {e}")

    finally:
        if connection:
            connection.close()

def updateLoyaltyProgramPointsEarned(loyalty_id, new_points_earned):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE LoyaltyProgram SET PointsEarned = %s WHERE LoyaltyID = %s"
            cursor.execute(update_query, (new_points_earned, loyalty_id))
            connection.commit()
            print("Loyalty program points earned updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update loyalty program points earned: {e}")

    finally:
        if connection:
            connection.close()

def deleteLoyaltyProgram(loyalty_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM LoyaltyProgram WHERE LoyaltyID = %s"
            cursor.execute(delete_query, (loyalty_id,))
            connection.commit()
            print("Loyalty program deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete loyalty program: {e}")

    finally:
        if connection:
            connection.close()

# Billing functions
def getAllBillings():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Billing")
            billings = cursor.fetchall()

            for billing in billings:
                print(billing)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all billings: {e}")
    finally:
        if connection:
            connection.close()

def addBilling(member_id, amount, date):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO Billing (MemberID, Amount, Date) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (member_id, amount, date))
            connection.commit()
            print("Billing record added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add billing record: {e}")

    finally:
        if connection:
            connection.close()

def updateBillingAmount(bill_id, new_amount):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE Billing SET Amount = %s WHERE BillID = %s"
            cursor.execute(update_query, (new_amount, bill_id))
            connection.commit()
            print("Billing amount updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update billing amount: {e}")

    finally:
        if connection:
            connection.close()

def deleteBilling(bill_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM Billing WHERE BillID = %s"
            cursor.execute(delete_query, (bill_id,))
            connection.commit()
            print("Billing record deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete billing record: {e}")

    finally:
        if connection:
            connection.close()

# Room functions
def getAllRooms():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Room")
            rooms = cursor.fetchall()

            for room in rooms:
                print(room)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all rooms: {e}")
    finally:
        if connection:
            connection.close()

def addRoom(room_name, capacity):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO Room (RoomName, Capacity) VALUES (%s, %s)"
            cursor.execute(insert_query, (room_name, capacity))
            connection.commit()
            print("Room added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add room: {e}")

    finally:
        if connection:
            connection.close()

def updateRoomCapacity(room_id, new_capacity):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE Room SET Capacity = %s WHERE RoomID = %s"
            cursor.execute(update_query, (new_capacity, room_id))
            connection.commit()
            print("Room capacity updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update room capacity: {e}")

    finally:
        if connection:
            connection.close()

def deleteRoom(room_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM Room WHERE RoomID = %s"
            cursor.execute(delete_query, (room_id,))
            connection.commit()
            print("Room deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete room: {e}")

    finally:
        if connection:
            connection.close()

# Equipment functions
def getAllEquipment():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Equipment")
            equipment = cursor.fetchall()

            for item in equipment:
                print(item)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all equipment: {e}")
    finally:
        if connection:
            connection.close()

def addEquipment(equipment_name, room_id, maintenance_status):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO Equipment (EquipmentName, RoomID, MaintenanceStatus) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (equipment_name, room_id, maintenance_status))
            connection.commit()
            print("Equipment added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add equipment: {e}")

    finally:
        if connection:
            connection.close()

def updateEquipmentMaintenanceStatus(equipment_id, new_maintenance_status):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE Equipment SET MaintenanceStatus = %s WHERE EquipmentID = %s"
            cursor.execute(update_query, (new_maintenance_status, equipment_id))
            connection.commit()
            print("Equipment maintenance status updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update equipment maintenance status: {e}")

    finally:
        if connection:
            connection.close()

def deleteEquipment(equipment_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM Equipment WHERE EquipmentID = %s"
            cursor.execute(delete_query, (equipment_id,))
            connection.commit()
            print("Equipment deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete equipment: {e}")

    finally:
        if connection:
            connection.close()

# FitnessGoal functions

def getAllFitnessGoals():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM FitnessGoal")
            fitness_goals = cursor.fetchall()

            for goal in fitness_goals:
                print(goal)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all fitness goals: {e}")
    finally:
        if connection:
            connection.close()

def addFitnessGoal(member_id, goal_description):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO FitnessGoal (MemberID, GoalDescription) VALUES (%s, %s)"
            cursor.execute(insert_query, (member_id, goal_description))
            connection.commit()
            print("Fitness goal added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add fitness goal: {e}")

    finally:
        if connection:
            connection.close()

def updateFitnessGoalDescription(goal_id, new_description):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE FitnessGoal SET GoalDescription = %s WHERE GoalID = %s"
            cursor.execute(update_query, (new_description, goal_id))
            connection.commit()
            print("Fitness goal description updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update fitness goal description: {e}")

    finally:
        if connection:
            connection.close()

def deleteFitnessGoal(goal_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM FitnessGoal WHERE GoalID = %s"
            cursor.execute(delete_query, (goal_id,))
            connection.commit()
            print("Fitness goal deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete fitness goal: {e}")

    finally:
        if connection:
            connection.close()


# Activity functions

def getAllActivities():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Activity")
            activities = cursor.fetchall()

            for activity in activities:
                print(activity)

            cursor.close()
    except Exception as e:
        print(f"Error: Unable to get all activities: {e}")
    finally:
        if connection:
            connection.close()

def addActivity(activity_name, date, description):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO Activity (ActivityName, Date, Description) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (activity_name, date, description))
            connection.commit()
            print("Activity added successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to add activity: {e}")

    finally:
        if connection:
            connection.close()

def updateActivityDescription(activity_id, new_description):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE Activity SET Description = %s WHERE ActivityID = %s"
            cursor.execute(update_query, (new_description, activity_id))
            connection.commit()
            print("Activity description updated successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to update activity description: {e}")

    finally:
        if connection:
            connection.close()

def deleteActivity(activity_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM Activity WHERE ActivityID = %s"
            cursor.execute(delete_query, (activity_id,))
            connection.commit()
            print("Activity deleted successfully")
            cursor.close()

    except Exception as e:
        print(f"Error: Unable to delete activity: {e}")

    finally:
        if connection:
            connection.close()

# Example usage of the functions
def main():
    print("\nInput 0-10 to interact with tables:\n")
    print("Quit application: 0")
    print("Interact with Members Table: 1")
    print("Interact with Trainers Table: 2")
    print("Interact with Administrative Staff Table: 3")
    print("Interact with Training Session Table: 4")
    print("Interact with Activities Table: 5")
    print("Interact with Fitness Goals Table: 6")
    print("Interact with Billing Table: 7")
    print("Interact with Loyalty Program Table: 8")
    print("Interact with Rooms Table: 9")
    print("Interact with Equipment Table: 10 \n")
    # Add more options for the remaining tables

    while True:
        try:
            choice = int(input("\nChoose your number: "))

            print("\nGet All From Table: 1")
            print("New Input Entry to Table: 2")
            print("Update Entry of Table: 3")
            print("Delete Entry of Table: 4 \n")
            operation = int(input("\nChoose your number : "))
            if choice == 0:
                print("Exiting application.")
                break
            elif choice == 1: 
                if operation == 1:
                    print("All members from Member table:")
                    getAllMembers()
                elif operation == 2:
                    name = input("Enter new member's name: ")
                    contact_info = input("Enter new member's contact info: ")
                    addMember(name, contact_info)
                elif operation == 3:
                    id = int(input("Enter MemberID to update contact info: "))
                    new_contact_info = input("Enter new contact info: ")
                    updateMemberContactInfo(id, new_contact_info)
                elif operation == 4:
                    delete_id = int(input("Enter MemberID to delete that member: "))
                    deleteMember(delete_id)
            elif choice == 2: 
                if operation == 1:
                    print("All trainers from Trainer table:")
                    getAllTrainers()
                elif operation == 2:
                    name = input("Enter new trainer's name: ")
                    specialization = input("Enter new trainer's specialization: ")
                    addTrainer(name, specialization)
                elif operation == 3:
                    id = int(input("Enter TrainerID to update specialization: "))
                    new_specialization = input("Enter new specialization: ")
                    updateTrainerSpecialization(id, new_specialization)
                elif operation == 4:
                    delete_id = int(input("Enter TrainerID to delete that trainer: "))
                    deleteTrainer(delete_id)
            elif choice == 3: 
                if operation == 1:
                    print("All staff members from AdministrativeStaff table:")
                    getAllAdministrativeStaff()
                elif operation == 2:
                    name = input("Enter new staff member's name: ")
                    role = input("Enter new staff member's role: ")
                    addAdministrativeStaff(name, role)
                elif operation == 3:
                    id = int(input("Enter StaffID to update role: "))
                    new_role = input("Enter new role: ")
                    updateStaffRole(id, new_role)
                elif operation == 4:
                    delete_id = int(input("Enter StaffID to delete that staff member: "))
                    deleteAdministrativeStaff(delete_id)
            elif choice == 4: 
                if operation == 1:
                    print("All training sessions from TrainingSession table:")
                    getAllTrainingSessions()
                elif operation == 2:
                    member_id = int(input("Enter MemberID for the session: "))
                    trainer_id = int(input("Enter TrainerID for the session: "))
                    date = input("Enter session date (YYYY-MM-DD): ")
                    notes = input("Enter session notes: ")
                    addTrainingSession(member_id, trainer_id, date, notes)
                elif operation == 3:
                    session_id = int(input("Enter SessionID to update notes: "))
                    new_notes = input("Enter new notes: ")
                    updateTrainingSessionNotes(session_id, new_notes)
                elif operation == 4:
                    delete_id = int(input("Enter SessionID to delete that training session: "))
                    deleteTrainingSession(delete_id)
            elif choice == 5: 
                if operation == 1:
                    print("All activities from Activities table:")
                    getAllActivities()
                elif operation == 2:
                    activity_name = input("Enter activity name: ")
                    date = input("Enter activity date (YYYY-MM-DD): ")
                    description = input("Enter activity description: ")
                    addActivity(activity_name, date, description)
                elif operation == 3:
                    activity_id = int(input("Enter ActivityID to update description: "))
                    new_description = input("Enter new description: ")
                    updateActivityDescription(activity_id, new_description)
                elif operation == 4:
                    delete_id = int(input("Enter ActivityID to delete that activity: "))
                    deleteActivity(delete_id)
            elif choice == 6: 
                if operation == 1:
                    print("All fitness goals from FitnessGoal table:")
                    getAllFitnessGoals()
                elif operation == 2:
                    member_id = int(input("Enter MemberID for the fitness goal: "))
                    goal_description = input("Enter fitness goal description: ")
                    addFitnessGoal(member_id, goal_description)
                elif operation == 3:
                    goal_id = int(input("Enter GoalID to update description: "))
                    new_description = input("Enter new description: ")
                    updateFitnessGoalDescription(goal_id, new_description)
                elif operation == 4:
                    delete_id = int(input("Enter GoalID to delete that fitness goal: "))
                    deleteFitnessGoal(delete_id)
            elif choice == 7: 
                if operation == 1:
                    print("All billings from Billing table:")
                    getAllBillings()
                elif operation == 2:
                    member_id = int(input("Enter MemberID for the billing record: "))
                    amount = float(input("Enter billing amount: "))
                    date = input("Enter billing date (YYYY-MM-DD): ")
                    addBilling(member_id, amount, date)
                elif operation == 3:
                    bill_id = int(input("Enter BillID to update amount: "))
                    new_amount = float(input("Enter new amount: "))
                    updateBillingAmount(bill_id, new_amount)
                elif operation == 4:
                    delete_id = int(input("Enter BillID to delete that billing record: "))
                    deleteBilling(delete_id)
            elif choice == 8: 
                if operation == 1:
                    print("All loyalty program records from LoyaltyProgram table:")
                    getAllLoyaltyProgramRecords()
                elif operation == 2:
                    member_id = int(input("Enter MemberID for the loyalty program record: "))
                    points_earned = int(input("Enter points earned: "))
                    points_redeemed = int(input("Enter points redeemed: "))
                    addLoyaltyProgramRecord(member_id, points_earned, points_redeemed)
                elif operation == 3:
                    loyalty_id = int(input("Enter LoyaltyID to update points earned and redeemed: "))
                    new_points_earned = int(input("Enter new points earned: "))
                    new_points_redeemed = int(input("Enter new points redeemed: "))
                    updateLoyaltyProgramRecord(loyalty_id, new_points_earned, new_points_redeemed)
                elif operation == 4:
                    delete_id = int(input("Enter LoyaltyID to delete that loyalty program record: "))
                    deleteLoyaltyProgramRecord(delete_id)
            elif choice == 9: 
                if operation == 1:
                    print("All rooms from Room table:")
                    getAllRooms()
                elif operation == 2:
                    room_name = input("Enter room name: ")
                    capacity = int(input("Enter room capacity: "))
                    addRoom(room_name, capacity)
                elif operation == 3:
                    room_id = int(input("Enter RoomID to update capacity: "))
                    new_capacity = int(input("Enter new capacity: "))
                    updateRoomCapacity(room_id, new_capacity)
                elif operation == 4:
                    delete_id = int(input("Enter RoomID to delete that room: "))
                    deleteRoom(delete_id)
            elif choice == 10: 
                if operation == 1:
                    print("All equipment from Equipment table:")
                    getAllEquipment()
                elif operation == 2:
                    equipment_name = input("Enter equipment name: ")
                    room_id = int(input("Enter RoomID for the equipment: "))
                    maintenance_status = input("Enter maintenance status (True/False): ")
                    addEquipment(equipment_name, room_id, maintenance_status)
                elif operation == 3:
                    equipment_id = int(input("Enter EquipmentID to update maintenance status: "))
                    new_maintenance_status = input("Enter new maintenance status (True/False): ")
                    updateEquipmentMaintenanceStatus(equipment_id, new_maintenance_status)
                elif operation == 4:
                    delete_id = int(input("Enter EquipmentID to delete that equipment: "))
                    deleteEquipment(delete_id)
            else:
                print("Error: Please enter an integer from 0 to 10.")
        except ValueError:
            print("Error: Please enter an integer from 0 to 10.")

main()
