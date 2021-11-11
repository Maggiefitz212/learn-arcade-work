import re


# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    dictionary_file = open("dictionary.txt")

    # Create an empty list to store our names
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in dictionary_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        dictionary_list.append(line)

    dictionary_file.close()

    print("--- Linear Search ---")

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    story_file = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in story_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            current_list_position = 0
            while current_list_position < len(dictionary_list) and \
                    word.upper() != dictionary_list[current_list_position]:
                current_list_position += 1

            if current_list_position >= len(dictionary_list):
                print("Line", line_number, "possible misspelled word:", word)

    story_file.close()

    print("--- Binary Search ---")

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    story_file = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in story_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        # line = line.strip()
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            # Loop until we find the item, or our upper/lower bounds meet
            while lower_bound <= upper_bound and not found:

                # Find the middle position
                middle_pos = (lower_bound + upper_bound) // 2

                # Either move to upper bound, lower bound, or found = False
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print(line_number, "possible misspelled word:", word)

    story_file.close()


main()
