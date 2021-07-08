#!/usr/bin/env python
# coding: utf-8

# In[15]:


class hotel:
    bal=0
    
    def veg(s):
        print('''
                     Grand Hotel
        ---------------Veg Menu----------------------
        samosa--------------------10 Rs | Type S
        Vadapav-------------------20 Rs | Type V
        Misal---------------------40 Rs | Type M
        
        press 0 for Back to Main menu
        ''')
        
    def nonveg(s):
        print('''
                      Grand Hotel
        ---------------Non veg Menu------------------
        Chicken Dish--------------80 Rs | Type ch
        Mutton Dis---------------100 Rs | Type ma
        Fish Fry------------------60 Rs | Type fi
        
        press 0 for Back to Main menu
        ''')
        
        
    def display(s):
        print('''Please Press 3 for continue
        Press 4 for another category
        press 5 for Exit''')
        
    def a1(s):
        s.veg()
        dname=input("Enter Dish Name: ")
        if dname=="S":
            qty=int(input("Enter Quantity: "))
            s.bal=s.bal+qty*10
            print("Amount Rs ",s.bal)
        elif dname=="V":
            qty=int(input("Enter Quantity: "))
            s.bal=s.bal+qty*20
            print("Amount Rs ",s.bal)
        elif dname=="M":
            qty=int(input("Enter Quantity: "))
            s.bal=s.bal+qty*40
            print("Amount Rs ",s.bal)
        elif dname=="0":
            s.menu()
        else:
            print("Please enter right crendential")
            s.a1()
            
    def a2(s):
        s.nonveg()
        dname=input("Enter Dish Name: ")
        if dname=="ch":
            qty=int(input("Enter Quantity: "))
            s.bal=s.bal+qty*80
            print("Amount Rs ",s.bal)
        elif dname=="ma":
            qty=int(input("Enter Quantity: "))
            s.bal=s.bal+qty*100
            print("Amount Rs ",s.bal)
        elif dname=="fi":
            qty=int(input("Enter Quantity: "))
            s.bal=s.bal+qty*60
            print("Amount Rs ",s.bal)
        elif dname=="0":
            s.menu()
            
        else:
            print("Please enter right crendential")
            s.a2()
            
    def work1(s):
        s.display()
        dis1=input("Enter The Number: ")
        if dis1=="3":
            s.order1()
        elif dis1=="4":
            s.menu()
        elif dis1=="5":
            print(" ----------------Thank you! Please visit again-------------------")
            print("Total amount to be paid ",s.bal,"Rs only")
        else:
            print("You have enter wrong credentials...Please enter agqain")
            s.work1()
    
    def order1(s):
        s.a1()
        s.work1()
            
    def work2(s):
        s.display()
        dis1=input("Enter The Number: ")
        if dis1=="3":
            s.order2()
        elif dis1=="4":
            s.menu()
        elif dis1=="5":
            print(" ----------------Thank you! Please visit again-------------------")
            print("Total amount to be paid ",s.bal,"Rs only")
        else:
            print("You have enter wrong credentials...Please enter agqain")
            s.work2()
                
    def order2(s):
        s.a2()
        s.work2()
        
            
    def menu(s):
        print('''-----------------Welcome to Grand Hotel------------------
            Please Press 1 for Veg Menu
            Press 2 for Non Veg Menu
            Press 3 for Exit''')
            
        dis=input("Enter The Number: ")
        if dis=="1":
            s.order1()
            
        elif dis=="2":
            s.order2()
            
        elif dis=="3":
            print(" ----------------Thank you! Please visit again-------------------")
            print("Total amount to be paid ",s.bal,"Rs only")
        
        else:
            print("You have Entered wrong crendential....Please Enter again")
            s.menu()
        
        
                
        
h=hotel()
h.menu()
            
        
        


# In[ ]:





# In[ ]:




