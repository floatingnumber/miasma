'''
Miasma binary modification program.
First revision created by Mario Mercaldi
Licensing - Do whatever you want with it.
'''
import os,sys
from target import *
from globals import *

if __name__ == '__main__':
	
	#Argument Handling
	if(len(sys.argv) != 2 and len(sys.argv) != 3):
		print("Usage - miasma.py targetbinary ['args']")
		exit(1)
	
	#Ensure binary target file exists.
	if(not os.path.exists(sys.argv[1])):
		print("Error - Target binary doesn't exist")
		exit(1)
	(base,bin) = os.path.split(sys.argv[1])
	
	#Ensure binary patch file exists - create otherwise.
	if(not os.path.exists('%s.msa' % sys.argv[1])):
		f = open('%s.msa' % sys.argv[1], "w+")
		f.close()
		
	print("Miasma Engine Started")
	
	#Init binary target with or without args.
	if(len(sys.argv) < 3):
		binary = Target(sys.argv[1],None)
	else:
		binary = Target(sys.argv[1],sys.argv[2])
	
	#Execute the fork and start the process.
	binary.run()
	exit(0)