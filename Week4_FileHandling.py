def file_read_write():
    # Step 1: Ask user for filename
    filename = input("Enter the filename to read: ")

    try:
        # Step 2: Try to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Step 3: Modify the content (example: uppercase everything)
        modified_content = content.upper()

        # Step 4: Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File has been modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
file_read_write()
