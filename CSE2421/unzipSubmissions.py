#Author: Thomas Sullivan
#unzips .zip files in current directory and puts content in a file named after the student and late status.
#places processed files in a folder named "unzipped"
#Expected file format: studentname_<late>_####_####.zip 
#<late> is optional and ### are numbers

#usage: python unzipSubmissions.py &
import os

names = os.listdir(".")
if (not os.path.isdir("unzipped")):
  os.mkdir("unzipped")

for fileName in names:
  if (os.path.isfile(fileName) and fileName.endswith(".zip")):
    splitName = fileName.split("_")
    directoryName = splitName[0]
    if (splitName[1] == "late"):
      directoryName = splitName[0] + "_" + splitName[1]
    print("Unzipping " + fileName + " into " + directoryName)
    os.system("unzip " + fileName + " -d " + directoryName)
    os.system("mv " + fileName + " unzipped")
