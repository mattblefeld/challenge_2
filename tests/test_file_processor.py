import pytest
import os
from source.file_processor import process_file

# get the data directory, specific to environment, to use in all the tests
data_dir = os.getcwd().replace("tests", "data/")


@pytest.mark.regression
def test_input_file_is_not_corrupt():
    """
    Purpose: To test that the input file opens and does not throw an exception.
    Test Steps:
        1) Try to open valid file
        2) Confirm file is open
    """
    try:
        file = open(data_dir + "sample_file.txt", 'r')
        assert (file.closed is False) is True
    except:
        pytest.fail(msg="Input file was unable to be opened")


@pytest.mark.regression
def test_input_file_is_populated():
    """
    Purpose: To test that the input file is not empty.
    Test Steps:
        1) Open valid file and read content
        2) Confirm content is not empty
    """
    result = process_file(data_dir + "sample_file.txt")
    assert (result is not '') is True


@pytest.mark.regression
@pytest.mark.parametrize("input_file", ["sample_file.txt", "random_sample_file.txt"])
def test_largest_word_was_identified(input_file):
    """
    Purpose: To test that the process_file() method correctly identifies the largest word in a text file of words. This test will run once for each parameter provided in the parameterize fixture, above.
    Test Steps:
        1) Run the process_file method on the input file
        2) Confirm that the result from process_file() matches the expected result.
    """
    # set the expected result based upon which file is being run in the test
    if "random" not in input_file:
        expected_result = "abcde"
    else:
        expected_result = "challenge"

    actual_result = process_file(data_dir + input_file)
    assert (actual_result[0] == expected_result) is True


@pytest.mark.regression
@pytest.mark.parametrize("input_file", ["sample_file.txt", "random_sample_file.txt"])
def test_largest_word_was_transposed(input_file):
    """
    Purpose: To test that the process_file() method correctly transposes the largest word in a text file of words. This test will run once for each parameter provided in the parameterize fixture, above.
    Test Steps:
        1) Run the process_file method on the input file
        2) Confirm that the result from process_file() matches the expected result.
    """

    # set the expected result based upon which file is being run in the test
    if "random" not in input_file:
        expected_result = "edcba"
    else:
        expected_result = "egnellahc"

    actual_result = process_file(data_dir + input_file)
    assert (actual_result[1] == expected_result) is True


@pytest.mark.negative
def test_file_processor_fails_with_incorrect_file_name():
    """
    Purpose: To test that the process_file() method correctly fails when an incorrect filename is passed to the method.
    Test Steps:
        1) Run the process_file method and pass in an incorrect filename
        2) Confirm that the process_file method throws an exception.
    """
    try:
        process_file(".txt")
        assert False
    except:
        assert True


@pytest.mark.negative
def test_file_processor_fails_with_empty_input_file():
    """
    Purpose: To test that the process_file() method correctly fails when a valid, but empty, file is passed to the method.
    Test Steps:
        1) Run the process_file method and pass in the valid, but empty, file
        2) Confirm that the process_file method throws an exception.
    """
    try:
        process_file(data_dir + "empty_file.txt")
        assert False
    except:
        assert True
