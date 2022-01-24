N = int(input()) #takes input in int
arr = list(set(map(int, input().split()))) #takes input as array
for i in range(0 , N): #executes until i is in range of 0 to N
     print(sorted(arr)[-2]) #sorts the array and return the second last element
     break #stops for loop
