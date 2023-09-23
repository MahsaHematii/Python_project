n=int(input("enter rhombus's sides: "))
def rhombus(n):
    rhombus=[]

    for i in range(0,2*n-1):
        row=[]
        for j in range(0,2*n-1):
            row.append(" ")
        
        rhombus.append(row)
    
    for i in range(0,n):
        for j in range(n-i-1,n+1):
            rhombus[i][j]="*"
            rhombus[2*n-2-i][j]="*"

    for row in rhombus:
        for column in row:
            print(column, end='')
        print(" ")


rhombus(n)