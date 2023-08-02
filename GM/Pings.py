'''
    CIS188 Sample Program
    CSV reading and IP address pinging
    
    This program is a companion sample for Lab 11
    Chapter 18 Automate the Boring Stuff with Python
    
    You can use this program as a template to start

    Include ip.csv in the same directory as this .py file

    You must first pip install ping3 and ezgmail modules
    
    Author: Professor McInstructor

'''

import csv
from ping3 import ping
import ezgmail
import os

ezgmail.init(tokenFile='token.json', credentialsFile='credentials.json')

def add_new_column():
    ip_results = []
    with open('ip.csv', 'r', newline='') as input_csv, open('ipUpdate.csv', 'w', newline='') as output_csv:
        reader = csv.DictReader(input_csv)  # Change csv.reader to csv.DictReader
        writer = csv.writer(output_csv)
        # Read the header row and add the new column header
        headers = reader.fieldnames  # Use reader.fieldnames to access header row
        headers.append('Ping Time')
        writer.writerow(headers)
        # Read the rest of the rows and add the new column data
        for row in reader:
            ip = row['ip']  # Access 'ip' value from the row dictionary
            ping_time = ping(ip)
            row['Ping Time'] = f'{ping_time:.2f}' if ping_time is not None else 'N/A'
            writer.writerow([row[column] for column in headers])  # Use a list comprehension to write the row
            ip_results.append(f'IP: {ip}, Ping Time: {ping_time:.2f}' if ping_time is not None else f'IP: {ip}, Ping Time: N/A')
    return '\n'.join(ip_results)


# How can we send an email with a message we've built?
try:
    message = add_new_column()
    ezgmail.send('email@mail.email.edu', 'List of IPs and Ping Time', f'List of IPs and ping time stored in a CSV file:\n\n{message}', ['ipUpdate.csv'])
except Exception as e:
    print(f"An error occurred: {e}")
