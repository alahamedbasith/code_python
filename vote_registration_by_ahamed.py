#This program is about vote registration created by Ahamed basith
name=input("Enter your correct name:")
print("Hello",name,",Iam Ahamed Basith.Welcome to vote registration")
def again():
    a=int(input("Enter your correct age:"))
    def func():
        return 18-a
    parties="""Available parties in tamilnadu:
                    1.Udaiya Suriyan
                    2.Rettai ilai
                    3.Pressure Cooker
                    4.Vivasayi
                    5.Torchlight """
    def party():
        m = int(input("Enter the correct number to vote which given above:"))
        if m <= 5:
            if m == 0:
                print("Sorry,You are select wrong option.Please enter the correct option")
                party()
            elif m==1:
                ud=input("Why are you select Udaiya suriyan?__Write something....")
                ud1=len(ud)
                print("Total number of words you typed (include spaces),it's shows the strength=",ud1)
                str1=input('type "yes" how computer says position of your word "no" for continue:').lower()
                if str1=="yes":
                    for i in range(ud1):
                        print(ud[(i)],"  Word:",i+1)
                    print(name,"your vote registered sucessfully,coded by Ahamed basith")
                else:
                    print(name,"your vote registered sucessfully,coded by Ahamed basith")    
            elif m==2:
                ret=input("Why are you select Rettai ilai?__Write something....")
                ret1=len(ret)
                print("Total number of words you typed (include spaces),it's shows the strength=",ret1)
                str2=input('type "yes" how computer says position of your word "no" for continue:').lower()
                if str2=="yes":
                    for i in range(ret1):
                        print(ret[(i)],"  Word:",i+1)
                    print(name,"your vote registered sucessfully,coded by Ahamed basith")
                else:
                    print(name,"your vote registered sucessfully,coded by Ahamed basith")
            elif m==3:
                pres=input("Why are you select Pressure Cooker?__Write something....")
                pres1=len(pres)
                print("Total number of words you typed (include spaces),it's shows the strength=",pres1)
                str3=input('type "yes" how computer says position of your word "no" for continue:').lower()
                if str3=="yes":
                    for i in range(pres1):
                        print(pres[(i)],"  Word:",i+1)
                    print(name,"your vote registerd sucessfully,coded by Ahamed basith") 
                else:
                    print(name,"your vote registered sucessfully,coded by Ahamed basith")
            elif m==4:
                viv=input("Why are you select Vivasayi?__Write something....")
                viv1=len(viv)
                print("Total number of words you typed (include spaces),it's shows the strength=",viv1)
                str4=input('type "yes" how comuter says position of your word "no" for continue:').lower()
                if str4=="yes":
                    for i in range(viv1):
                        print(viv[(i)],"  Word:",i+1)
                    print(name,"your vote registerd sucessfully,coded by Ahamed basith")
                else:
                    print(name,"your vote registered sucessfully,coded by Ahamed basith")
            elif m==5:
                tor=input("Why are you select Torchlight?__Write something....")
                tor1=len(tor)
                print("Total number of words you typed (include spaces),it's shows the strength=",tor1)
                str5=input('type "yes" how computer says position of your word "no" for continue:').lower()
                if str5=="yes":
                    for i in range(tor1):
                        print(tor[(i)],"  Word:",i+1)
                    print(name,"your vote registerd sucessfully,coded by Ahamed basith")    
                else:
                    print(name,"your vote registered sucessfully,coded by Ahamed basith")
            else:
                print("your vote Registered Sucessfully,coded by Ahamed basith")
        else:
            print("Sorry,You are select wrong option.Please enter the correct option")
            party()
    if a<110:
        if a==0:
            print( "Sorry,enter a valid age")
            again()
            pass
        elif a<17:
            print("Sorry,You are not eligible,Wait",func(),"more years")
        elif a==17:
            print( "Sorry,You are not eligible,Wait one more year")
        if a==18:
            print( 'You have voter ID type "yes" ')
            print( 'Don\'t have voter ID type "no" ')
            c=input("enter the correct option=")
            d=c.lower()
            if d=="yes":
               print("You are eligible!!!")
               print(parties)
               party()   
            else:
               print("Sorry,You are not eligible...Apply voter ID and then vote")
        elif a>18:
           print("You are eligible")
           print(parties)
           party()
    else:
        print("Select a Valid Age")
        again()
    print('Do you want to continue again for registration Type "yes"')
    print('Iam complete my registration Type "no"')
    new=input("Enter the correct option:").lower()
    if new=="yes":
       print (again())
    else:
        print("This program is terminated")
        pass
again()
print("Only for education purpose,coded by Al Ahamed Basith")






    

       

