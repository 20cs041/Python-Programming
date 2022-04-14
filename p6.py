N = int(input()) #takes int input
dcn = {} #creating empty dictionary
list = [] #creating empty list
for i in range(N): #loop gets implemented in the range from 0 to N
    word = input() #takes string input
    list.append(word) #adds the word to list
    if word in dcn: #checks if the added word is already in dictionary or not
        dcn[word]+=1 #if word is alreay in dictionary then increments the value of word
    else:
        dcn[word]=1 #if word is not in dictionary then sets the word's value to one
print(len(dcn)) #prints length of dictionary
print(*dcn.values()) #prints values of words