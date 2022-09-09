import tkinter as tk
import mysql.connector
from tkinter import *


def submitact():

	psu_id = Username.get()

	print(f"The psu id entered by you is {psu_id}")

	content = logintodb(psu_id)

	textbox.delete(1.0,"end")
	for each in content:
		textbox.insert(END, each + '\n')




def logintodb(psu_id):

	db = mysql.connector.connect(host ="localhost",
								user = "root",
								password = "Ilaaksh@2500",
								db ="sunlab_homework1")
	cursor = db.cursor()


	status_query =  "SELECT stts from accounts where stu_id = %s"
	id = (str(psu_id),)

	content = []
	toggle = 1

	try:
		cursor.execute(status_query,id)
		status = cursor.fetchone()
		if status[0]:
			content.append("The account you logged in doesn't have access rights")
			print (" The account you logged in doesn't have access rights")
			toggle = 0

	
	except:
		toggle = 0
		content.append("Entered Penn state ID is not registered")
		print("Entered Penn state ID is not registered")
	

	if toggle: 
		# A Table in the database
		savequery = "SELECT stu_id, enter, departure FROM time_records"

		try:
			cursor.execute(savequery)
			myresult = cursor.fetchall()

			# Printing the result of the
			# query
			for each in myresult:
				content.append("PSU ID : " + str(each[0]))
				print("PSU ID : " + str(each[0]))
				content.append("Start Time: " + str(each[1] ))
				print("Start Time: " + str(each[1] ))
				content.append("End Time: " + str(each[2]))
				print("End Time: " + str(each[2])+ "\n")
			print("Query Executed successfully")

		except:
			db.rollback()
			print("Error occured")
	
	return content


root = tk.Tk()
root.geometry("1500x1500")
root.title("DBMS Login Page")


# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)


submitbtn = tk.Button(root, text ="Login",
					bg ='grey', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)

textbox = tk.Text(root, height = 10)
textbox.place(x = 150 , y = 300, width = 1000)


root.mainloop()