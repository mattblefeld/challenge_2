# Introduction

### The Coding Challenge:

1. Read input from a file of words;
2. Find the largest word in the file
3. Transpose the letters in the largest word
4. Show the largest word and the largest word transposed
5. Demonstrate positive and negative test cases
6. Ensure you document code and instructions for building and running based on the response best practices above

### Example file contents

a

ab

abc

abcd

abcde


# Development approach
 - I set the file parameter value to NONE (null) so that if a file was not passed in to the function, 
   I could catch it and fail fast with a verbose message to the user.
 - Then, I read the file and convert each line into an item in a list. 
 - Next I iterate over the list, counting the length of each word. 
   I compare it to the previous largest length word and, if it is larger, then it becomes the longest word.
 - Once I have iterated over all items in the list and identified the longest word, I then transpose the word using slicing, by starting at 
   the end of the word and working backwards to 0.

Resulting output from running the file_processor.py script:  
The largest word is: abcde  
The largest word transposed is: edcba

# Test Development Approach

My solution is in python, and I use pytest as the test runner.

I prefer this approach as pytest offers some advanced features that can allow:
 - tests to be categorized and grouped into suites by specified text (specified in the pytest.ini file) or by keywords
 - tests to be parameterized, thereby reducing actual test code and limiting changes to only those variables
   fed into the test structure. This feature can also be used for data driven testing.
 - customized test fixtures to be used in tests, such as query results for use in the tests, db updates upon test teardown, common webdriver harness for all tests, and more.

Pytest performs test collection in the /tests directory by scanning all files in the directory, and identifying those with
method names that begin with test_ and class names that begin with Test. If a mark is used when running pytest,
then pytest will collect all the available tests in the /tests directory, and then deselect those that don't
match the mark specified in the mark flag. Pytest will then run the remaining tests and provide a pass/fail output.
Pytest marks can be used as suite identifiers, and multiple marks can be applied to a single test method or entire test class, providing even more ability to build test suites.
This feature comes in especially handy when integrating with Jenkins, or other CI/CD systems, as it makes building scheduled/triggered test suite runs very easy and straight forward.

# Test Approach

I've provided automated test coverage of the cases, below. I've also provided the test case steps as docstrings within the actual tests themselves.

### Positive Tests
   1) Test that the input file is not corrupt (i.e. it can be opened).
   2) Test that the input file contains content.
   3) Test that the largest word was identified and matched what was expected.  
      (I provided two files for this test, and used pytests parameterization fixture to run this test twice, once for each file.)
   4) Test that the largest word was transposed correctly and matched what was expected.  
      (Again, I provided two files for this test, and used pytests parameterization fixture to run this test twice, once for each file.)
### Negative Tests
   5) Test that the process_file() method fails without a valid file being passed to it.
   6) Test that the process_file() method fails when an empty file is passed to it.

### Suite creation
I applied pytest marks to these tests so that I could demonstrate the ability to pickup only specific test suites in test collection. 
I used the following marks: 'regression' and 'negative'. See below to run these suites.
    
# Assumptions
 - you have a working python3 environment, with pip installed, and access to the python3 interpreter in your PATH or virtual environment

# Run the Tests from the Terminal

### Before running any tests, please install pytest
From your terminal:

`pip install pytest`

### Run all the tests
This will run all 8 tests available. From your terminal:

`cd tests`

`python -m pytest -v`

### Run the 'regression' test suite only
This will run all 6 tests available. From your terminal:

`cd tests`

`python -m pytest -m "regression" -v`

### Run the 'negative' test suite only
This will run all 2 tests available. From your terminal:

`cd tests`

`python -m pytest -m "negative" -v`

### Run script to process the text file and output the results.
This will run the file processor method on the sample_text.txt file and output the longest word, and it transposed. From your terminal:

`cd source`

`file_processor.py`


## What happens when I run the tests?
Pytest will collect the appropriate tests, run them, and then provide the result in the terminal.

With the use of a few more pytest flags and plugins, we can quickly provide junit output and html reporting.