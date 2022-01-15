"""Octavia 1.0 written in Python (Gattorete@Home)."""
# For more: http://www.gattorete.org
# Author: 0x8b30cc [Davide Pataracchia] (Gattorete@Home)
# Licensed under GNU GENERAL PUBLIC LICENSE (GPLv3)

# from urllib.request import urlopen, HTTPError
import requests
import data.output_writer

# Terminal colors and options
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

ext = [".bak", ".txt", ".zip", ".log", ".csv", ".dat", ".xml",
".db", ".sql", ".cfg", ".tmp", ".old", ".copy"]

s = requests.Session()


# Check the url http response
def http_response(url):
	try:
		print("DEBUG: " + url)
		r = s.get(url, timeout=5)
		# connection = urlopen(url)
		return r.status_code
	except requests.HTTPError:
		print('uh oh')


# Test the webserver for dirs
def test_dirs(lines, target):
	data.output_writer.append_to_list("++++++DIRECTORIES++++++")
	for line in lines:
		line = line.replace("\n", "")
		response = http_response(target + "/" + line)
		if (response == 200):
			print(GREEN + BOLD + "[SUCCESS] Found: " + target + "/" + line + ENDC)
			data.output_writer.append_to_list(target + "/" + line)
		elif (response == 403):
			print(GREEN + BOLD + "[SUCCESS]" + YELLOW +
				" 403 Forbidden: " + target + "/" + line + ENDC)
			data.output_writer.append_to_list("FORBIDDEN: " + target + "/" + line)
		elif (response == 301):
			print(GREEN + BOLD + "[SUCCESS]" + YELLOW + " 301: " +
				target + "/" + line + ENDC)
			data.output_writer.append_to_list(target + "/" + line)


# Test the webserver for files
def test_files(lines, target):
	data.output_writer.append_to_list("++++++FILES++++++")
	for line in lines:
		for a in ext:
			line = line.replace("\n", "")
			response = http_response(target + "/" + line + a)
			if (response == 200):
				print(GREEN + BOLD + "[SUCCESS] Found: " + target + "/" + line + a + ENDC)
				data.output_writer.append_to_list(target + "/" + line + a)
			elif (response == 403):
				print(GREEN + BOLD + "[SUCCESS]" + YELLOW + " 403 Forbidden: " +
					target + "/" + line + a + ENDC)
				data.output_writer.append_to_list("FORBIDDEN: " + target + "/" + line + a)
			elif (response == 301):
				print(GREEN + BOLD + "[SUCCESS]" + YELLOW + " 301: " + target +
					"/" + line + a + ENDC)
				data.output_writer.append_to_list(target + "/" + line + a)
