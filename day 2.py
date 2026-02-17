#######################

# stype = input("Enter Student Type (MSDS, MSH, MGSD): ").strip().lower()
# if stype not in ["msds", "msh", "mgsd"]:
#     print("Invalid student type entered. Please enter MSDS, MSH, or MGSD.")
#     exit()

# while True:
#     try:
#         tuition = float(input("Enter Tuition Fee: "))
#         break
#     except:
#         print("Invalid input! Please enter a numeric value.")

# if stype == "msds":
#     while True:
#         try:
#             college = float(input("Enter College Fee: "))
#             break
#         except:
#             print("Invalid input! Please enter a numeric value.")
#     hostel = 0
# elif stype in ["msh", "mgsd"]:
#     while True:
#         try:
#             hostel = float(input("Enter Hostel Fee: "))
#             break
#         except:
#             print("Invalid input! Please enter a numeric value.")
#     college = 0

# if stype == "msds":
#     total = tuition + college
# elif stype == "msh":
#     total = tuition + hostel
# else:  
#     total = 1.5 * tuition + hostel

# print(f"Total Fee for {stype.upper()}: {total}")

#transaction limit per day

# account_balance=int(input('enter the account balance='))
#withdrawl_amount=int(input('enter the withdrawl amount='))
# if (withdrawl_amount>account_balance):
#     print('insufficiant fund')
# elif (withdrawl_amount>10000):
#     print('limit exceeded')
# else :
#     print('allow withdrawl')

#atm pin
# account_pin=9486
# x=int(input('enter the pin='))
# if(x==account_pin):
#     print('pin is correct')
#     withdrawl_amount=int(input('enter the withdrawl amount='))
#     if (withdrawl_amount>account_balance):
#         print('insufficiant fund')
#     elif (withdrawl_amount>10000):
#         print('limit exceeded')
#     elif (withdrawl_amount<=0):
#         print('invalid amount')
#     else :
#         print('allow withdrawl')
#         balance_amount=account_balance-withdrawl_amount
#         print('the balance amount is=',balance_amount)
# else:
#     print('wrong pin')

# age=int(input('enter your age='))
# show=input('enter the show time(mng,eve)=')
# child=150
# adult=250
# senior=200
# if (age<=4):
#     print('free entry')
# elif (age>=5) or (age<=16):
#     if (show == "mng"):
#         child_mng=0.5*child
#         print('the ticket price is=',child_mng)
#     else:
#         print('the ticket price is=',child)

# elif (age>=17) or (age<=59):
#     if (show == "mng"):
#         adult_mng=0.5*adult
#         print('the ticket price is=',adult_mng)
#     else:
#         print('the ticket price is=',adult)
# else:
#     if (show == "mng"):
#         senior_mng=0.5*senior
#         print('the ticket price is=',senior_mng)
#     else:
#         print('the ticket price is=',senior)
    
######
#loop

# odd_sum=0
# print("odd number is:")
# for number in range(1,100,2):
#     print(number)
#     odd_sum+=number
# print("the sum of the odd number is:",odd_sum)

# eve_sum=0
# print("number is:")
# for n in range(2,100,2):
#     print(n)
#     eve_sum+=n
# print("the sum of the number is:",eve_sum)

# sum=0
# print("number is:")
# for num in range(1*5,55,5):
#     print(num)
#     sum+=num
# print("the sum of the number is:",sum)

# tam=int(input("tam mark:"))
# eng=int(input("eng mark:"))
# math=int(input("math mark:"))
# sci=int(input("sci mark:"))
# ss=int(input("ss mark:"))
# total=tam+eng+math+sci+ss
# print("total mark=",total)
# aver=total/5
# print("Average=",aver)

    
# for n in range(1,6):
#     print("*"*n)
    
# for n in range(5,0,-1):
#     print("*"*n)
    
# n=0
# i=n
# while i<100:
#     print(i)
#     n=n+i
#     i=i+2
    
# print("---------------------------------------")
# n=1
# i=n
# while i<100:
#     print(i)
#     n=n+i
#     i=i+2
    
#star while
# i=1
# while i<6:
#     print("*"*i)
#     i=i+1
    
# i=5
# while i>0:
#     print("*"*i)
#     i=i-1
    
# i=5
# while i<55:
#     print(i)
#     i+=5
    
def book_seats():
    total_seats = 5
    current_seat = 1  
    while current_seat <= total_seats:  
        passenger_name = input("Enter passenger name: ")  
        print(f"Seat {current_seat} booked for {passenger_name}")  
        current_seat += 1  
    print("All seats are booked.") 
if __name__ == "__main__":
    book_seats()