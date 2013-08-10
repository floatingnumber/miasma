#!/usr/bin/env python
'''
Miasma binary modification program.
First revision created by Mario Mercaldi
Licensing - Do whatever you want with it.
'''
import os,sys
from miasma.target import Target
from miasma.globals import *

def main(largs):
	#Argument Handling
	if(len(largs) not in range(2,3)):
		print("Usage - miasma.py targetbinary ['args']")
		exit(1)
	
	#Ensure binary target file exists.
	if(not os.path.exists(largs[1])):
		print("Error - Target binary doesn't exist")
		exit(1)
	(base,bin) = os.path.split(largs[1])
	
	#Ensure binary patch file exists - create otherwise.
	if(not os.path.exists('%s.msa' % largs[1])):
		f = open('%s.msa' % largs[1], "w+")
		f.close()
		
	print("Miasma Engine Started")
	
	#Init binary target with or without args.
	if(len(largs) < 3):
		binary = Target(largs[1],None)
	else:
		binary = Target(largs[1],largs[2])
	
	#Execute the fork and start the process.
	binary.run()
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
