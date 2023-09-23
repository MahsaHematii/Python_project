n= int(input("please enter n: "))


def khayam_paskal(n):
    list=[]
    for i in range(n):
        list.append([1]*(i+1))
      
    for i in range (2,n):
        for j in range(1,i):
             list[i][j]=list[i-1][j]+list[i-1][j-1]
    return list      

k=khayam_paskal(n)
for i in k:
    print(i)