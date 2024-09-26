def chatbot():
    # Welcome message

    print("Hello and Welcome to the Code2College Program! ")
    print(" ")
    print("I'm here to assist you with everything you need.\n")

    # Collect user's name
    name = input("May I know your name, please? ")

    # Thank user and ask for age
    print(f"\nThank you, {name}!")
    age = input("How old are you? ")

    # Ask how to help
    print(f"\nGreat! How can I assist you today, {name}?")

    # Provide menu of options
    print("\nPlease choose one of the options below to continue:")
    print("1. Learn more about Code2College")
    print("2. Talk to a Code2College representative")
    print("3. Access the Code2College application form")
    print("4. Code2College Frequently Asked Questions (FAQs)")
    print("5. Exit")

    # User selects an option
    option = input("\nEnter the number of your choice: ")

    # Respond based on user's choice
    if option == "1":
        print("\nCode2College is a program designed to empower underrepresented students through education in STEM and leadership.")
    elif option == "2":
        print("\nConnecting you to a Code2College representative...")
    elif option == "3":
        print("\nYou can access the Code2College application form through our official channels.")
    elif option == "4":
        print("\nYou can check out the Code2College Frequently Asked Questions (FAQs) section for more details.")
    elif option == "5":
        print("\nThank you for using the Code2College chatbot. Goodbye!")
    else:
        print("\nInvalid option. Please try again.")

# Call the chatbot function to start the interaction
chatbot()
