file = open(r'C:/Users/Professional/Downloads/vvod1.txt', 'r')
filee = open(r'C:/Users/Professional/Downloads/vivod1.txt', 'w+', encoding='UTF-8')

A1 = file.readline(1)
A2 = file.readline(1)
A3 = file.readline(1)
A4 = file.readline(1)
A5 = file.readline(1)
A6 = file.readline(1)
A7 = file.readline(1)
A8 = file.readline(1)
A9 = file.readline(1)

n1 = [int(x) for x in A1]
n2 = [int(x) for x in A2]
n3 = [int(x) for x in A3]
n4 = [int(x) for x in A4]
n5 = [int(x) for x in A5]
n6 = [int(x) for x in A6]
n7 = [int(x) for x in A7]
n8 = [int(x) for x in A8]
n9 = [int(x) for x in A9]

file.close()
file = open(r'C:/Users/Professional/Downloads/vvod1.txt', 'r')

R = file.readlines()

e1 = [n1,n2,n3]
e2 = [n4,n5,n6]
e3 = [n7,n8,n9]

print(e1)
print(e2)
print(e3)

str1 = n1+n2+n3
str2 = n4+n5+n6
str3 = n7+n8+n9

st1 = n1+n4+n7
st2 = n2+n5+n8
st3 = n3+n6+n9

d1 = n1+n5+n9
d2 = n7+n5+n3

if (str1 == str2) and (str3 == str1) and (str2==str3) and (str1==st1) and (st1==st2) and (st3==st2) and (st3==d1) and (d1==d2):
    print(" Матрица явяется магическим квадратом")
    filee.write('\n')
    filee.write(str("Матрица явяется магическим квадратом"))
    filee.close()
            
else:
    print("Матрица не явяется магическим квадратом")
    filee.write('\n')
    filee.write(str("Матрица не явяется магическим квадратом"))
    filee.close()
