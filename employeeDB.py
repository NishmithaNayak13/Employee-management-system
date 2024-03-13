# importing mysql connector
from asyncio.windows_events import NULL
import mysql.connector


con = mysql.connector.connect(
host="localhost", user="root", password="mysql123", database="employeedb")


def Add_Employ():

	Id = input("Enter Employee Id : ")
	
	# Checking if Employee with given Id already Exist or Not
	if(check_employee(Id) == True):
		print("Employee already exists\nTry Again\n")
		menu()
	else:
		Name = input("Enter Employee Name : ")
		Post = input("Enter Employee Post : ")
		Salary = input("Enter Employee Salary : ")
		data = (Id, Name, Post, Salary)
	
		
		sql = 'insert into emp2 values(%s,%s,%s,%s)'
		c = con.cursor()
		
		
		c.execute(sql, data)
		
		con.commit()
		print("Employee Added Successfully ")
		menu()


def Promote_Employee():
	Id = int(input("Enter Employ's Id"))
	
	# Checking if Employee with given Id exist or not
	if(check_employee(Id) == False):
		print("Employee does not exists\nTry Again\n")
		menu()
	else:
		Amount = int(input("Enter increase in Salary"))
		
		sql = 'select salary from emp2 where id=%s'
		data = (Id,)
		c = con.cursor()
		
		c.execute(sql, data)
		
		r = c.fetchone()
		t = r[0]+Amount
		
		
		sql = 'update emp2 set salary=%s where id=%s'
		d = (t, Id)
		
		c.execute(sql, d)
		
		con.commit()
		print("Employee Promoted")
		menu()

# Function to Remove Employee with given Id
def Remove_Employ():
	Id = input("Enter Employee Id : ")
	
	
	if(check_employee(Id) == False):
		print("Employee does not exists\nTry Again\n")
		menu()
	else:
		
		sql = 'delete from emp2 where id=%s'
		data = (Id,)
		c = con.cursor()
		
		
		c.execute(sql, data)
		
		
		con.commit()
		print("Employee Removed")
		menu()

# Function To Check if Employee with given Id Exist or Not
def check_employee(employee_id):
	
	
	sql = 'select * from emp2 where id=%s'
	
	c = con.cursor(buffered=True)
	data = (employee_id,)
	
	c.execute(sql, data)
	
	r = c.rowcount
	if r == 1:
		return True
	else:
		return False

# Function to Display All Employees from Employee Table
def Display_Employees():
	

	sql = 'select * from emp2'
	c = con.cursor()
	

	c.execute(sql)
	

	r = c.fetchall()
	if r != NULL:
		for i in r:
			print("Employee Id : ", i[0])
			print("Employee Name : ", i[1])
			print("Employee Post : ", i[2])
			print("Employee Salary : ", i[3])
			print("----------------------------")
	else:
		print("No employee found!!")		
	menu()

# menu function to display menu
def menu():
	print("Employee Management Record")
	print("Press: ")
	print("1 to Add Employee")
	print("2 to Remove Employee ")
	print("3 to Promote Employee")
	print("4 to Display Employees")
	print("5 to Exit")

	ch = int(input("Enter your Choice "))
	if ch == 1:
		Add_Employ()
	elif ch == 2:
		Remove_Employ()
	elif ch == 3:
		Promote_Employee()
	elif ch == 4:
		Display_Employees()
	elif ch == 5:
		exit(0)
	else:
		print("Invalid Choice")
		menu()



menu()
