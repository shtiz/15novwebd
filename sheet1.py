#2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6 == 6)

a = 20
a += 30
a %= 3
print(a)
print(True * False)
print(True & False)
print(True and False)
print((6>3) and  (7<4) or (18 == 3) and (9>3))
print(True is False)
#print(False in 'False')
print((True == False) or (False > True) and (False <= True ))

#3
s1 = 'nice to have you '
s2 = 'here'
print(s1 + s2)

#4
a  =[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#5
a[0] = [s1]
a += [s2]
print(a)

#6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]

for i in numbers :
        if (i<237 and i%2 == 0) :
            print(i)
            


#7

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red" ,  "Green"])
print((color_list_1 or color_list_2) - (color_list_1 and color_list_2))

#8
# the  brown fox jumps over a lazy dog -> pangram

s = input("enter the string to be checked for pangram :")
l = list(range(65,91))

for i  in s.upper() :
    if ord(i) in l :
        l.remove(ord(i))

if len(l) == 0:
    print('it is pangram')
else :
    print('it is not pangram')            

#9
a = int(input('num :'))
b = int(a*10 + a)
c = int(a*100 +b)
sum = a + b + c
print(sum)

#10

l = input('enter the pattern:').split("#")
x = l[0].split(" ")
y = l[1].split(" ")
x = [int(i) for i in x]
y = [int(i) for i in y]
print(f"l = {l}" , f"x = {x}" , f"y = {y}" , sep = "\n")

#11
a = input("enter the sequence of words:").split(",")
a.sort()
print(a)

#12

d = {'Students' : ['rahul', 'kishore','vidhya' , 'rakhi'],'Marks': [57,87,67,79]}

ma = max(d['Marks'])
i = d['Marks'].index(ma)
print(d['Student'][i])

#13
s = input("enter the string :")
l = 0
d = 0
for i in s :
    if i.isalpha() :
        l += 1
    elif i.isnumeric() :
        d += 1
print(l,d)      

#14
d = {'Name' : ['akash', 'soniya' ,'vishaka' , 'akshay' ,'rahul','vikas'] , 'subject' :['python'  ,'java' ,'python', 'C','python' , 'java'] 
     ,'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

sub = input("enter the subject:")
newData = {"Name : []" , "subject :[]" , "ratings : []"} 
for i in range(len(d['Name'])) :
    s  = d["subject"][i]
    if s == "python" :
        newData["Name"].append(d["Name"][i])
        newData["subject"].append(d["subject"][i])
        newData["ratings"].append(d["ratings"][i])
print(newData)   

#16

ini = (0,0)
up = int(input("enter no. of steps for up :"))
down = int(input("enter no. of steps for down :"))
left = int(input("enter no. of steps for left :"))
right = int(input("enter no. of steps for right :"))
y = abs(up - down)
x = abs(right - left)

fin = (x,y)
d = int(((ini[0] - fin[0]**2) + (ini[1] - fin[1])**2)**0.5)
print(up)
print(down)
print(left)
print(right)
print(x)
print(y)
print(d)
