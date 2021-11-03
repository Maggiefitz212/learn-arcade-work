def main():
    my_file = open("super_villains.txt")
    villain_list = []
    for line in my_file:
        line = line.strip()
        villain_list.append(line)

    my_file.close()

    print(villain_list)
    print("There were ", len(villain_list), "names in the file.")

    # Linear search
    key = "Octavia the Siren"
    current_position = 0
    while current_position != len(villain_list) and villain_list[current_position] != key:
        current_position += 1

    if current_position == len(villain_list):
        print("Item not found.")


main()
