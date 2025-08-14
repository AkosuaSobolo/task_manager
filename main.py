# Use loop to calculate the sum of the numbers below
# numbers = [10, 5, 20, 8, 15]
# sum = 0
# for number in numbers:
    # sum = sum + number
    # print(f"Your total is {sum}")

# Open the file emails.txt in READ mode
# Read and split the data using \n to get a list
# Loop over the list of emails and print a generated username for each of them ie. username is all
#  characters before the @
# file = open("emails.txt", "r")
# emails = file.read(). split("\n")
# index = 0
# for email in emails:
    # username = email.split("@")[index:][0]
    # print(username)

# Define a resgister user function
# def register_user(name, email, password):
    # Check if user does not already exist
    # Has user password
    # Validate inputs
    # Check if user is not a robot
    # Return response
    # return "user registered successfully"
# calling the registered user function
# response = register_user("Akosua Sobolo", "akosuaworde11@gmail.com", "244466666")

# Define a function, add task

import add
import show
import update
import delete


add_task_response = add.add_task("sleep")
print(add_task_response)

show_task_response = show.show_tasks
print(show_task_response)

update_task_response = update.update_tasks
print(update_task_response)

delete_task_response = delete.delete_task("wake up")
print(delete_task_response)




