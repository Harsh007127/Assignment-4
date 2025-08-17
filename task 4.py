# Assignment 4.  
# Task 1: Read a File and Handle Errors

# Module 5: Files, Exceptions, and Errors in Python

def read_file(filename="sample.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print("Reading file content:")
            for i, line in enumerate(f, start=1):
                print(f"Line {i}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: the file '{filename}' was not found.")
    except OSError as e:
        # Any other file-related issue (permissions, encoding, etc.)
        print(f"Error: could not read '{filename}': {e}")

if _name_ == "_main_":
    read_file()

# task2_write_append.py
  Task 2: Write and Append Data to a File

def main():
    filename = "output.txt"

    try:
        # 1) Take user input and WRITE to file
        first_text = input("Enter text to write to the file: ").strip()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(first_text + "\n")
        print(f"Data successfully written to {filename}.")

        # 2) Take more input and APPEND to same file
        more_text = input("Enter additional text to append: ").strip()
        with open(filename, "a", encoding="utf-8") as f:
            f.write(more_text + "\n")
        print("Data successfully appended.")

        # 3) Read & display final content
        print("\nFinal content of output.txt:\n")
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())

    except (OSError, IOError) as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if _name_ == "_main_":
    main()
