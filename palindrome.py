def webs(s):
    y = s[::-1]
    if y==s:
        print("palindrome")
    else:
        print("its not")
webs("dood")

first=[1,2,3,4,5,6,7,8,9]
second=[3]
for i in first:
    for j in second:
        # if i==j:
            # continue
        print(i,'*',j,'=',j*i)

# dictt={'wed':34,'thus':56,'thur':45,'fri':67}
# print(sorted(dictt.values()))
# for d in sorted(dictt.items()):
#     print(d,end='')

# hello="childrenplayinginplayground"
# half=(len(hello))//2
# half_word=(hello[0:half]).upper()
# half2=hello[half:]
# full_word=half_word+half2
# print(full_word)





# s ="respect"
# s[::-1]
# print(s)

# r="dood"
# h=r.reversed()
# print(h)