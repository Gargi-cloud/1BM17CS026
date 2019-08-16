lis=[]
even_lis=[]
n=int(input("enter the size of the list: "))
for i in range(0,n):
    numbers=int(input("enter the numbers into the list : "))
    lis.append(numbers)
    print(lis)
    def divide(lis):

        for i in lis:
            if(i%2==0):
                even_lis.append(i)
divide(lis)
print(even_lis)
