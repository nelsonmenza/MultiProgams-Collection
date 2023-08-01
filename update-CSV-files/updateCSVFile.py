import csv
import random
import string


def generate_password(length):

    # Generate a random password with the specified length.

    all_characters = string.ascii_letters + \
        string.digits + '!@$%^&*-_+=~<>/\(){}[]?|'
    password = "".join(random.sample(all_characters, length))
    return password


def add_new_column():

    # Add a new column 'Password' to the 'employees.csv' file and populate it with the specified data.

    with open('Lab10/employees.csv', 'r', newline='') as input_csv, open('Lab10/employeesUpdate.csv', 'w', newline='') as output_csv:
        reader = csv.reader(input_csv)
        writer = csv.writer(output_csv)
        # Read the header row and add the new column header
        headers = next(reader)
        headers.append('password')
        writer.writerow(headers)
        # Read the rest of the rows and add the new column data
        for row in reader:
            row.append(generate_password(PASS_LENGTH))
            writer.writerow(row)


PASS_LENGTH = 16
add_new_column()
