# #PIZZA BILL GENERATOR

# print ("Welcome to Pizza Hub")
# print ("Select your piza size")
# print("1. Normal")
# print("2. Deluxe")

# size=int(input("Enter your choice 1 or 2:"))
# if size=='1':
#     print("you selected: Normal ")
# if size=='2':
#     print("you selected: Deluxe")
    
    
# print ("Select pizza type")    
# print("3. Veg")
# print("4. Non Veg")

# type=int(input("Enter your choice 3 or 4:"))
# if type=='3':
#     print("you selected: Veg ")
# if type=='4':
#     print("you selected: Non Veg")
    
# if size== 1 and type==3:
#     base_price=300
# elif size==1 and type==4:
#     base_price=400
# elif size==2 and type==3:
#     base_price=600
# elif size==2 and type ==4:
#     base_price=800
# else:
#     base_price=0

# chesse=int(input("\nEnter Chesse? [1.Yes or 2.No]"))
# extra_chesse=100 if chesse==1  else 0

# topping=int(input("\nEnter topping? [1.Yes or 2.No]"))
# extra_topping=100 if topping==1 else 0

# water_bottle=int(input("\nEnter water bottle? [1.Yes or 2.No]"))
# water_cost=20
# if water_bottle==1:
#     count= int (input("How many water bottels:"))
#     water_cost=count*20
    
# ketchup=int(input("\nEnter ketchup? [1.Yes or 2.No]"))
# Ketchup_cost=5
# if ketchup==1:
#     count= int (input("How many packets:"))
#     Ketchup_cost=count*5
    
# soft_drinks=int(input("\nEnter soft_drinks? [1.Yes or 2.No]"))
# drinks_cost=75
# if soft_drinks==1:
#     count= int (input("How many SoftDrinks:"))
#     drinks_cost=count*75
    
# take_away=int(input("\nEnter take_away? [1.Yes or 2.No]"))
# take_away=20 if take_away==1 else 0
    
# total_cost= base_price +  extra_chesse + extra_topping + water_cost + Ketchup_cost+  drinks_cost + take_away
# gst=total_cost * 0.18
# net_amount= total_cost+gst    
    
# print("-------------------------------------")
# print("        *Pizza Bill Generator*"       ) 
# print("-------------------------------------")
# print("Base Price          =",(base_price))
# print("Extra Cheese        =",(extra_chesse))
# print("Extra Topping       =",(extra_topping))
# print("Water BottLe        =",(water_cost))
# print("Ketchup             =",(Ketchup_cost))
# print("Soft Drinks         =",(drinks_cost))
# print("Take Away           =",(take_away))
# print("------------------------------------")
# print("Total Cost          =",(total_cost))
# print("GST                 =",(gst))
# print("-------------------------------------")
# print("Net Amount          =",(net_amount))
# print("-------------------------------------")
# print("             THANK YOU               ")
# print("-------------------------------------")

# push(data)
# if(stack is full):
#     print stack overflow
# else:
#     top++
#     stack[top or index]=data

# #code
# stack=[]

# while True:
#     print("1. Push,2. Pop,3. Display,4. Exit")
#     choice=int(input("Enter your choice:"))
#     if choice==1:   
#         val=int(input("Enter value:"))
#         stack.append(val)
#         print("Data pushed successfully!",val)
#     elif choice==2:
#         if not stack:
#             print("Stack is empty!")
#         else:
#             print("Popped data:", stack.pop())
            
#     elif choice==3:
#         if not stack:
#             print("Stack is empty!")
#         else:
#             print("top of stack:",stack[-1])
            
#     elif choice==4:
#         print("Exiting the program. Goodbye!")
#         break
        
#     else:
#         print("Invalid choice!.")
        
# from polars import when


# queue=[]

# while True:
#     print("1. Enqueue,2. Dequeue,3. Display,4. Exit")
#     choice=int(input("Enter your choice:"))
#     if choice==1:   
#         val=int(input("Enter value:"))
#         queue.append(val)
#         print("Data enqueued successfully!",val)
#     elif choice==2:
#         if not queue:
#             print("Queue is empty!")
#         else:
#             print("Dequeued data:", queue.pop(0))
            
#     elif choice==3:
#         if not queue:
#             print("Queue is empty!")
#         else:
#             print("Front of queue:",queue[0])
            
#     elif choice==4:
#         print("Exiting the program. Goodbye!")
#         break
        
#     else:
#         print("Invalid choice!.")

# #circular queue
# #1.reuses empty space        
# #save memory

# #if front is free,rear can reuse it

# n=3
# queue=[None]*n
# front=0
# rear=0

# #insert

# queue[rear]=10
# rear=(rear+1)%n

# [10 - - - - - - -]
# [10,20 - - - - - ]
# [10,20,30 - - - -]
# delete->10

# important condition
# queue is full when (rear+1)%n==front
# queue is empty when rear==front


# Pseudocode
# ENQUEUE

# . if queue full -> print "queue full"
# .If first element -> front=0
# .Move rear circularly
# .Insert element

# DEQUEUE
# .If queue empty -> print "queue empty"
# .Remove element at front
# .If last element removed -> reset front & rear
# .Else move front circularly

# Display

# .If empty -> print message
# .Start from from 
# .print until Rear

# | Type           | Insert      | Delete      | Special Feature       |
# | -------------- | ----------- | ----------- | --------------------- |
# | Simple Queue   | Rear        | Front       | FIFO                  |
# | Circular Queue | Rear        | Front       | Reuses space          |
# | Priority Queue | By priority | By priority | Important items first |
# | Deque          | Both ends   | Both ends   | Flexible              |
        


size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue(value):
    global front, rear
    
    if (rear + 1) % size == front:
        print("Queue Full")
        return
    
    if front == -1:
        front = 0
    
    rear = (rear + 1) % size
    queue[rear] = value
    print(value, "inserted")

def dequeue():
    global front, rear
    
    if front == -1:
        print("Queue Empty")
        return
    
    removed = queue[front]
    
    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size
    
    print(removed, "removed")

def display():
    if front == -1:
        print("Queue Empty")
        return
    
    i = front
    print("Queue elements:")
    
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")