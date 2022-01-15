"""Octavia 1.0 written in Python (Gattorete@Home)."""
# For more: http://www.gattorete.org
# Author: 0x8b30cc [Davide Pataracchia] (Gattorete@Home)
# Licensed under GNU GENERAL PUBLIC LICENSE (GPLv3)

import sys

# Terminal colors and options
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLO = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

output_list = []


# Append an element to output_list
def append_to_list(element):
	output_list.append(element)


# Print output_list
def dump_list():
	print(YELLO + "[INFO] Dumping the output list..." + ENDC)
	print
	for element in output_list:
		print(element)


# Write output_list to a file
def write_to_file():
	file_path = input(YELLO + "Output file path: " + ENDC)
	print
	print(YELLO + "[INFO] Writing to the output file..." + ENDC)
	f = open(file_path, "w")
	# Write the list to an external file
	f.write("\n".join(output_list))


# Ask the user what he wants to do with the output list
def ask():
	print(HEADER + "**************************DONE***********************" + ENDC)
	print
	print(BOLD + GREEN + "[1] " + YELLO + "Dump the output list" + ENDC)
	print(BOLD + GREEN + "[2] " + YELLO +
		"Write the output list in a file" + ENDC)
	print(BOLD + GREEN + "[3] " + YELLO + "Quit" + ENDC)
	print
	print(HEADER + "*****************************************************" + ENDC)
	valid = False
	while not valid:
		choice = input(BOLD + GREEN + "0ctavia-$: " + ENDC)
		if (choice == '1'):
			dump_list()
			valid = True
		elif (choice == '2'):
			write_to_file()
			valid = True
		elif (choice == '3'):
			valid = True
			sys.exit(0)
		else:
			print(RED + "[ERROR] Invalid value..." + ENDC)
			valid = False
