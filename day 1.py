_APple123=10
# 
# print(_APple123)

# Datatype (int,float,str,bool)

#########
# Operators

# age calculator
# birth=2006
# future=2027
# age=future-birth
# print(age)

# age=20
# max=40
# amount=300
# rest=max-age
# total=rest*365*amount
# print(rest)
# print(total)

# age=20
# max=50
# water=4
# years=max-age
# days=years*365
# life=water*days
# print(years)
# print(days)
# print(life)

# trip=900
# mileage=20
# liter=101
# need=trip/mileage
# cost=liter*need
# print(need)
# print(cost)

# usage=2
# month=30
# total=month*usage
# print(total)

# age=20
# days=age*365
# print(days)

# price=500
# disc=30
# decimal=disc/100
# amount=price*decimal
# sub=price-amount
# print(decimal)
# print(amount)
# print(sub)

##########
#----------------------------------
##########
#loop

# x=8
# y=12
# if(x==y):
#     print("x and y are equal")
# elif(x>y):
#     print("x is greather than y")
# else:
#     print("x is lesser than y")
        
# x=input("entera a characther:")
# if(x=="a,e,i,o,u"):
#     print("vowel")
# elif(x!="a,e,i,o,u"):
#     print("consonant")
# elif():
#     print("not a alphabet")        
        
# x=int(input("enter you mark:"))
# if(x==100):
#     print("o grade")
# elif(x>=90 and x<99):
#     print("a grade")
# elif(x>=80 and x<89):
#     print("b grade")    
# elif(x>=70 and x<79):
#     print("c grade")
# elif(x>=60 and x<69):
#     print("d grade")    
# elif(x>=50 and x<59):
#     print("e grade")
# else:
#     print("f grade")    

x = int(input('Enter the cost price of 1 dozen = '))
y = int(input('Enter the selling price of 1 item = '))
selling_price_dozen = y * 12
if selling_price_dozen > x:
    profit = selling_price_dozen - x
    print('It is profit of Rs.', profit)
elif selling_price_dozen < x:
    loss = x - selling_price_dozen
    print('It is loss of Rs.', loss)
else:
    print('No profit, no loss.')