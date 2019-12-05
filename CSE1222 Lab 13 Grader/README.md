# Multiple File Compilation Checker

A script that uses the g++ compiler to compile a students program file, with an input file, and displays contents of output file

## How to use

Using bash, type ````./gradeFile PATH/TO/DIR/CONTAINING/SUBMISSION```` when bash is currently in the same directory as the file. This will run the script with the given parameter.
Example: ````./gradeFile myFile.cpp```` or ````./gradeFile myFolder/myFile.cpp````

## Understanding the Output

The script prints a message stating the file being processed, prints a horizontal line, and then the contents of the output file "outfile" (output file name given to program through input during execution).

## Requirements

* Must have g++ compiler.
* File called "input" that has the exact input necessary for full execution of student's program.
* Program must know that output file is called "outfile".

## Use Case

### Primary
* To check the compilation of lab 13 _.cpp_ file submitted by students to OSU's Carmen system that are compiled using a g++ compiler.

### Alternate

* By editing the value of the input file from _input_, this script can be used with any input file.
* By editing the ````g++```` command, this script can be used with any command.
