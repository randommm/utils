#!/usr/bin/python3

#Get sequence of page number for printing a Booklet

begin = ""
end = ""
while not begin.isdigit():
    begin = str(input("set first page number:\n"))
while not end.isdigit():
    end = str(input("set last page numer:\n"))

begin = int(begin)
end = int(end)

a=[]
acc=0
for i in range(0, end - begin + 4):
    a.append(acc + begin)
    if (i%4 == 0):
        acc = acc + 2
    elif (i%4 == 1):
        acc = acc + 1
    elif (i%4 == 2):
        acc = acc - 2
    else:
        acc = acc + 3
a.append(acc + begin)
while True:
    if a[-1] > end:
        a.pop()
    else:
        break

print(a)
