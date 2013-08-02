import os,struct
from globals import *
from array import array

class Patchreader(object):
	def __init__(self,path):
		self.mem_mods = {}
		self.loadPatches(path)
		if(DEBUG):
			print("DEBUG: Patches Read")
	
	def readPatches(self,path):
		patchfile = open(path,"r")
		lines = patchfile.readlines()
		patchfile.close()
		return lines
	
	def loadPatches(self,path):
		lines = self.readPatches(path)
		patches = {}
		dip_parsing = True
		for line in lines:
			line = line.strip()
			if(line != ""):
				if(line[0] != "#"):
					ele = line.split(' | ')
					patches[ele[0]] = ele[1:]
		self.procPatches(patches)

		
	def procPatches(self,patches):
		for ele in patches:
			mod_name = ele
			operation = patches[ele][0]
			addr = int(patches[ele][1],16)
			arg = patches[ele][2]
			
			#Strip quotes out of string args
			arg = arg.replace("'","")
			
			if(operation == 'NOP'):
				self.mem_mods[addr] = [mod_name,bytearray(b'\x90' * int(arg,16))]
			
			if(operation == 'NULL'):
				self.mem_mods[addr] = [mod_name,bytearray(b'\x00' * int(arg,16))]
				
			if(operation == 'WR'):
				if(arg[:2] == "0x"):
					self.mem_mods[addr] = [mod_name,struct.pack("<I",int(arg,16))]
					continue
				else:
					arg = arg.replace("\\x","")

					self.mem_mods[addr] = [mod_name,array('B',arg.decode("hex"))]
			if(operation == 'STR'):
				arg += '\x00'
				self.mem_mods[addr] = [mod_name,bytearray(arg)]
#Testing Code
if __name__ == '__main__':
	patches = Patchreader('piu.msa')