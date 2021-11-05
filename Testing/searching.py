# Open the file for reading, and store a pointer to it in the new
# variable "file"
my_file = open("super_villains.txt")

name_list = []
# Loop through each line in the file like a list
for line in my_file:
    # Remove any line feed, carriage returns or spaces at the end of the line
    line = line.strip()
    name_list.append(line)

my_file.close()
key = "Morgiana the Shrew"
lower_bound = 0
upper_bound = len(name_list) - 1
found = False

# Loop until we find the item, or our upper/lower bounds meet
while lower_bound <= upper_bound and not found:

    # Find the middle position
    middle_pos = round((lower_bound + upper_bound) // 2)

    # Figure out if we:
    # move up the lower bound, or
    # move down the upper bound, or
    # we found what we are looking for
    if name_list[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif name_list[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print("The name is at position", middle_pos)
else:
    print("The name was not in the list.")

