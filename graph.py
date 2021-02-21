import numpy as np
arr=[]
n= int(input("enter no of vertices"))
for i in range(n):
    mylist=[]
    for j in range(n):
        mylist.append(0)
    arr.append(mylist)
print("initial matrix")
print(np.matrix(arr))
ch=input("do you want to adda a path")
while ch!='n':
    u=int(input("enter source"))-1
    v=int(input("enter enter destination"))-1
    arr[u][v]=1
    ch=input("do you want to adda a path")
print("after adding path")    
print(np.matrix(arr))

mytuple=[]#contains all existiing paths
for i in range(n):
    for j in range(n):
        if(arr[i][j]):
           mytuple.append((i,j))
           #appended existing path
def checkpath(source,destination):
    if (source,destination) in mytuple:
        return True
    for i in range(n):
        if(arr[source][i]):
            a=checkpath(i,destination)
            if(a):
                return a
    return False
ch=input("do you want to check a path")
while ch!='n':
    x=int(input("enter source"))-1
    y=int(input("enter enter destination"))-1
    if checkpath(x,y):
        print("path exists")
    else:
        print("path not exists")
    ch=input("do you want to check a path")











