#1)...choise no arithmetic
while True:
    print("1.(+)...2.(-)...3.(*)...4(//)...5.(exit)\n")
    ch=int(input("enter your choise no :- "))
    if ch>=1 and ch<=5:
        if input==ch:
            a=int(input("enter 1st digit :- "))
            b=int(input("enter 2nd digit :- "))      
        if ch==1:
            c=a+b
            print("addition a & b is :- ",c,"\n")
        elif ch==2:
            c=a-b
            print("substraction a & b is :- ",c,"\n")
        elif ch==3:
            c=a*b
            print("multiplication a & b is :- ",c,"\n")
        elif ch==4:
            c=a//b
            print("division a & b is :- ",c,"\n")
        elif ch==5:
            print("exit")
            break
        else:
            print("invalid")
    else:
        print("invalid digit")
        break
