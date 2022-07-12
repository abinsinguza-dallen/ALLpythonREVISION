
import datetime

hello=(110,120,130,140,150)
w=(w*5 for w in hello)
print(w)

def average():
    ten_number=[]
    while len(ten_number)!=10:
        user=int(input("enter number:"))
        sum=0
        for num in ten_number:
            print(num)
            ave=sum/len(ten_number)
            print(ave)

def numbs():
    last=[2,75,50,145,525,50]
    for n in last:
        if n%5==0:
            if n>150:
                continue
            if n >500:
                break
            return n
                         
def num():
    m=[12,75,150,180,145,525,50]
    for x in m:
        if x>500:
            break
        elif x>150:
            continue
        elif x%5==0:
            print(x)
            
today=datetime.datetime.now()
print(today)

for a in range(1,11):
    if a>5:
        print("multiplication table of",a)
for b in range(1,11):
    print(a*b, end='')
    print('')

for i in range(1, 11):
    # condition to break outer loop
    if i >=10:
        break
    print('times', i)
    for j in range(1, 11):
        print(i * j, end=' ')
    # print('')


for d in range(1,11):
    if d%2==0 and d>7:
        continue
    print(d)
else: 
    print("i love codding")

    