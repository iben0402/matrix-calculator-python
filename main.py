from matrix import Matrix

def interface():
    listOfMatrices = []
    while True:
        command = input("Enter command: ")
        if command == "help":
            print("'create' - creates new empty matrix")
            print("'createRand' - creates matrix with random data (you can adjust the range and type of data)")
            print("'list' - prints you a list of your matrices")
            print("'print' - prints you a chosen matrix")
            print("'edit' - edits chosen matrix")
            print("'dot' - returns a dot product of two matrices and saves it to your list")
            print("'exit' - exits program")
        elif command == "create":
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))
            listOfMatrices.append(Matrix(rows, columns))
            print("Created new matrix under the id: " + str(len(listOfMatrices)-1))
        elif command ==  "createRand":
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))
            min = int(input("Enter minimum value: "))
            max = int(input("Enter maximum value: "))
            type = input("Enter type of data (int|double)")
            if type != "int" and type != "double":
                print("Invalid type of data.")
            else:
                listOfMatrices.append(Matrix(rows, columns))
                listOfMatrices[len(listOfMatrices)-1].randomize(min, max, type)
                print("Created new matrix under the id: " + str(len(listOfMatrices)-1))
        elif command == "list":
            for i in range(len(listOfMatrices)):
                print("Matrix " + str(i) + ":")
                listOfMatrices[i].printMatrix()
        elif command == "print":
            i = int(input("Enter number of matrix you want to print: "))
            listOfMatrices[i].printMatrix()
        elif command == "edit":
            i = int(input("Enter number of matrix you want to edit: "))
            listOfMatrices[i].edit()
        elif command == "dot":
            if len(listOfMatrices) < 2:
                print("You don't have enough matrices created. Create new matrix using 'create' command")
            else:
                first = int(input("Enter id of first matrix"))
                second = int(input("Enter id of second matrix"))
                result = listOfMatrices[first].dot_product(listOfMatrices[second])
                if result == None:
                    print("You can't multiply these matrices")
                else:
                    listOfMatrices.append(result)
                    print("Result saved under id: " + str(len(listOfMatrices)-1))
        elif command == "exit":
            print("Leaving calculator, see you soon!")
            break;
        else:
            print("Invalid command. Enter 'help' to see the list of avaliable commands")

def main():
    print("")
    print("------------------------------------------------------------")
    print("Welcome to the matrix calculator! Enter commands to navigate")
    print("Type help to see the commands")
    print("------------------------------------------------------------")
    print("")
    interface()


if __name__ == "__main__":
    main()