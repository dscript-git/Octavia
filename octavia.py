#!/usr/bin/env python
"""Octavia 1.0 written in Python (Gattorete@Home)."""

# For more: http://www.gattorete.org
# Author: 0x8b30cc [Davide Pataracchia] (Gattorete@Home)
# Licensed under GNU GENERAL PUBLIC LICENSE (GPLv3)

import data.file_reader
import data.output_writer


# Terminal colors and options
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLO = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


# Shows a cool banner on startup
def banner():
	print("\033c" + HEADER)
	print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-\n"
	"   ____   _____ _______  __      _______                    \n"
	"  / __ \ / ____|__   __|/\ \    / /_   _|   /\              \n"
	" | |  | | |       | |  /  \ \  / /  | |    /  \             \n"
	" | |  | | |       | | / /\ \ \/ /   | |   / /\ \            \n"
	" | |__| | |____   | |/ ____ \  /   _| |_ / ____ \           \n"
	"  \____/ \_____|  |_/_/    \_\/   |_____/_/    \_\ v 1.0    \n"
	"                                                            \n"
	"          Author: 0x8b30cc (www.gattorete.org)              \n"
	"               Licensed under the GPLv3                     \n"
	"                                                            \n"
	"#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-\n")
	print(ENDC)


# Ask if the user wants to brute-force files
def file_bool_ask():
	valid = False
	while not valid:
		file_bool_input = input(YELLO + "Bruteforce files? [Y/N]: " + BOLD)
		print(ENDC)
		if (file_bool_input.upper() == "Y"):
			file_bool = True
			valid = True
		elif (file_bool_input.upper() == "N"):
			file_bool = False
			valid = True
		else:
			print(RED + "[ERROR] Please answer with Y (for yes) or N (for no).")
			print(ENDC)
			valid = False
	return file_bool


# Ask if the user wants to brute-force dirs
def dir_bool_ask():
	valid = False
	while not valid:
		dir_bool_input = input(YELLO + "Bruteforce dirs? [Y/N]: " + BOLD)
		print(ENDC)
		if (dir_bool_input.upper() == "Y"):
			dir_bool = True
			valid = True
		elif (dir_bool_input.upper() == "N"):
			dir_bool = False
			valid = True
		else:
			print(RED + "[ERROR] Please answer with Y (for yes) or N (for no).")
			print(ENDC)
			valid = False
	return dir_bool


def main():
	# Ask for the target url
	target = input(YELLO + "Target url: " + BOLD)
	print(ENDC)
	# Ask for the list file path
	dir_wordlist_path = input(YELLO + "Dirs/files list path: " + BOLD)
	print(ENDC)
	dir_bool = dir_bool_ask()
	file_bool = file_bool_ask()
	data.file_reader.read_from_list(
		dir_wordlist_path,
		target,
		dir_bool,
		file_bool
	)
	data.output_writer.ask()

banner()
main()
