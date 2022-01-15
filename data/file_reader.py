"""Octavia 1.0 written in Python (Gattorete@Home)."""
# For more: http://www.gattorete.org
# Author: 0x8b30cc [Davide Pataracchia] (Gattorete@Home)
# Licensed under GNU GENERAL PUBLIC LICENSE (GPLv3)

import sys
import data.http_test

# Terminal colors and options
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


# Open the input file and read each line for testing
def read_from_list(file_path, target, dir_bool, file_bool):
	print
	print(BOLD + HEADER + "Let the hunt begin!" + ENDC)
	print
	print
	try:
		with open(file_path) as f:
			content = f.readlines()
	except:
		print(RED + "[ERROR] No such file in: " + file_path + ENDC)
		sys.exit(0)
	if dir_bool:
		print(YELLOW + "[INFO] Testing for dirs, please wait..." + ENDC)
		print
		try:
			# Test for directories
			data.http_test.test_dirs(content, target)
			print
		except KeyboardInterrupt:
			print
			print(RED + "[INFO] Skipping the directories test..." + ENDC)
			print
	if file_bool:
		print(YELLOW + "[INFO] Testing for files, please wait..." + ENDC)
		print
		try:
			# Test for files
			data.http_test.test_files(content, target)
		except KeyboardInterrupt:
			print
			print(RED + "[INFO] Skipping the files test..." + ENDC)
			print
	if not dir_bool and not file_bool:
		print(RED + "[ERROR] Nothing to do here... Are you drunk mate?" + ENDC)
		print
		sys.exit(0)
