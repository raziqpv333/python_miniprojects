students=[]
print("student management system")
while True:
    print("1.add student\n2.view student\n3.update student\n4.delete student\n5.exit")
    choice=int(input("enter your choice number"))
    if choice==1:
        name=input("enter your name")
        rollno=int(input("enter your roll number"))
        age=int(input("enter your age"))
        course=input("enter your couse")
        students.append([name,rollno,age,course])
    elif choice==2:
        for i in students:
            print(i)
    elif choice==3:
        rollno=int(input("enter your roll number"))        
        f=0
        for i in students:
            if rollno in i:
                course=input("enter your course")
                i[3]=course 
                f=1
        if f==0:
            print("not available")     
    elif choice==4:
        rollno=int(input("enter your roll number"))   
        f=0
        for i in students:
            if rollno in i:
                students.remove(i)
                f=1
        if f==0:
            print("not available")     
    elif choice==5:
        break  
    else:
        print("invalid choice")                 
            
      


