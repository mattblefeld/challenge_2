def process_file(file=None):
    """
    Purpose: The purpose of this function is to:
                1. accept a file with words
                2. read its contents
                3. identify the longest word in the file
                4. transpose the longest word
                5. print both the longest word and transposed word.
    :param file: Text file with extension .txt
    :return:    longest_word, transposed
    """

    # check if file param was not used and fail fast and gracefully
    if file is None:
        raise ValueError("You must supply a valid .txt file to the file parameter.")

    # open file and read each line as an item in a list
    with open(file) as sample_file:
        contents = sample_file.read().splitlines()

        # set the baseline for the largest word size and establish the longest_word variable
        largest_size = 0
        largest_word = None

        # loop through the list and get the length of each item
        # check the item length against the current largest and update the baseline variables if it is larger
        for item in contents:
            size = len(item)
            if size > largest_size:
                largest_size = size
                largest_word = item

        # transpose the largest word using slicing and the obtained word length and working backwards to zero
        transposed = largest_word[largest_size::-1]

        print("The largest word is: " + largest_word)
        print("The largest word transposed is: " + transposed)

    return largest_word, transposed


if __name__ == "__main__":
    # get the data directory, specific to environment
    import os
    data_dir = os.getcwd().replace("source", "data/")
    process_file(data_dir + "sample_file.txt")
