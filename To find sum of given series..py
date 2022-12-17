#Menudriven Program to print the sum of various series.
def choices():  #Provides differnt choices to the user.
    while True: #To keep the program working till the user wants to.
        print()
        print("SELECT ANY ONE OPERATION TO BE PERFORMED:")
        print("1.To print sum of 1+(1/2!)+(1/3!)+....+(1/n!)")
        print("2.To print sum of 1+(2/2!)+(3/3!)+....+(n/n!)")
        print("3.To print sum of 1+x+(x**2/2!)+(x**3/3!)+....+(x**n/n!)")
        print("4.To print sum of 1+(1/2**2)+(1/3**2)+....+(1/n**2)")
        print("5.Exit.")      
        print()
        choice=int(input("Enter your your choice: "))
        if choice==1:
            sum1()
        elif choice==2:
            sum2()
        elif choice==3:
            sum3()
        elif choice==4:
            sum4()  
        elif choice==5:
            print("PROGRAM TERMINATED")
            break   #Terminates the whole program.
        else:
            print("Enter a valid choice: ")
def sum1():
    n=int(input("Enter the factorial range: "))
    fact=1
    ssum=0 
    for i in range(1,n+1):
        fact*=i
        ssum+=(1/fact)
    print(ssum)
def sum2():
    n=int(input("Enter the factorial range: "))
    fact=1
    ssum=0
    for i in range(1,n+1):
        fact*=i
        ssum+=i/fact
    print(ssum)
def sum3():
    n=int(input("Enter the factorial range: "))
    x=int(input("Enter the value of x: "))
    fact=1
    ssum=1
    for i in range(1,n+1):
        fact*=i
        ssum+=(x**i/fact)
    print(ssum)
def sum4():
    n=int(input("Enter the series range: "))
    ssum=0
    for i in range(1,n+1):
        ssum+=1/(i**2)
    print(ssum)
choices()
        


    
    
    
        
