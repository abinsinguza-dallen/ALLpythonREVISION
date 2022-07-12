def my_fun(arg1,*argv):
    print("first arguement:",arg1)
    for arg in argv:
        print("next arguement argv",arg)
def kwarg(**kwargs):
    for key,value in kwargs.items():
        print ("%s == %s" %(key, value))
        

from re import X


x=[3,4,5,6,7,8,3]
for g in x:
    print(x[0],x[-1],end="")
    if x[0]==x[-1]:
        print(x)
    else:
        print("dallen")    

m="dallen"
y=len(m)//2
z=m[0]+m[y]+m[-1]       
print(z) 

count=1
while count<7:
    print(count)
    count+=count




def solution(n):
    your code goes here



    print(solution(n))

student={'dallen':20,'speria':34,'tanya':45}
nam=int(input("enter numer:"))
for nam in student.keys():
    if nam==student.keys():
        print('true')

    else:
        print('false')  

people= {'dallen':20,'speria':34,'tanya':45}
people.pop('dallen')
print(people) 

print(type(people))
print(people.values())

p=[2,3,4,5,6,7]
p[0],p[-1]=p[-1],p[0]
print(p)

def words():
    t=["wer","wr","sd","rt","ty"]
    st=""
    for r in t:
        st+=r

        print(st)

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    traverse in the string  
    for ele in s: 
        str1 += ele  
    return str1        
ditt={'dalle':34,'ven':56,'spre':46}
for d in sorted(ditt.items()):
    print(d,end='')
    