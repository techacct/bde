import os
import sys
import glob

import pydoop.hdfs as hdfs

# Copy files to HDFS from local filesystem
# Modify for your needs, includes some file and path existence checks

# Define file and local path
localPath="CSV-write/"
localCWD=os.path.dirname(os.path.abspath(__file__))
fullPath=localCWD+"/"+localPath
if not os.path.exists(fullPath):
	print("The file path does not exist:")
	print(fullPath)
	sys.exit(1)

# Define HDFS path an check
hdfsPath="/user/hands-on/CSV-write"
if not hdfs.path.isdir(hdfsPath):
	hdfs.mkdir(hdfsPath)
	# make sure the mkdir operation worked
	if  not hdfs.path.isdir(hdfsPath):
		print("Cannot create HDFS path")
		sys.exit(1)

# Use hdfs.put to move files into HDFS
print("\nThe local source file(s):")
for filename in glob.glob(os.path.join(fullPath, '*.csv')):
	print(filename)
	head, tail = os.path.split(filename)
	if hdfs.path.isfile(hdfsPath+"/"+tail):
		print("HDFS file exists:")
		print(hdfsPath+"/"+tail)
		sys.exit(1)
	else:
		hdfs.put(filename,hdfsPath)

# Print the result:
contents=hdfs.ls(hdfsPath)
print("\nContents of HDFS directory:")
print(contents)
