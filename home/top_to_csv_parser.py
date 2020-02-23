#!/usr/bin/python3

################################################
#                                              #
#   Project:  top Parser                       #
#   Version:  1.0.1                            #
#   Made By:  Volodymyr Zyhmund                #
#   Date:     2020.02.18                       #
#   E-mail:   volodymyr.romanovych@gmail.com   #
#                                              #
################################################


# Additional libraries
import os
import csv
import time
import subprocess

# Variables
save_to_file = "top_log.csv"   # Parse data to this file
snapshot_duration = 1          # E.g. Take data snapshot 'n' times every 1 second
max_iterations = 10            # Specify maximum iteration loops to be done, before the end   <-   To avoid an endless cycle

# If old file [ top_log.csv ] exist - remove it
os.system(f"[ -e {save_to_file} ] && rm {save_to_file}")

# Receive one snapshot of data from the top.
temp = subprocess.Popen(['top', '-b', '-n 1'], stdout = subprocess.PIPE)

# Get the output of top (raw data)
output = str(temp.communicate())
output = output.split("\n")
output = output[0].split('\\n')

# Variable to store the result
res = []
for line in output:
    res.append(line)

# Values list
values = res[6].split()

# Data to be added to a new column each time
raw_data = ' '.join(res[len(res) - 6:len(res) - 1])
data = raw_data.split()

# List of active processes
list_of_processes = data[11::12]
list_of_processes_len = len(list_of_processes)

# 1st column list
first_column = []
for item in list_of_processes:
    first_column += [item] + ['']*(len(res[6].split()) - 1)

# 2nd column list
second_column = values*list_of_processes_len

# Function to add first 2 columns to [ top_log.csv ] file
def add_first_2_columns_to_csv(output_file, list_to_column):
    """ Append a column in csv using csv.writer class"""
    # Open [ output_file ] in write mode
    with open(output_file, 'w', newline='') as write_obj:
        # Create a csv.writer object from the output file object
        csv_writer = csv.writer(write_obj)
        # Read each row of the input csv file as a list
        for row in list_to_column:
            # Convert tuple [ row ] to a list
            row = list(row)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


# Function to append new list of data as a new column to [ top_log.csv ] file
def append_column_to_csv(output_file, list_to_column):
    """ Append a column in existing csv using csv.reader and csv.writer classes"""
    # Open [ output_file ] in read mode
    with open(output_file, 'r') as read_obj:
        # Create a csv.reader object from the file object
        csv_reader = csv.reader(read_obj)
        # Read each row of existed csv file as a list to [ existed_list ] list
        existed_list = []
        for row in csv_reader:
            existed_list.append(row)

    # Open [ output_file ] in write mode
    with open(output_file, 'w', newline='') as write_obj:
        # Create a csv.writer object from the file object
        csv_writer = csv.writer(write_obj)
        # Read each row of csv file as a list
        cnt = 0

        # Uncomment 2 comments below to see the main output in terminal

        # print(f"\tMAIN OUTPUT:")
        for row in existed_list:
            row.append(list_to_column[cnt])
            # print(f"{row}")
            cnt += 1
            csv_writer.writerow(row)


# Debug mode function (if required)
def debug_mode():
    """ Debug mode function"""
    # Values list
    print(f"\n\tVALUES:\n{values}\n")

    # Number of columns in top (by default is 12)
    print(f"\tNUMBER OF COLUMNS in top:\n{len(res[6].split())}\n")

    # Data to be added to a new column each time
    print(f"\tDATA:\n{data}\n")

    # List of active processes
    print(f"\tPROCESSES ({list_of_processes_len}):\n{list_of_processes}\n")

    # 1st column list
    print(f"\tFIRST COLUMN:\n{first_column}\n")

    # 2nd column list
    print(f"\tSECOND COLUMN:\n{second_column}\n")


if __name__ == "__main__":

    # Debug mode function (uncomment if required)
    # debug_mode()

    # Add first 2 columns to [ top_log.csv ] file
    add_first_2_columns_to_csv(save_to_file, zip(first_column, second_column))

    # Add new data column to [ top_log.csv ] file every 'n' seconds and
    # User friendly output in terminal
    iter_symbol = ''
    print()
    while True:
        if len(iter_symbol) < max_iterations:
            iter_symbol += '.'
            iter_result = f"  Passed [ {len(iter_symbol)} of {max_iterations} ] iterations, every [ {snapshot_duration} ] seconds {iter_symbol}"
            append_column_to_csv(save_to_file, data)
            print(f"\r{iter_result}", end = "")
            time.sleep(snapshot_duration)
        else:
            print(f"{iter_result}\n")
            exit()
