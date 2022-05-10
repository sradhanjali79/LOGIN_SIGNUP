import json
print("   welcome   ")
print("press 1 for signup")
print("press 2 for login")
user=int(input("press the button.."))
if user==1:
    username=input("enter your name...")
    password1=input("creat password...")
    if len(password1)>=6 and len(password1)<=20:
        c1,c2,c3,c4=0,0,0,0
        for i in password1:
            if i in "abcdefghijklmnopqrstuvwxyz":
                c1+=1
            elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                c2+=1
            elif i in "1234567890":
                c3+=1
            elif i in "@!$":
                c4+=1
        if c1>=1 and c2>=1 and c3>=1 and c4>=1:
            password2=input("Re-enter your password...")
            if password1!=password2:
                print("password don't match")
            else:
                description=input("enter description...")
                dob=input("enter your DOB...")
                Hobbies=input("enter your hobbies...")
                Gender=input("enter your gender male or female...")
                dic={}
                dic1={}
                dic2={}
                z=[]
                dic["name"]=username
                dic["password"]=password1
                dic1["description"]=description
                dic1["DOB"]=dob
                dic1["Hobbies"]=Hobbies
                dic1["Gender"]=Gender
                dic["Profile"]=dic1
                z.append(dic)
                dic2["user"]=z
                with open("user_details.json","w") as f:
                    json.dump(dic2,f,indent=2)
            print("congratulation",username,"you are signed up succesfully")
        else:
            print("please use atleast one capital,one small letter,one digit and one special character")
    else:
        print("invalid password")
else:
    if user==2:
        print("login")
        username1=input("enter your username")
        password3=input("enter your password")
        confirm_password=input("Re-enter your password")
        if len(password3)>=6 and len(password3)<=20:
            c1,c2,c3,c4=0,0,0,0
            for i in password3:
                if i in "abcdefghijklmnopqrstuvwxyz":
                    c1+=1
                elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    c2+=1
                elif i in "1234567890":
                    c3+=1
                elif i in "@!$":
                    c4+=1
            if c1>=1 and c2>=1 and c3>=1 and c4>=1:
                print("logged in successfully")
            else:
                print("your password is wrong")
        else:
            print("login error")
            with open ("user_details.json","a") as f1:
                    json.dump("f2",f1,indent=2)
    else:
        print("you are out of game")


