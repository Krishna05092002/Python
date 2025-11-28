class Assignmentfunctions:
    def subfieldinAI():
            subfields = input("Sub- Fields in AI are:")
            list=["Machine learning","Neural  network","Vision","Robotics",
                  "Speech processing","Natural language processing"]
            for temp in list:
                print(temp)
                
    def oddeven():
        num=int(input("Enter a Num:"))
        if((num%2 )== 0):
            print("Even number")
            number="Even number"
        else:
            print("Odd number")
            number="Odd number"
        return number

    def Elegible():
        Gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(Gender=='Male'):
            if(age<21):
                print("Not Eligible")
        elif(Gender=='Female'):
                print("Not Eligible")
        else:
            print("Eligible")

    def percentage():
        a1=int(input("Subject1:"))
        a2=int(input("Subject2:"))
        a3=int(input("Subject3:"))
        a4=int(input("Subject4:"))
        a5=int(input("Subject5:"))
        total = a1+a2+a3+a4+a5
        print("Total:", a1+a2+a3+a4+a5)
        percent= (total/ 500) * 100
        print("percentage:", percent)

    def triangle():
        Height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(Height*breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Height1+Height2+breadth)
