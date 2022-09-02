print("welcome to atm")
a_pin=1234
bal=5000
p=3
while p>0: 
    pin=int(input("enter your pin :- "))
    if pin==a_pin:
        while True: 
            print("(1)..withdraw\n(2)..balance\n(3)..pin change\n")
            ch=int(input("enter your choise :- "))   

            if ch==1:  
                amo=int(input("enter amount:- "))
                print("withdrawal amount:-",amo)
                total_bal=bal-amo
                print("your balance is  :-",total_bal)

                if amo>=bal:
                    
                    print("insufficient balance")
                    
                else:
                    ch=input("transacation again yes/no :- ")
                    
                    if ch=='yes':
                        
                         ch=int(input("enter your choise :- ")) 
                            
                    else:
                        print("Thanks for visit")
                        break
            elif ch==2:
                print("your balance is :- ",bal)
                break
                
            else:
                print("invalid choise")
                break
        break              
    else:
        p=p-1
        print(p)
        if p==0:
            print("try after 24 hours")
            break
