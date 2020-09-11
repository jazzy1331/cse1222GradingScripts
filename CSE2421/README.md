# Lab 1 Quick Grade Tool

A script that calls make, displays readme, and waits for keypress to go next in all submission folders

## How to use

### To unzip, call make, and display readme's
Using bash, type ````./makeFiles```` when bash is currently in the same directory as all of the students zipped submissions (achieved by unzipping submissions.zip from Carmen). Then, press any key to move on to the next student/directory when prompted.

### To call make and display readme's
Using bash, type ````./makeFiles```` when bash is currently in the same directory as all of the students unzipped submissions.  Then, press any key to move on to the next student/directory when prompted.

## Understanding the Output

Every student's directory will show:
```
PATH/BEING/ASSESSED
OUTPUT FROM MAKE
LAB1README
```

## Requirements
* Need both files to be in the same directory as the other directories (zipped or unzipped depending on usage)

## Troubleshooting
If error occurs, type ````ls -al```` and make sure that the script file has executable(````x````) permissions. If it doesn't enter ````chmod +x checkFileCompiles````
