def read_file_line_by_line(filename):

    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # Remove extra whitespace and print
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_file_line_by_line("something.py")

