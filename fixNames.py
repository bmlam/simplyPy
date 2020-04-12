#!/usr/bin/python

""" 
Renames the filenames within the same directory to be Unix friendly
1. Change " - " to "-"
2. Change single spaces to single underbars

"""

def parseCmdLine() :
	import argparse 

	parser = argparse.ArgumentParser()
	parser.add_argument( '-p', '--dirPath', help='which directory the action should apply on (currently non-recursive'
		, required= False, default='./')
	result= parser.parse_args()

	return result

def main():
	import os

	argConfig = parseCmdLine()

	orgDirPath =   argConfig.dirPath
	filenames = os.listdir(orgDirPath)

	for filename in filenames:
		orgFilePath = os.path.join( orgDirPath, filename )
		baseName = os.path.basename( filename )
		newBaseName = baseName.replace( " - ", "-" ) # condense 3 separators to 1
		newBaseName = newBaseName.replace( " ", "_" )
		newFilePath =  os.path.join(orgDirPath, newBaseName )
		# raise ValueError( newFilePath )
		os.rename(orgFilePath, newFilePath )

if __name__ == "__main__":
	main()

