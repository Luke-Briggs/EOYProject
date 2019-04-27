# Luke Briggs
# R00172161
# Project 2019
#
# Need a main function, load_data, view specific employee, edit salary,
# add employee, delete employee, give bonus to all employees, Generate report and Quit.


# main function need 8 other functions.
def main():
    filename = "project.txt"
    (employee_id_list, firstname_list, surname_list, email_list, salary_list) = load_data(filename)
    quit = menu(employee_id_list, firstname_list, surname_list, email_list, salary_list)
    print(quit)


# Function to put all values into various arrays
def load_data(filename):
    # Opening file and reading out the lines
    data_file = open(filename)
    lines = data_file.readline()
    # Creating empty lists to add people in
    employee_id_list = []
    firstname_list = []
    surname_list = []
    email_list = []
    salary_list = []

    # Making a loop to add values into arrays.
    while len(lines) > 0:
        temparray = lines.split(",")

        if temparray == " ":
            break
        else:
            employee_id_list.append(int(temparray[0]))
            firstname_list.append(temparray[1])
            surname_list.append(temparray[2])
            email_list.append(temparray[3])
            salary_temp = temparray[4][0:len(temparray[4]) - 2]
            salary_list.append(float(salary_temp))
            lines = data_file.readline()

    # Returning values
    return employee_id_list, firstname_list, surname_list, email_list, salary_list

# Show all employee details
def showEmpDetails(employee_id_list, firstname_list, surname_list, email_list, salary_list):
    print("")
    print("===================")
    print("")
    # For loop to put group each employees details together.
    for i in range(0,len(employee_id_list)):
        print("Employee ID: "+str(employee_id_list[i]) )
        print("Name: " + firstname_list[i] + " " +surname_list[i])
        print("Email: " + email_list[i])
        print("Salary: " + str(salary_list[i]))
        print("")
        print("===================")
        print("")

# Menu function for the user to choose what they want to do
def menu(employee_id_list, firstname_list, surname_list, email_list, salary_list):
    while True:
        choose = input("Would you like to 1. View all employee information, 2. View one employee, 3. Edit an employees salary "
                       "4. Add new employee 5. Delete an employee 6. Give Bonus 7. Make a Report 8. Quit.")
        if choose == "1":
            showEmpDetails(employee_id_list, firstname_list, surname_list, email_list, salary_list)
        elif choose == "2":
            emp_details = one_emp(employee_id_list, firstname_list, surname_list, email_list, salary_list)
        elif choose == "3":
            salary_change = emp_sal_change(salary_list, firstname_list, surname_list, email_list, employee_id_list)
            print(salary_change)
        elif choose == "4":
            added = add_emp(employee_id_list, firstname_list, surname_list, email_list, salary_list)
            print("Employee has been added.")
        elif choose == "5":
            delete = delete_emp(employee_id_list, firstname_list, surname_list, email_list, salary_list)
            print(delete)
        elif choose == "6":
            new_sal = bonus_to_all(firstname_list, surname_list, salary_list)
            print(new_sal)
        elif choose == "7":
            report, average, highest_salary = overall_report(firstname_list, salary_list)
            print("")
            print("=============================================================================")
            print(report + "\n\n" + average + "\n\n" + highest_salary + "\n")
            print("=============================================================================")
            print("")
        elif choose == "8":
            quit = ("Okey dokey, byeee")
            return quit

# Looking at an employee
def one_emp(employee_id_list, firstname_list, surname_list, email_list, salary_list):
    emp_id = input("Please enter the employee id: ")

    # Make sure there's something entered
    while True:
        if len(emp_id) == 0:
            emp_id = input("Please input a value: ")
        else:
            break

    # Make sure its a number
    while True:
        if emp_id.isalpha():
            emp_id = input("Please enter a number, try again: ")
        else:
            break

    # Make sure the employee ID exists
    while True:
        if int(emp_id) not in employee_id_list:
            emp_id = input("Not a valid id, try again: ")
        else:
            break

    emp_id = int(emp_id)

    for i in range(0, len(employee_id_list)):
        if emp_id == employee_id_list[i]:
            print("")
            print("===================")
            print("")
            print("Employee ID: " + str(employee_id_list[i]))
            print("Name: " + firstname_list[i] + " " + surname_list[i])
            print("Email: " + email_list[i])
            print("Salary: " + str(salary_list[i]))
            print("")
            print("===================")
            print("")
            break

# Function to change salary
def emp_sal_change(salary_list, firstname_list, surname_list, email_list, employee_id_list):
    emp_id = input("Please enter the employee id: ")

    # Validation
    # Make sure there's something entered
    while True:
        if len(emp_id) == 0:
            emp_id = input("Please input a value: ")
        else:
            break

    # Make sure its a number
    while True:
        if emp_id.isalpha():
            emp_id = input("Please enter a number, try again: ")
        else:
            break

    # Make sure the employee ID exists
    while True:
        if int(emp_id) not in employee_id_list:
            emp_id = input("Not a valid id, try again: ")
        else:
            break

    increase_or_decrease = input("Would you like to 1.Increase salary or 2.Decrease salary? ")

    # Validation
    # Make sure its a number
    while True:
        if increase_or_decrease.isalpha():
            increase_or_decrease = input("Please enter a number, try again, 1 or 2: ")
        else:
            break

    while True:
        if int(increase_or_decrease) != 1 and int(increase_or_decrease) != 2:
            increase_or_decrease = input("Please enter 1 or 2")
        else:
            break

    emp_id = int(emp_id)

    # Increasing salary
    if increase_or_decrease == "1":
        sal_increase = input("How much would you like to add on to their salary?")

        # Validation
        while True:
            if sal_increase.isalpha():
                sal_increase = input("Please enter a number: ")
            else:
                break

        # Loop to increase salary
        for i in range(0, len(salary_list)):
            if emp_id == employee_id_list[i]:
                salary_sum = float(salary_list[i]) + float(sal_increase)
                salary_list[i] = salary_sum
                salary_change = ("The new salary is " + str(salary_sum))
                break

    # Decreasing salary
    elif increase_or_decrease == "2":
        sal_decrease = input("How much would you like to take away  from their salary? ")

        # Validation
        while True:
            if sal_decrease.isalpha():
                sal_decrease = input("Please enter a number: ")
            else:
                break

        # Loop to decrease salary
        for i in range(0, len(salary_list)):
            if emp_id == employee_id_list[i]:
                salary_sum = float(salary_list[i]) - float(sal_decrease)
                salary_list[i] = salary_sum
                salary_change = ("The new salary is " + str(salary_sum))
                break

    # Save data to file
    reWriteData(employee_id_list, firstname_list, surname_list, email_list, salary_list)

    return salary_change


# Rewriting the file so the deleted person, or added is saved.
def reWriteData(employee_id_list, firstname_list, surname_list, email_list, salary_list):
    
    # open the file and write to it
    filename = "project.txt"
    data_file = open(filename, "w")

    for i in range(0, len(employee_id_list)):
        row = str(employee_id_list[i]) + "," + firstname_list[i] + "," + surname_list[i] + "," + email_list[i] + "," + \
              str(salary_list[i]) + "\n"
        # write out the file
        data_file.write(row)

    # close the file
    data_file.close()


main()