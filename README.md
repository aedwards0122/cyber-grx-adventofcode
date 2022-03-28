# cyber-grx-adventofcode

**This is the code used for the Advent of Code 2021 # 10.  It parses a text file of brackets to identify corrupted and incomplete lines and can determine a score based on a scoring map and a hash map of opening and closing brackets.**

# How to Use 

**You will need to have venv running in the directory where this code will run**

https://docs.python.org/3/library/venv.html

*python3 -m venv env*
**This command will set up the virtual environment** 

*source env/bin/activate* 
**This command will active your virtual environment, and your command line will show your virtual environment is running**

**Once your virtual environment is running you can install the dependences by using**

*pip install -r requirements.txt*

**You can also pip install any package, and it will be bound to the virtual environment running, but the new packages will need to be frozen to the requirements.txt file**

**The program will need a source data file to parse.  For this example, the program is using the data provided by the Advent of Code problem.  The text file is called source.txt, and there is also a source_test.txt file that contains the data in the AoC example that is being used for the test cases**

**Once the text file is set up you can run**

*python3 run.py*
**Start parsing the configured text file**

*pytest*
**Runs all the tests that are in the test_sample.py file, and returns the testing results**



#Files

*main.py*
**This is the main file and class that does all the parsing.  The constructor of the class will look for the data file provided to it.  It will look in data directory for the file and parse the lines out into a list, and finally will call the “parse_data”.  In addition, the class has a “get_key_by_value” method which is used to find a key in the character key dict using the value.  Lastly the class has a “parse_data” method which does all processing, and calls into the “output_data_values” method to print all the data out.**

*run.py*
**This is used to invoke the main class “StringParse” and passes in the string value of the data file to be parsed.** 

*test_sample.py*
**This is used to hold all the tests we want to run on out main class.  The tests are run by calling “pytest” from the command line.**

#Directories

*Data*
**The data directory will hold the source data files to be used by the application.  There are currently two files.  More can added and used by the program.**
-	source.txt 
-	source_test.txt


 
