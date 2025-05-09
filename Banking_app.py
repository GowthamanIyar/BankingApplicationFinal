Entering_User_ID=10000
Entering_User_password=20       #global variable
Balance=50000
Entering_User_Activity_No=00
Amount=00

import datetime as dt    
on_time=dt.datetime.now()                                          #Time input for even every Transaction when were Done
Current_time=on_time.strftime("%A, %Y-%b-%d   %I:%M:%S%p.")

Customers={10000:{'No':00,'ID':10000,'name':'admin','age':21,'address':'address','NIC_No':'NIC_No','Contact_No':123456789}}
Dic_Customer_Details=Customers[Entering_User_ID]                     #Dic customers --> important recoded data list 
List_Customer_Details=list(Dic_Customer_Details.values())

Customers_activities={10000:{00:{'No':00,"Time":Current_time,'diposit':00,'withdraw':00,'balance':30000}}}
Dic_Customer_activities=Customers_activities[Entering_User_ID]
Next_Activity_No=len(Dic_Customer_activities)
List_of_Dic_Customer_activity_Numpers=list(Dic_Customer_activities.keys())
Dic_Customer_activity=Dic_Customer_activities[00]                   #Dic Customers_activities --> important recoded data list
List_Customer_activity=list(Dic_Customer_activity.values())

Users={10000:{'NO':00,'ID':10000,'password':'35666960Gk','password_1':'8170126Gk'}}
Dic_User=Users[Entering_User_ID]
List_User=list(Dic_User.values())                                        #Dic Users --> important recoded data list

def Choice_1():    
    while True:
        try:
            print("====================================================================")
            print("1.Main Menu \t2.Exit \n")
            Choice_1=int(input("Please Enter Your New Choice: ",))
            if Choice_1==1:                                                #Ask to Customer; are you going do another service or exit
                Main_Menu()
            elif Choice_1==2:
                print("\nThank For Using Our Service. \nPlease take Your Card!!!")
                print("====================================================================")
                Options()
            else:
                print("\nEnter the Correct Number!!!")
        except ValueError:
            print("\nPlease Enter Number Only!!!")

def Main_Menu():    
    while True:
        try:
            print("====================================================================")
            print("1.Deposit Money \t\t2.Withdraw Money \n3.Check Balance \t\t4.Transaction History") 
            print("5.Change Password \t\t6.Transfer Amount \n7.Exit \n")       
            Choice=int(input("Enter Your Choice: ",))
            if Choice==1:
                Customer_Deposit()
                Choice_1()
            elif Choice==2:
                User_2nd_time()
                Customer_withdraw()
                Choice_1()                
            elif Choice==3:
                print("====================================================================")
                Balance_check()
                print("Your Available Balance is:Rs ",Balance)        
                Choice_1()
            elif Choice==4:
                print("====================================================================")
                print("Your Transactions Are blow Here!\n")
                Transactions_History()
                Choice_1()
            elif Choice==5:                                                           #to show howmany services are have for customer
                User_2nd_time()                                                       #those are what
                Change_Password()                                                     #ask to customer which service you want
                Choice_1()
            elif Choice==6:
                User_2nd_time()
                Transfer_Amount()
                Choice_1()
            elif Choice==7:
                print("====================================================================")
                print("Thank For Using Our Service. \nPlease take Your Card!!!")
                print("====================================================================")
                Options()
            else:
                print("\nPlease Enter the the Correct Choice Number!!!") 
        except ValueError:
            print("\nPlease Enter Number Only!!!")
            
def User_2nd_time():
    while True:
        try:
            print("====================================================================")            
            User_1=int(input("Please Enter Your User ID Again: ",))
            User_1passcode=input("Please Enter Your Password Again: ",)
            if User_1==Entering_User_ID and User_1passcode==Entering_User_password:
                print("\nRe_Entry Successful!")
                break                                                       #for the safty purposes customer re_login
            else:                                                           #it is important for withdraw & transfer
                print("\nYour User ID or Password is Incorrect!!!")    
                print("Please Enter the Correct User ID and Password!!!")
                print("Thank For Using Our Service. \nPlease take Your Card!!!\n")
                print("====================================================================")
                print("====================================================================")
                Options()
        except ValueError:
            print("\nPlease Enter Number Only For User ID!!!")

def User():
    global Entering_User_ID
    global Entering_User_password 
    while True:
        try:
            print("====================================================================")
            User_1_ID=int(input("\nEnter Your User ID: ",))
            User_1passcode=input("Enter Your Password: ",)
            for key,value in Customers.items():
                if User_1_ID==key:
                    Dic_of_User_1= Users[key]                                          #ustomer Login
                    User_1Password=Dic_of_User_1.get('password')
                    if User_1Password==User_1passcode:
                        Entering_User_ID=User_1_ID
                        Entering_User_password=User_1passcode
                        print("\nlog in is sucessfull!")
                        break                                          
            else:
                print("\nYour User ID or Password is Incorrect!!!")    
                print("Please Enter the Correct User ID and Password!!!")
                print("Thank For Using Our Service. \nPlease take Your Card!!!")
                print("====================================================================")
                print("====================================================================")
                Options()
            Main_Menu()
        except ValueError:
            print("\nPlease Enter Number Only For User ID!!!")
 
def Entry_of_withdraw():
    global Customers_activities
    Dict_of_current_Customer=Customers_activities.get(Entering_User_ID)
    Next_Activity_No=len(Dict_of_current_Customer)
    New_Activity={Next_Activity_No:{'No':Next_Activity_No,"Time":Current_time,'diposit':00,'withdraw':00,'balance':00}}
    Dic_New_Activity=New_Activity.get(Next_Activity_No)
    Dic_New_Activity['withdraw']=Amount
    Dic_New_Activity['balance']=Balance
    Dict_of_current_Customer.update(New_Activity)

def Customer_withdraw():
    global Balance
    global Amount
    while True:
        try:
            Balance_check()
            print("====================================================================")
            print("We didn't give coins,10,20,50Rs.")
            print("So, Please Enter the withdraw money should be as a multiple of 100Rs.")
            print("Eg:SriLankan Rs.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.\n")      #Customers Withdraw purposes     
            Amount_1=int(input("Enter Your Withdraw Amount: ",))
            if Balance-505>=Amount_1:    #Bank min balance is 500
                if Amount_1%100==0:     #Like a ATM withdraw 
                    Balance-=Amount_1+5  # 5Rs for Servise Charge
                    Amount=Amount_1
                    Entry_of_withdraw()
                    print("\nPlease take Your Money: ",Amount_1)                              
                    print("Your New Balance is: ",Balance)
                    break
                else:
                    print("Your Avaiable Balance is:",Balance-505)
                    print("\nWe didn't give coins,10,20,50Rs.")
                    print("So, Please Enter the withdraw money should be as a multiple of 100Rs.")
                    print("Eg:SriLankan Rs.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.")                   
                    break
            else:
                print("\nYou Have not Inof Money. \nYour Balance is: ",Balance)
                print("Your Avaiable Balance is: ",Balance-500)
                break
        except ValueError:
            print("\nPlease Enter Number Only!!!")

def Entry_of_Diposit():
    global Customers_activities
    Dict_of_current_Customer=Customers_activities.get(Entering_User_ID)
    Next_Activity_No=len(Dict_of_current_Customer)
    New_Activity={Next_Activity_No:{'No':Next_Activity_No,"Time":Current_time,'diposit':00,'withdraw':00,'balance':00}}
    Dic_New_Activity=New_Activity.get(Next_Activity_No)
    Dic_New_Activity['diposit']=Amount
    Dic_New_Activity['balance']=Balance
    Dict_of_current_Customer.update(New_Activity)

def Customer_Deposit():
    global Amount
    global Balance
    while True:
        try:
            Balance_check()
            print("====================================================================")
            print("We didn't take coins,10,20,50RS.")                                         #customer's deposit
            print("So, Please put your money should be as a multiple of 100Rs.")
            print("Eg:Srilankan RS.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.\n")       
            Amount_1=int(input("Enter Your Deposit Amount: ",))
            if Amount_1>0:
                if Amount_1%100==0:  #like a ATM diposit
                    Balance+=Amount_1-5 # 5Rs for Servise Charge
                    Amount=Amount_1
                    Entry_of_Diposit()
                    print("\nYour Deposit Amount is: ",Amount_1)                                        
                    print("Your New Balance is: ",Balance)
                    break
                else:
                    print("\nPlease take your diposit Money!!!")
                    print("\nWe didn't take coins,10,20,50RS.")
                    print("So, Please put your money should be as a multiple of 100Rs.")
                    print("Eg:Srilankan RS.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.")
                    break
            else:
                print("\nPlease Enter Positive Value only!!!")                
                break
        except ValueError:
            print("\nPlease Enter Number Only!!!")

# User() 

def Add_Customer():
    global Customers
    global Users
    global Customers_activities
    global Entering_User_ID
    List_of_Customer_Keys=list(Customers.keys())
    Last_User_ID=List_of_Customer_Keys[-1]
    ID = Last_User_ID +1
    Entering_User_ID=ID
    print("====================================================================")
    name=input("Enter the Customer Name: ",)
    age=input("Enter the Customer Age: ",)        
    address=input("Enter the Customer Address: ",)                           #create new accound for new customer 
    NIC_No=input("Enter the Customer NIC Number: ",)                         #only avaiable for admin 
    Contact_No=input("Enter the Customer Mobile Number:",)             
    password=str(len(Customers)+11)+age
    New_Customer={ID:{'No':len(Customers),'ID':ID,'name':name,'age':age,'address':address,
                    'NIC_No':NIC_No,'Contact_No':Contact_No}} 
    New_User={ID:{'No':len(Customers),'ID':ID,'password':password}}
    New_Customers_activities={ID:{00:{'No':00,"Time":Current_time,'diposit':00,'withdraw':00,'balance':00}}}
    print(f"\n{name},Your User ID is: ",ID)
    print(f"{name},Your password is:",password)
    Customers.update(New_Customer)
    Users.update(New_User)
    Customers_activities.update(New_Customers_activities)
    print(f"\n{New_Customer}")
    print("\n",New_User)
    print("\n",New_Customers_activities)
    print("====================================================================")

# Add_Customer()

def Admin_options():
    while True:
        try:
            print("====================================================================")
            print("1.Create Account \t\t2.Deposit Money \n3.Withdraw Money \t\t4.Check Balance")
            print("5.Transaction History \t\t6.Edit Customer Details \n7.Change Customer Password \t8.Change Admin Password \n9.Exit\n")
            Choice=int(input("Enter Your Choice: ",))
            if Choice==1:
                Admin_Using_time()
                Add_Customer()
                Choice_2()
            elif Choice==2:
                Admin_Using_time()
                Search_User()
                Choice_3()                                            #show to admin what are the service are you can handle
                Deposit()                
            elif Choice==3:
                Admin_Using_time()
                Search_User()
                Choice_3()
                withdraw()
            elif Choice==4:
                Admin_Using_time()
                Search_User()
                Choice_3()
                print("====================================================================")
                Balance_check()
                print("Your Available Balance is:Rs ",Balance)        
            elif Choice==5:
                Admin_Using_time()
                Search_User()
                Choice_3()
                print("====================================================================")
                print("Your Transactions Are blow Here!\n")
                Transactions_History()
            elif Choice==6:
                Admin_Using_time()
                Search_User()
                Choice_3()
                Edit_Customer()
            elif Choice==7:
                Admin_Using_time()
                Search_User()
                Choice_3()
                Change_Customer_Password()
            elif Choice==8:
                Admin_Using_time()
                Change_Admin_Password()
            elif Choice==9:
                print("\nWe want to increase Our Valuable Customers Count.")
                Options()
            else:
                print("\nPlease Enter the the Correct Choice Number!!!") 
        except ValueError:
            print("\nPlease Enter Number Only!!!")

def Choice_2():
    while True:
        try:
            print("====================================================================")
            print("1.Add_Customer \t\t\t2.Exit \n")
            Choice_2=int(input("Please Enter Your New Choice: ",))
            if Choice_2==1:
                Admin_Using_time()
                Add_Customer()                      #to quick access to entering new costomers with create accound
            elif Choice_2==2:
                print("\nWe want to increase Our Valuable Customers Count.")               
                Admin_options()
            else:
                print("\nEnter the Correct Number!!!")
        except ValueError:
            print("\nPlease Enter Number Only!!!")

def Admin_Using_time():
    global Entering_User_ID
    while True:
        try:
            print("====================================================================")
            User_1=int(input("Enter Your User ID: ",))
            User_1passcode=input("Enter Your Password: ",)
            List_of_Customer_Keys=list(Customers.keys())
            Admin_ID=List_of_Customer_Keys[0]           
            if User_1==Admin_ID :
                Admin_dict =Users.get(Admin_ID)
                Admin_password=Admin_dict.get('password_1')                   
                if User_1passcode==Admin_password: 
                    Entering_User_ID=Admin_ID              
                    print("\nlog in is sucessfull!")                  #Admin Login
                    break 
                else:
                    print("\nYour Password is Incorrect!!!")    
                    print("Please Enter the Correct Password!!!")
                    Admin_options()
            else:
                print("\nYour User ID is Incorrect!!!")    
                print("Please Enter the Correct User ID and Password!!!")
                Admin_options()
        except ValueError:
            print("\nPlease Enter Number Only For User ID!!!")

def Balance_check():
    global Balance
    Dict_of_current_user_activities=Customers_activities.get(Entering_User_ID)       #current time using customer's check bank balance
    Last_Activity_No=len(Dict_of_current_user_activities)-1
    Last_Activity=Dict_of_current_user_activities.get(Last_Activity_No)
    Current_user_balance=Last_Activity.get('balance')
    Balance=Current_user_balance

def Options():    
    while True:
        try:
            print("====================================================================")
            print("1.Customer login \t2.Bank Managenment login \n")
            Choice_1=int(input("Enter Your Choice: ",))
            if Choice_1==1:
                User()                                                                  #first page of who is going to use Admin or Customer
            elif Choice_1==2:
                Admin_options()
            else:
                print("\nEnter the Correct Number!!!")
        except ValueError:
            print("\nPlease Enter Number Only!!!")

def Change_Password():
    global Users
    global Entering_User_password
    print("====================================================================")
    Dict_of_current_Customer=Users.get(Entering_User_ID)
    New_Password=input("Enter Your New Password: ",)
    NewPassword=input("Please Enter Your New Password Again: ",)
    if New_Password==NewPassword:
        print("\nYour Password Change SuccessFul!")                #change password for Customer to change themself
        Dict_of_current_Customer['password']=New_Password
        Entering_User_password=New_Password
    else:
        print("Your Password Not Change. \nPlease Try Again")

def Search_User():
    global Entering_User_ID
    try:
        print("====================================================================")                        
        Customer_ID=int(input("Please Enter the Customer ID: ",))
        for key,value in Customers.items():
            if Customer_ID==key:
                Entering_User_ID=key
                Dic_of_User_1=value                             #Admin usage to identfy the customer
                print("\n",value) 
                break                              
        else:
            print("\nUser ID is not Defined!!!") 
            Admin_options()
    except ValueError:
        print("\nPlease Enter Number Only For User ID!!!")

def Edit_Customer():
    global Customers
    print("====================================================================")
    name=input("Enter the Customer Name: ",)
    age=input("Enter the Customer Age: ",)        
    address=input("Enter the Customer Address: ",)                       #to change if had any typing error when created accound 
    NIC_No=input("Enter the Customer NIC Number: ",)
    Contact_No=input("Enter the Customer Mobile Number:",)             
    Edit_Customer={'ID':Entering_User_ID,'name':name,'age':age,'address':address,
                    'NIC_No':NIC_No,'Contact_No':Contact_No}        
    print(f"\n{name},Your User ID is: ",Entering_User_ID)
    Customers[Entering_User_ID]=Edit_Customer
    print(f"\n{Edit_Customer}")
    print("====================================================================")

def Choice_3():
    while True:
        try:
            print("====================================================================")
            print("1.Continue \t2.Exit \n")
            Choice_3=int(input("Please Enter Your New Choice: ",))
            if Choice_3==1:      
                print("Customer is Verified")
                break
            elif Choice_3==2:                                                    #Admin using time if Customer & customer id not match as the time stop purpose
                print("\nWe want to increase Our Valuable Customers Count.")               
                Admin_options()
            else:
                print("\nEnter the Correct Number!!!")
        except ValueError:
            print("\nPlease Enter Number Only!!!")

def Change_Customer_Password():
    global Users
    print("====================================================================")
    Dict_of_current_Customer=Users.get(Entering_User_ID)
    New_Password=input("Enter Your New Password :",)
    NewPassword=input("Please Enter Your New Password Again :",)
    if New_Password==NewPassword:                                   #when Customer forgot there passwprs
        print("\nYour Password Change SuccessFul!")
        Dict_of_current_Customer['password']=New_Password
        print("\nCustomer New Password is: ",New_Password)
    else:
        print("Your New Passwords are not match. \nPlease Try Again")

def Change_Admin_Password():
    global Users
    print("====================================================================")
    Dict_of_Admin=Users.get(Entering_User_ID)
    New_Password=input("Enter Your New Password: ",)
    NewPassword=input("Please Enter Your New Password Again: ",)
    if New_Password==NewPassword:
        print("\nYour Password Change SuccessFul!")                #Admin Change there own password
        Dict_of_Admin['password_1']=New_Password
        
    else:
        print("Your Password Not Change. \nPlease Try Again")

def withdraw():
    global Amount
    global Balance
    while True:        
        try:
            Balance_check()
            print("====================================================================")           
            Amount_1=int(input("Enter Your Withdraw Amount: ",))
            if Balance-500>=Amount_1:    #Bank min balance is 500
                Balance-=Amount_1+5 # 5Rs for Servise Charge
                Amount=Amount_1
                Entry_of_withdraw()
                print("\nPlease take Your Money: ",Amount_1)
                print("Your New Balance is: ",Balance)
                break                                                     #in side of  the bank customers withdraw with Admin Help
            else:
                print("\nYou Have not Inof Money. \nYour Balance is: ",Balance)
                print("Your Avaiable Balance is: ",Balance-500)
                break
        except ValueError:
            print("\nPlease Enter Number Only!!!")

def Deposit():
    global Balance
    global Amount
    while True:
        try:
            Balance_check()
            print("====================================================================")
            Amount_1=int(input("Enter the Deposit Amount: ",))
            if Amount_1>0:
                Balance+=Amount_1-5 # 5Rs for Servise Charge
                Amount=Amount_1
                Entry_of_Diposit()
                print("\nDeposit Amount is: ",Amount_1)           #in side of the bank diposit for Customer With Admin Help
                print("New Balance is: ",Balance)
                break
            else:
                print("\nPlease Enter Positive Value only!!!")                
                break
        except ValueError:
            print("\nPlease Enter Number Only!!!")

def Transactions_History():
    Dict_of_current_Customer=Customers_activities.get(Entering_User_ID)
    for key,value in Dict_of_current_Customer.items():
        # Dic_Customer_Activity=value
        # List_Activity=list(Dic_Customer_Activity.values())     
        print("\n",value)

def Transfer_Amount():
    global Balance
    global Customers_activities
    global Amount
    while True:
        try:
            Balance_check()
            print("====================================================================")
            print("We didn't give coins,10,20,50Rs.")
            print("So, Please Enter the Transfer money should be as a multiple of 100Rs.")
            print("Eg:SriLankan Rs.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.\n")           
            Amount_1=int(input("Enter Your Transfer Amount: ",))
            if Balance-505>=Amount_1:            #Bank min balance is 500
                True
                if Amount_1%100==0:                                    #for Customer tranfsfer there cash to another accound
                    True
                    try:
                        print("====================================================================") 
                        Customer_ID=int(input("Enter the Customer ID: ",))
                        Customer1_ID=int(input("Please Enter the Customer ID Again: ",))
                        if Customer_ID==Customer1_ID:
                            for key,value in Customers.items():
                                if key==Customer_ID:
                                    Dic_of_Customer=value
                                    Name_of_Customer=Dic_of_Customer.get('name')
                                    while True:
                                        try:
                                            print("====================================================================")
                                            print("Customer Name is: ",Name_of_Customer)                                    
                                            print("\nif this Name is correct please enter to continue")
                                            print("if this Name incorrect please enter to exit")
                                            print("1.Continue \t2.Exit \n")
                                            Choice_1=int(input("Enter Your New Choice: ",))
                                            if Choice_1==1:
                                                Balance-=Amount_1+5 # 5Rs for Servise Charge
                                                Amount=Amount_1
                                                Entry_of_withdraw()

                                                Dict_of_Getting_Customer=Customers_activities.get(Customer1_ID)
                                                Next_Activity_No=len(Dict_of_Getting_Customer)
                                                New_Activity={Next_Activity_No:{'No':Next_Activity_No,"Time":Current_time,'diposit':00,'withdraw':00,'balance':00}}
                                                Dic_New_Activity=New_Activity.get(Next_Activity_No)
                                                Dic_New_Activity['diposit']=Amount_1
                                                Privous_Activity=Dict_of_Getting_Customer.get(Next_Activity_No-1)
                                                Balance_1=Privous_Activity.get('balance')                                                                                           
                                                Balance_1+=Amount_1
                                                Dic_New_Activity['balance']=Balance_1
                                                Dict_of_Getting_Customer.update(New_Activity)                                                
                                                print("\nYour Transfer Amount is: ",Amount_1)
                                                print("Your New Balance is: ",Balance)                                                 
                                            elif Choice_1==2:
                                                print("\nThank For Using Our Service. \nPlease take Your Card!!!")
                                                print("====================================================================")
                                                Options()
                                            else:
                                                print("\nEnter the Correct Number!!!")
                                                continue
                                            break
                                        except ValueError:
                                            print("\nPlease Enter Number Only!!!") 
                                    break
                            else:
                                print("Customer ID is not Found!!!")
                                Choice_1()
                            break
                        else:
                            print("Your Re_Enter Customer User ID is Not Match") 
                            Choice_1()     
                    except ValueError:
                        print("\nPlease Enter Number Only!!!") 
                else:
                    print("Your Avaiable Balance is:",Balance-505)
                    print("\nWe didn't give coins,10,20,50Rs.")
                    print("So, Please Enter the Transfer money should be as a multiple of 100Rs.")
                    print("Eg:SriLankan Rs.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.")                   
                    Choice_1()
            else:
                print("\nYou Have not Inof Money. \nYour Balance is: ",Balance)
                print("Your Avaiable Balance is: ",Balance-500)
                Choice_1()
        except ValueError:
            print("\nPlease Enter Number Only!!!")

def Add_Customer_Detail():
    file=open("Customer_Details.txt","a")
    file.writelines(str(List_Customer_Details))
    file.close()

def Add_User():
    file=open("User_Details.txt","a")
    file.writelines(str(List_User))
    file.close()

def Add_Activity():
    file=open(f"Customer_{Entering_User_ID}_activities.txt","a")
    file.writelines(str(List_Customer_activity))
    file.close()

def Read_Activity():
    file=open(f"Customer_{Entering_User_ID}_activities.txt","r")
    file.readlines()
    file.close()

Options()