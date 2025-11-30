filename = input("Enter file name: ")

while True:
    print("\n1. Read file")
    print("2. Write to file")
    print("3. Append to file")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        f = open(filename, "r")
        print("\nFile Content:\n", f.read())
        f.close()

    elif choice == "2":
        text = input("Enter text to write: ")
        f = open(filename, "w")
        f.write(text)
        f.close()
        print("Written successfully!")

    elif choice == "3":
        text = input("Enter text to append: ")
        f = open(filename, "a")
        f.write("\n" + text)
        f.close()
        print("Appended successfully!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
