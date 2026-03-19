#simple calculator 

while True:
    # menu 
    print('-----SIMPLE CALCULATOR-----')
    print('\n1.ADD')
    print('\n2.SUBTRACT')
    print('\n3.MULTIPLICATION')
    print('\n4.DIVISION')
    
    choice=int(input("enter your choice: "))
    ist=int(input("enter first number: "))
    second=int(input("enter second number: "))
    
    if choice==1:
        print(f'sum:{ist+second}')
    elif choice==2:
        print(f'subtraction:{ist-second}')
        
    elif choice==3:
        print(f'multiplication:{ist*second}')
    elif choice==4:
        try:
            print(f'division:{ist/second}')
        except ZeroDivisionError:
            print("divison by zero is not possible")
            
    x=input("do you wish to continue (y/n): ")
    x.lower()
    if x!='y':
        break
    
    
