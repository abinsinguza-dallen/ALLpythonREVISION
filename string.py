var ="cookies"
p="hello mum how are you %s "% var
print(p)

x="Dallen"
half=len(x)//2
y=''
for b in range(len(x)) :
    if b >=half:
        y+=x[b].upper()

    else:
        y+=x[b]
print(str(y))

x="ilovemymum"
d=len(x)//2
b=''
for n in range(len(x)):
    if n>=d:
     b+=x[n].upper()
    else:
        b+=x[n]
print(str(b))

count=0
for letter in "hello world":
    if letter=='l':
        count+=1
print(count,"letters")

def word(hello):
    length=len(hello)
    if length>=3:
        if hello[-3:]=='ing':
            hello+='ly'
        else:
            hello+='ing'  

    print(hello)  
    from this import s


def numbs(f):
    x=s
    x.pop()
    print(["da","seth","res"])

def numbs():
    mylist=["dallen",[8,4,5],[3,6,6]]
    print(mylist[1][0])

numbs()

d=[1,3,4,5,6,7,8]
d.remove(8)
print(d)

def num():
    f=num.remove(num[3])
    print(f)

    num()

def namee():
    name=["speria","gal","gal","pop","dallen"]  
    print(name.count("gal"))  

    
    
def smallest():
    smallest=[2,3,4,5,6,7,98]
    b=min(smallest)
    print(b)
smallest()


def divisible():
    d=[]
    for b in range(100,200):
        if b %7==0:
            d.append(b)
            print(d)
divisible()

def itegs ():
    w=int(input("enter number :"))
    d=int(input("enter a number"))
    m=w+d
    if m>10:
        print(m)

    else:
        m<=10
        print("the number i s correct")    
itegs() 

def numbd():
    n=[4,45,6,7,8]
    if 3 in n:
        print(True)
    else:
        print(False)    
numbd() 

def get (h):
    if 4 in h:
        print(True)
    else:
        print(False)    

get([2,45,67,8,9])

def fruits(e):
    e.pop()
    print(e)

fruits(["apple","tomato","aple","rest"])

def car(r):
    r.sort()
    print(r)

car(["rete","baba","call"])
s=[2,3,4,5,6,7,5,7,8]
print(s[-1::])











    



    
       
    
       


