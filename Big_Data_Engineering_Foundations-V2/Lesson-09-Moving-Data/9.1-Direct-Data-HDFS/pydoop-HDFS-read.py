import os
import sys
import glob
import pydoop.hdfs as hdfs

# Copy files from HDFS to local filesystem
# Modify for your needs, includes some file and path existence checks

# Use local directory, check if it exits
localPath="CSV-read/"
localCWD=os.path.dirname(os.path.abspath(__file__))
fullPath=localCWD+"/"+localPath
if not os.path.exists(fullPath):
        print("The file path does not exist:")
        print(fullPath)
        sys.exit(1)

hdfsPath="/user/hands-on/CSV-read"
if not hdfs.path.isdir(hdfsPath):
	print("HDFS Path does not exist:")
	print(hdfsPath)
	sys.exit(1)
HDFSfiles = hdfs.ls(hdfsPath);
print("\nReading HDFS file(s):")
for file in HDFSfiles:
	# check if file aleady exists
	head, tail = os.path.split(file)
	if os.path.exists(fullPath+tail):
		print("File exists:")
		print(fullPath+tail)
		sys.exit(1)
	else:
		# use hdfs.get to pull file from HDFS
		print(file)
		hdfs.get(file,fullPath)
print("\nContents of local directory:")
for filename in glob.glob(os.path.join(fullPath, '*.csv')):
        print(filename)

