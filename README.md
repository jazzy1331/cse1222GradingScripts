# Multiple File Compilation Checker

A script that uses the g++ compiler to compile all files in a directory and prints out live results.

## How to use

Using bash, type ````./checkFileCompiles PATH/TO/DIR/CONTAINING/SUBMISSIONS/DIR```` when bash is currently in the same directory as the file. This will run the script with the given parameter.

## Understanding the Output

Every file processed is separated by a horizonatal line. Every file that compiles successfully will have no extra output messages. Files that return output when compiled using g++ will display it below the "processing" line and above the the horizontal line divider.

## Use Case

### Primary
* To check compilation of _.cpp_ files submitted by students to OSU's Carmen system that are compiled using a g++ compiler.

### Alternate

* By editing the value of the ````FILES```` variable, this script can be used with any directory.
* By editing the ````g++```` command, this script can be used with any command.
