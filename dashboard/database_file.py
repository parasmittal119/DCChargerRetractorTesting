import datetime
import sqlite3
import os
import time
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import getpass
import subprocess


class Database:
    def __init__(self):
        self.shared_folder_path = "C:\\Users\\paras.mittal\\Desktop\\"

        self.database_name = "retractor_database.db"

    def connect_DB(self):
        # return True
        try:
            # print(self.time_check(timeout=1))
            account_user = getpass.getuser()
            self.dblocation = open(f"C:/Users/{account_user}/AppData/Local/retractorDBLocation/source.txt",
                                   "r").readline()
            # self.dblocation = self.shared_folder_path + self.database_name
            print(self.dblocation)
            if True:

                self.connection = sqlite3.connect(self.dblocation, 0.5)
                # self.connection = sqlite3.connect(self.dblocation)

                self.cursor = self.connection.cursor()

                print("Database Connected")
                return True
            else:
                return False

        except (sqlite3.DatabaseError, Exception) as err:
            if str(err) == "'Database' object has no attribute 'cursor'":
                self.Message("Error2", "Database not connected, Kindly connect to server!")
                return None
            if str(err) == "":
                self.Message("Error1", "Database not connected, can't proceed testing!")
                return None
            print(err)
            print("Database Not connected, check above error for debugging.")
            self.Message("Error3", "Database Connection issue")
            return None

    def time_check(self):
        # return True
        try:
            # Run the ipconfig command and capture the output
            result = subprocess.run(['ipconfig'], capture_output=True, text= True)

            # Check if the command was successful
            if result.returncode == 0:
                # Print the ipconfig output
                # print(result.stdout)

                # Extract relevant information (customize as needed)
                lines = result.stdout.split('\n')
                for line in lines:
                    if "IPv4 Address. . . . . . . . . . . : 172.16.21." in line:
                        print(f"Connected to network: {line.strip()}")
                        return True
                else:
                    print(f"Error running ipconfig: {result.stderr}")
                    return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def writeDetails(self, serialNumber, associateName, startTime, endTime, result):
        try:
            self.cursor.execute("INSERT INTO TestLog (serial_number, associated_name, start_time, end_time, Result)"
                                f"Values ('{serialNumber}','{associateName}', '{startTime}', '{endTime}','{result}')")
            self.connection.commit()

            self.cursor.execute(f"SELECT Test_ID from Testlog where Start_Time = '{startTime}'")
            dataValue = self.cursor.fetchall()
            for i in dataValue:
                print(f"Current Test_ID: {i[0]}")
                return i[0]
        except (sqlite3.DatabaseError, Exception) as err:
            print(err)
            if str(err) == "'Database' object has no attribute 'cursor'":
                self.Message("Error2", "Database not connected, Kindly connect to server!")
                return None
            if str(err) == "":
                self.Message("Error1", "Database not connected, can't proceed testing!")
                return None
            print("Database Not connected, check above error for debugging.")
            return None

    def writeEndtime(self, testID, endTime):
        try:
            self.cursor.execute(f"UPDATE TestLog SET end_time = '{endTime}' where Test_ID = {testID}")
            self.connection.commit()
        except (sqlite3.DatabaseError, Exception) as err:
            if str(err) == "'Database' object has no attribute 'cursor'":
                self.Message("Error2", "Database not connected, Kindly connect to server!")
                return None
            if str(err) == "":
                self.Message("Error1", "Database not connected, can't proceed testing!")
                return None
            print("Database Not connected, check above error for debugging.")
            return None

    def searchQuery(self, query: str):
        try:
            self.cursor.execute(query)
            # self.connection.commit()
            data = self.cursor.fetchall()
            return data
        except (sqlite3.DatabaseError, Exception) as err:
            print(err)
            if str(err) == "'Database' object has no attribute 'cursor'":
                self.Message("Error2", "Database not connected, Kindly connect to server!")
                return None
            if str(err) == "":
                self.Message("Error1", "Database not connected, can't proceed testing!")
                return None
            print("Database Not connected, check above error for debugging.")
            return None

    def commitQuery(self, query: str):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except (sqlite3.DatabaseError, Exception) as err:
            print(err)
            if str(err) == "'Database' object has no attribute 'cursor'":
                self.Message("Error2", "Database not connected, Kindly connect to server!")
                return None
            if str(err) == "":
                self.Message("Error1", "Database not connected, can't proceed testing!")
                return None
            print("Database Not connected, check above error for debugging.")
            return None

    def writeDefaultLedStates(self, test_id):
        try:
            self.cursor.execute(
                f"INSERT INTO LedState Values ('{test_id}', 'Not Tested','Not Tested','Not Tested','Not Tested',"
                f"'Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested',"
                f"'Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested',"
                f"'Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested',"
                f"'Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested',"
                f"'Not Tested','Not Tested','Not Tested','Not Tested');")
            self.connection.commit()
        except (sqlite3.DatabaseError, Exception) as err:
            print(err)
            if str(err) == "'Database' object has no attribute 'cursor'":
                self.Message("Error2", "Database not connected, Kindly connect to server!")
                return None
            if str(err) == "":
                self.Message("Error1", "Database not connected, can't proceed testing!")
                return None
            print("Database Not connected, check above error for debugging.")
            return None

    def updateLedState(self, test_id: int, stateName: str, value: str):
        try:
            # print(f"UPDATE LedState SET '{stateName}' = {value} where testId = {test_id}")
            self.cursor.execute(f"UPDATE LedState SET '{stateName}' = {value} where testId = {test_id}")
            self.connection.commit()
        except (sqlite3.DatabaseError, Exception) as err:
            if str(err) == "'Database' object has no attribute 'cursor'":
                self.Message("Error2", "Database not connected, Kindly connect to server!")
                return None
            if str(err) == "":
                self.Message("Error1", "Database not connected, can't proceed testing!")
                print("Database Not connected, check above error for debugging.")
                return None
            else:
                print("Updation failed due to following error:")
                print(err)
                self.connection.rollback()
                return None

    def disconnectDB(self):
        try:
            self.cursor.close()
            self.connection.close()
            print('Database Disconnected!')
        except (sqlite3.DatabaseError, Exception) as err:
            print(err)
            if str(err) == "'Database' object has no attribute 'cursor'":
                self.Message("Error2", "Database not connected, Kindly connect to server!")
                return None
            if str(err) == "":
                self.Message("Error1", "Database not connected, can't proceed testing!")
                return None
            print("Database Not connected, check above error for debugging.")
            return None

    def DBisConnect(self):
        print("IN DBISCONNECT")
        try:
            if os.path.exists(self.shared_folder_path):
                self.searchQuery("Select * from TestLog")
                return True
            else:
                return False
        except Exception as err:
            print(err)
            if str(err) == "Cannot operate on a closed cursor.":
                self.connect_DB()

    def finalStatusDB(self, value, test_id):
        try:
            # print(f"UPDATE Testlog SET Result = '{value}' where Test_ID = {test_id}")
            self.cursor.execute(f"UPDATE Testlog SET Result = '{value}' where Test_ID = {test_id}")
            self.connection.commit()
        except (sqlite3.DatabaseError, Exception) as err:
            print("Updation failed due to following error:")
            print(err)
            self.connection.rollback()
            return None

    def Message(self, title: str = "MESSAGE", prompt: str = ""):
        self.message = QMessageBox()
        self.message.setWindowTitle(title)
        self.message.setWindowIcon(QIcon(f"{os.getcwd()}\images\logo_1.png"))
        self.message.setText(prompt)
        self.message.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.message.exec_()


'''Table Creation'''
# cursor.execute("CREATE TABLE TestLog (Test_ID INTEGER PRIMARY KEY AUTOINCREMENT, Serial_Number VARCHAR(255) NOT NULL, Associated_Name VARCHAR(255) NOT NULL, Start_Time TIMESTAMP, End_Time TIMESTAMP);")
# cursor.execute("CREATE TABLE LedState (testId INT PRIMARY KEY,    "
#                "'Idle Idle' VARCHAR(32) NOT NULL,    'Idle Preparing' VARCHAR(32) NOT NULL,"
#                "'Idle Charging' VARCHAR(32) NOT NULL,    'Idle Finishing' VARCHAR(32) NOT NULL,"
#                "'Idle Faulted' VARCHAR(32) NOT NULL,    'Idle Reserved' VARCHAR(32) NOT NULL,"
#
#                 "'Preparing Idle' VARCHAR(32) NOT NULL,    'Preparing Preparing' VARCHAR(32) NOT NULL,"
#                "'Preparing Charging' VARCHAR(32) NOT NULL,    'Preparing Finishing' VARCHAR(32) NOT NULL,"
#                "'Preparing Faulted' VARCHAR(32) NOT NULL,    'Preparing Reserved' VARCHAR(32) NOT NULL,"
#
#                "'Charging Idle' VARCHAR(32) NOT NULL,    'Charging Preparing' VARCHAR(32) NOT NULL,"
#                "'Charging Charging' VARCHAR(32) NOT NULL,    'Charging Finishing' VARCHAR(32) NOT NULL,"
#                "'Charging Faulted' VARCHAR(32) NOT NULL,    'Charging Reserved' VARCHAR(32) NOT NULL,"
#
#                 "'Finishing Idle' VARCHAR(32) NOT NULL,    'Finishing Preparing' VARCHAR(32) NOT NULL,"
#                "'Finishing Charging' VARCHAR(32) NOT NULL,    'Finishing Finishing' VARCHAR(32) NOT NULL,"
#                "'Finishing Faulted' VARCHAR(32) NOT NULL,    'Finishing Reserved' VARCHAR(32) NOT NULL,"
#
#                "'Faulted Idle' VARCHAR(32) NOT NULL,    'Faulted Preparing' VARCHAR(32) NOT NULL,"
#                "'Faulted Charging' VARCHAR(32) NOT NULL,    'Faulted Finishing' VARCHAR(32) NOT NULL,"
#                "'Faulted Faulted' VARCHAR(32) NOT NULL,    'Faulted Reserved' VARCHAR(32) NOT NULL,"
#
#                 "'Reserved Idle' VARCHAR(32) NOT NULL,    'Reserved Preparing' VARCHAR(32) NOT NULL,"
#                "'Reserved Charging' VARCHAR(32) NOT NULL,    'Reserved Finishing' VARCHAR(32) NOT NULL,"
#                "'Reserved Faulted' VARCHAR(32) NOT NULL,    'Reserved Reserved' VARCHAR(32) NOT NULL,"
#
#                " FOREIGN KEY (testId) REFERENCES TestLog(test_id));")
# connection.commit()
'''Table Created'''
#
# var = "'Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested','Not Tested'"
#
#
# s = Database()
# s.connect_DB()
# # #
# # # s.searchQuery("ALTER TABLE Testlog ADD COLUMN Result Varchar(255);")
# da = s.searchQuery("select * from Testlog where Start_Time >= '2024-01-18 00:00:00' and End_Time <= '2024-01-19%';")
# print(da)
# print(s.searchQuery("select * from LedState where testId = 81"))
# # s.commitQuery("DELETE FROM Testlog")
# s.commitQuery("DELETE FROM LedState")
