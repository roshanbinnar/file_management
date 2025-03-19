import os

def crete_file(filename):
    try:
        with open(filename , "x") as f:
            print(f"File_name {filename} : created successfully")
    except FileExistsError:
        print(f"File_name {filename} : Already Exists")
    except Exception as e:
        print(f"Error occured : {e}")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found!")
    else:
        print("Files in directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully")
    except FileNotFoundError:
        print("file not found !")
    except Exception as e:
        print(f"Error occured : {e}")

def read_file(filename):
    try:
        with open(filename ,"r") as f:
            content = f.read()
            print(f"Content of {filename} : \n{content}")
    except FileNotFoundError:
        print("file not found !")
    except Exception as e:
        print(f"Error occured : {e}")

def edit_file(filename):
    try:
        with open(filename , "a") as f:
            content = input("Enter data to add = ")
            f.write(content + "\n")
            print(f"Content added to {filename} successfully")
    except FileNotFoundError:
        print("file not found !")
    except Exception as e:
        print(f"Error occured : {e}")

def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1 : Crete file")
        print("2 : View all files")
        print("3 : Delete file")
        print("4 : Read file")
        print("5 : Edit file")
        print("6 : Exist")

        choice  = int(input("Enter your choice ( 1 to 6 ) = "))

        if choice == 1:
            filename = input("Enter a file_name to create = ")
            crete_file(filename)
        elif choice == 2:
            view_all_files()
        elif choice == 3:
            filename = input("Enter a file_name to delete = ")
            delete_file(filename)
        elif choice == 4:
            filename = input("Enter a file_name to read = ")
            read_file(filename)
        elif choice == 5:
            filename = input("Enter a file_name to edit = ")
            edit_file(filename)
        elif choice == 6:
            print("CLOSING THE APP.....")
            break
        else:
            print("INVALID SYNTAX")
if __name__ == "__main__":
    main()



