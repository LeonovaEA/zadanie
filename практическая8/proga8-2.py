
import math
def Zadanie82(a, b):
    W = 0
    for i in range(2):
        W += pow((a[i]-b[i]),2)
    return W
 
Identify=['X','Y','Z','T']
arr=[]
print("Введите кординаты точек:")
for i in range(4):
    b=[]
    print("Кординаты точки:",Identify[i])
    for j in range(2):
        b.append(int(input()))
    arr.append(b)
 
flag = True
for i in range(2):
    for j in range(i+1, 4):
        dist = distance(arr[i],arr[j])
        if flag or max_dist > dist:
            M1=i
            M2=j
            max_dist = dist 
            flag = False
 
print(f'Максимальная дистанция между точками {Identify[m1]} и {Identify[m2]}')
print(f'Размер дистанции= {max_dist**0.5:.3f}')
