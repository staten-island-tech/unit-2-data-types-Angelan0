""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" values=[1,3,5,6,8,14,16,18,20,22,24,26,28]
print(values[2])
print(values[5])
print(values[8]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" sent=input("sentence ")
word=sent.split( )
count=0
for i in word:
    count=count+1
    print(f"there are {count} words") """


""" day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 73:
    print('warm')
elif temp == 73:
    print('perfect')
else:
    print('cold') """

""" x=10
if 0 == x%2:
    print('even')
else:
    print('odd') """

""" bill=float(8)
service = input('how was the service?')
if service == "great":
    bill=bill*1.25
    print(bill)
elif service == "good":
    bill=bill*1.2
    print(bill)
elif service == "okay":
    bill=bill*1.15
    print(bill)
elif service == "bad":
    bill=bill*1
    print(bill) """

num=int(input('input a number '))
def factors(x):
    print(f"The factors of {x} are:")
    for i in range(i):
        if x%i == 0:
            print(i)
factors(num)
