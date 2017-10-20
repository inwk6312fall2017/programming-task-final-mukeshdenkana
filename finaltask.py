f1=open("Book1.txt",'r')
f2=open("Book2.txt",'r')
f3=open("Book3.txt",'r')
 
l = f1.readlines()
string = l[0]
stringsplit = string.split()

f1 = []
for i in stringsplit:
    f1.append(len(i))
    e = max(f1)
for j in stringsplit:
    if len(j) == e:
	return j
f2 = open('txt.txt','r')
l = f2.readlines()
string = l[0]
stringsplit = string.split()

f2 = []
for a in stringsplit:
    f2.append(len(b))
    e = max(f2)
for b in stringsplit:
    if len(b) == e:
        return b
f3 = open('txt.txt','r')
l = f3.readlines()
string = l[0]
stringsplit = string.split()

f3= []
for x in stringsplit:
    f3.append(len(x))
    e = max(f3)
for y in stringsplit:
    if len(y) == e:
        return y

if j>b>y or j>y>b :
	print ("largest word:",j)
elif b>y>j or b>j>y :
	 print ("largest word:",b)
else :
	print("largest word:", y)
