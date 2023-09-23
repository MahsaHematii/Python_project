n=int(input("enter the first number:"))
m=int(input("enter the second number:"))      

def muliplication_table(n,m):

    for i in range(n+1):
        if i==0:
            for j in range(m+1):
                if j==0:
                    print("×", end=" ")
                else:
                    print(j,end=" ")   
            print()        
        else:
            for j in range(m+1):
                if j==0:
                    print(i, end=" ")
                else:
                    print(i*j, end=" ")
            print()   

muliplication_table(n,m)