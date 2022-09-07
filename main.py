import tkinter as tk
import mysql.connector
from tkinter import *


def submitact():

	psu_id = Username.get()

	print(f"The psu id entered by you is {psu_id}")

	logintodb(psu_id)


def logintodb(psu_id):

	db = mysql.connector.connect(host ="localhost",
								user = "root",
								password = "Ilaaksh@2500",
								db ="sunlab_homework1")
	cursor = db.cursor()


	status_query =  "SELECT stts from accounts where stu_id = %s"
	id = (str(psu_id),)


	toggle = 0

	try:
		cursor.execute(status_query,id)
		status = cursor.fetchone()
		if status[0]:
			print (" The account you logged in doesn't have access rights")
			toggle=1

	
	except:
		print("Entered Penn state ID is not registered")
	

	if not toggle: 
		# A Table in the database
		savequery = "SELECT stu_id, enter, departure FROM time_records"

		try:
			cursor.execute(savequery)
			myresult = cursor.fetchall()

			# Printing the result of the
			# query
			for x in myresult:
				print(x)
			print("Query Executed successfully")

		except:
			db.rollback()
			print("Error occured")


root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")


# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)


submitbtn = tk.Button(root, text ="Login",
					bg ='grey', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)

root.mainloop()
