from db_creation import *
from crud_functions import *
from crud import *



def main():
    while True:
        # Display main menu and prompt user for action
        action = input("Choose an action: (1) Create Account, (2) delete user, (3) update user (4) view user, (e) exit: \n")
        
        match action:
            case "1":
                create_user()
            case "2":
                delete_user()
            case "3":
                update_user()
            case "4":
                read_users()
            case "e":
                quit()
            case _:
                 print("Invalid choice, please try again.")



if __name__ == "__main__":
    main()

