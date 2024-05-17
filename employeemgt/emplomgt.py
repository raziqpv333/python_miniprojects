employee=[]
print("employee management system")
while True:
    print("1.add employees\n2.view employees\n3.update employees\n4.delete emplyees\n5.search employee\n6.exit")
    choice=int(input("enter a choice number"))
    if choice==1:
        name=input("enter employees name")
        id=int(input("enter employees ID number"))
        position=input("enter employees position")
        salary=int(input("enter employees salary "))
        employee.append([name,id,position,salary])
    elif choice==2:
        for i in employee:
            print(i)
    elif choice==3:
        id=int(input("enter employees id number"))
        f=0
        for i in employee:
            if id in i:
                position=input("enter employees position")
                i[2]=position
                salary=input("enter employees salary")
                i[3]=salary
                f=1
        if f==0:
            print("not available") 
    elif choice==4:
        id=int(input("enter employees id number"))
        f=0
        for i in employee:
            if id in i:
                employee.remove(i)
                f=1
        if f==0:
            print("not available") 
    elif choice==5:
        id=int(input("enter employees id"))
        f=0
        for i in employee:
            if id in i:

                print(i)
        if f==0:
            print("not available")         

    elif choice==6:
        break
    else:
        print("invalid choice")
        


            