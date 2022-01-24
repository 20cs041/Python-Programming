N = input() #takes input

room = list(map(int ,input().split())) #takes input of list
a=set() #creating empty set a
b=set() #creating empty set b

for i in room: #executes until i is in range of room
    if i not in a: #checks if i is in a or not
        a.add(i) #addds element in a
        b.add(i) #addds element in b
    else:
        b.discard(i) #eliminates repeated elements
b = list(b) #converting b to list
print(b[0]) #prints the element on 0 index

        
