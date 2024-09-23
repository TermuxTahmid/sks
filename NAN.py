import os
import random
import requests

# Function to create a random clone
def random_clone():
    print("Starting Random Clone...")
    user_ids = []
    for _ in range(10):  # Generates 10 random numbers (user IDs)
        user_id = random.randint(1000000000, 9999999999)
        user_ids.append(str(user_id))
    
    print("Generated User IDs:")
    print(user_ids)

# Function to clone content from one file to another
def file_clone(source_file, destination_file):
    if os.path.exists(source_file):
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Cloned content from {source_file} to {destination_file}")
    else:
        print(f"Source file '{source_file}' not found!")

# Function to create a new file
def create_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' created with content.")

# Main menu for the script
def main():
    while True:
        print("\nChoose an option:")
        print("1. Random Clone")
        print("2. File Clone")
        print("3. Create File")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            random_clone()
        elif choice == "2":
            source_file = input("Enter the source file name: ")
            destination_file = input("Enter the destination file name: ")
            file_clone(source_file, destination_file)
        elif choice == "3":
            file_name = input("Enter the file name to create: ")
            content = input("Enter content for the file: ")
            create_file(file_name, content)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()