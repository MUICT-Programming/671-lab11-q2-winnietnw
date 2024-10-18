# YOUR CODE HERE
def summation(lst1,lst2,n):
    update_list=[]
    for i in range(n):
        update_list.append([lst1[i]+lst2[i]])
    return update_list
def find_min_max(lst):
    return (min(lst),max(lst))


x=[]
y=[]
n=int(input())
for i in range(n):
    x.append(int(input()))
for i in range(n):
    y.append(int(input()))
result= summation(x,y,n)
print(result)
minmax=find_min_max(result)
print(minmax)
