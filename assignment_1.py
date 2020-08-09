 -*- coding: utf-8 -*-

""""1. Develop a code for below scenario
            0: monkey
            1: rooster
            2: dog
            3: pig
            4: rat
            5: OX
year % 12 = 6: tiger
            7: rabbit
            8: dragon
            9: snake
            10: horse
            11: sheep"""

y=int(input('enter any year - '))
animals=('monkey','rooster','dog','pig','rat','ox','tiger','rabbit','dragon','snake','horse','sheep')
re = y%12;
print(animals[re])

                                     

"""2. A Quick Fox Transport Co. wants to develop an application for calculating amount based on distance and weight of goods. The charges (Amount) to be calculated as per rates given below. 

 distance  |     Weight       |     charge per km
           |     >=100        |        Rs.5/-
 >=500     |  >=10 &<=100     |        Rs.6/-
           |     <=100        |        Rs.7/-
-----------|------------------|---------------------
 <500      |     >=100        |        Rs.8/-
           |     <100         |        Rs.5/-
"""

l=float(input('enter distance (in kms) - '))
k=float(input('enter weight (in kgs) - '))
if (l>=500):
  if k>=100:
    print('amount to be charged is',5*l)
  elif k>=10 and k<100:
    print('amount to be charged is',6*l)
  else:
    print('amount to be charged is',7*l)
else:
  if k>=100:
    print('amount to be charged is',8*l)
  elif k<100:
    print('amount to be charged is',5*l)



"""3. A theater in Delhi wants to develop a computerized Booking System. The theater offers different types of seats. The Ticket rates are- Stalls- Rs. 625/-, Circle- Rs.750/-, Upper Class- Rs.850/- and Box- Rs.1000/-. A discount is given 10% of total amount if tickets are purchased on Cash. In case of credit card holders 5% discount is given."""

seat={1:625,2:750,3:850,4:1000}
pay={1:"cash",2:"credit"}
print("the rates of seat are")
print("stall - 625, circle - 750, upper circle - 850, box - 1000")
print("1 - stall, 2 - circle, 3 - upper circle, 4 - box ")
ac=int(input("enter type of seat to book - "))
py=int(input("enter payment option 1 - cash and 2 - credit - "))
if pay[py]=="cash":
  amt=seat[ac]
  print("you will get 10% discount by paying through cash") 
  amt=amt-amt*0.1
  print("total bill is - ", amt)
elif pay[py]==credit:
  amt=seat[ac]*no
  print("you will get 5% discount by paying through cash") 
  amt=amt-amt*0.05
  print("total bill is - ", amt)

"""4.	Develop a program that calculates the energy needed to heat water from an initial temperature to a final temperature. Your program should prompt the user to enter the amount of water in kilograms and the initial and final temperatures of the water. The formula to compute the energy is 
Q = M * (finalTemperature – initialTemperature) * 4184.
where M is the weight of water in kilograms, temperatures are in degrees Celsius,  and energy Q is measured in joules.
"""

M=int(input('enter water in kgs - '))
I=int(input('enter initial temperature in celsius - '))
F=int(input('enter final temperature in celsius- '))
Q=M*(F-I)*4184
print(Q,"KJ energy is used")




"""5. Develop a program that prompts user to enter month and  print 
a. “Winter ” -   December ,January and February
b. "Spring”  -   March ,April and May
c. “Summer”  --- June ,July, August
d. “Autumn ”  -- September ,October, November
"""

m=input('enter month - ')
if m=='december' or m=='january' or m=='february':
  print('winter')
elif m=='march' or m=='april' or m=='may':
  print('spring')
elif m=='june'or m=='july'or m=='august':
  print('summer')
elif m=='september' or m=='october'or m=='november':
  print('autumn')



"""Computing Body Mass Index  You can use nested if statements to write a program that interprets body mass index. Body Mass Index (BMI) is a measure of health based on height and weight. It can be cal-culated by taking your weight in kilograms and dividing it by the square of your height in meters. The interpretation of BMI for people 20 years or older is as follows:

BMI                |    Interpretation
-------------------|---------------------
BMI < 18.5         |     Underweight
18.5 < BMI < 25.0  |     Normal
25.0 < BMI < 30.0  |     Overweight
30.0 < BMI         |     Obese

Write a program that prompts the user to enter a weight in pounds and height in inches and displays the BMI.
"""

H=float(input('enter heignt (in inches) - '))
W=float(input('enter weight (in pounds) - '))
B=(W*703)/(H**2);
if B<18.5:
  print('your BMI is ', B)
  print('you are UNDER WEIGHT')
elif B>18.5 and B<25:
  print('your BMI is ', B)
  print('you are NORMAL WEIGHT')
elif B>25 and B<30:
  print('your B is ', B)
  print('you are OVER WEIGHT')
else:
  print('your BMI is ',B)
  print('you are OBESE')


    

"""Write a program that reads an integer between 100 and 1000 and adds all the digits in the integer"""

N=int(input('enter a number between 100 and 1000 - '))
s=0
while(N>0):
  s=s+(N%10)
  N=N//10
print('sum of the digits in number is ',s)





"""Print all palindrome numbers between 1 to 1000."""

for num in range(1,1001):
  t=num
  r=0
  while t>0:
    rem=t%10
    r=r*10+rem 
    t=t//10
  if(num==r):
      print(num, end='\n')


        
        
"""Print all Armstrong numbers between 1 to 1000."""

for NUM in range(1,1001):
  P = len(str(NUM))
  C = NUM
  sum=0
  while C > 0:
    DIG = C % 10
    sum = sum + (DIG ** P)
    C=C// 10
  if (NUM == sum):
     print(NUM)


        
        
 """Write a Java program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and print "Buzz" for the multiples of five. When number is divided by both three and five, print "fizz buzz"."""

for i in range(1,101):
  if(i%3==0 and i%5==0):
    print("fizz , Buzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)


    
    
    
 """11.	Spider Problem: A spider present at the bottom of the well of height H, needs to get out of it, using the slippery wall of the well. It decides to climb up the well; it goes up U meters and slips down D meters in one single step. So, in each step it covers (U-D) meters, and if the spider gets out of the well by covering U meters in the last step it doesn’t a slip back. For example, if the spider climbs up 5 meters and slips down by 3 meters in a single step, it covers (U - D) m in each step and 96 m in 48 steps, but in the 49th step it climbs up 5 m and reaches out of the well and it will not slip down and the step is counted as one step.     
Input: Each test case will contain 3 integers ’H’ height of the well, next ’U’ meters climbs up in each step, and the last ’D’ meters slips down in each step.
Output:  The number of steps 'N' required to get out of the well.
"""

HE=int(input('enter height of well in meters - '))
UP=int(input('enter meter climbed by spider in one step - '))
DO=int(input('enter meter sliped by spider in one step - '))
STEP=0
while HE>=UP:
  STEP=STEP+1
  HE=HE-(UP-DO)
STEP+=1
print('number of steps by spider is ',STEP)
