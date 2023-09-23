number_rows = int(input("enter number of rows: "))
number_coloumns = int(input("enter number of coloumns: "))

def chess(number_rows, number_coloumns):
    for i in range(number_rows):
        if i % 2 == 0:
            for j in range(number_coloumns):
                if j % 2 == 0:
                    print("*", end = " ")
                else:
                    print("#", end = " ")
            print()

        else:
            for j in range(number_coloumns):
                if j % 2 == 0 :
                    print("#", end = " ")

            else:
                print("*", end = " ")

        print()
chess(number_rows, number_coloumns)