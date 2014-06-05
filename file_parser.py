"""
The file_parser program is designed to parse device measurement data and to separate each location data to new .txt file.
Please refer to the README file to learn the usage of the program.
Author: Cem Koc

"""

import inspect
import sys

def main(fn):
    """Call fn with command line arguments.  Used as a decorator.

    The main decorator marks the function that starts a program. For example,

    @main
    def my_run_function():
        # function body

    Use this instead of the typical __name__ == "__main__" predicate.
    """
    if inspect.stack()[1][0].f_locals['__name__'] == '__main__':
        args = sys.argv[1:] # Discard the script name from command line
        fn(*args) # Call the main function
    return fn

def parse_file(name):
	""" parse_file takes in the input file and writes new files for each device """

	readfile = open(name[0], 'r')
	header = readfile.readline()
	has_opened = False
	try:
		for line in readfile:
			line_iter = iter(line)
			if next(line_iter) == '*':
				if has_opened == False:
					writefile = open(line.strip('*') + '.txt', 'a')
					has_opened = True
				else:
					writefile.close()
					writefile = open(line.strip('*') + '.txt', 'a')

				writefile.write(header)
			if has_opened:
				writefile.write(line.strip('*'))
	finally:
		writefile.close()
		readfile.close()

@main
def run(*args):
	print("The Program has begun")
	print("Creating files")
	parse_file(args)
