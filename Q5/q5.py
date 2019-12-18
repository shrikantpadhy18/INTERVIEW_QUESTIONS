class Node:
    
    def __init__(self, data):
        self.data=data
        self.next=None

ori=[]

list=Node(int(input("enter data")))
list.next=None
obj=Node(int(input("enter data")))
obj.next=None
list.next=obj
while(int(input("wants to proceed click 1 else click 0"))==1):
    obj=Node(int(input("enter data")))
    obj.next=None
    ptr=list
    while(ptr.next!=None):
        ptr=ptr.next
    ptr.next=obj
    
    


str=list
count=0
while(str!=None):
    ori.append(str.data)
    str=str.next
    count+=1
print(ori)

if ori==ori[::-1]:
    print("True")
else:
    print("False")

