pos=-1
def sort(list):
    for i in range(len(list)-1,0,-1):
        minpos=i
        for j in range(i):
            if list[j]>list[minpos]:
                minpos=j
        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp
        print(list)


def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
def match(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False
def found(list,n):
    for i in range(len(list)):
            if list[i]==n:
                globals()['pos']=i
                return True


    return False

list=[12,3,6,76,91,1]
sort(list)
print(list)
n=6
if search(list,n):
    print('found at:',pos)
else:
    print('not found')

n=76
if match(list,n):
    print('match at possision:',pos)
else:
    print('not match')

n=91
if found(list,n):
    print('found at pos:',pos)
else:
    print('not found')
print('hello')
print('changes')





