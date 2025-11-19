import json


def filter_users_by_name(name):
    """
        Filters and prints users whose name matches the given value.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    found = False
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)
        found = True

    if not found:
        print("User with this name not found.")


def filter_by_age(age):
    """
        Filters and prints users whose age matches the given value.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    found = False
    filtered_users= [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)
        found = True

    if not found:
        print("User with this age not found.")


def filter_by_email(email):
    """
         Filters and prints users whose email matches the given value.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    found = False
    filtered_users = [user for user in users if user["email"] == email.lower()]

    for user in filtered_users:
        print(user)
        found = True

    if not found:
        print("User with this email not found.")


if __name__ == "__main__":
    """
     Entry point of the program.

     Prompts the user to choose a filter option (name, age or email) and 
     calls the corresponding filtering function. If the user enters an 
     unsupported option, a message is displayed.
     """
    filter_option = input("What would you like to filter by? (Please enter  'name', 'age' or 'email': ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter the full email address (e.g., user@example.com): ").strip().lower()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")

