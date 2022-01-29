#Student Name: Khushbu Oza , Id:20CS041
'''Dictionary'''
#a.Write a Python script to check whether a given key already exists in a dictionary.
def Merge(Student1,Teacher) :
    return (Teacher.update(Student1))
Student1 = {   #initializing dictionary
    'Name': 'Khushbu Oza',
    'Id': '20CS041',
    'Age': '18'
}
print(Student1)  #printing dictionary
print('Name' in Student1)  #checks if Name key exists in the dictionary or not
print('Id' in Student1)   #checks if Id key exists in the dictionary or not
print('Age' in Student1)   #checks if Age key exists in the dictionary or not

#b.Write a Python script to merge two Python dictionaries.
Teacher = {
    'fn': 'Trusha Patel',
    'Address': 'Changa'
}
print(Merge(Student1, Teacher))  #merges two dictionarys
print(Teacher)

#c.Write a Python program to sum all the items in a dictionary.
d1 ={
     'a': 100,
     'b': 250
}
print(sum(d1.values()))  #sums the values of dictionary

#d.Write a Python script to add a key to a dictionary.
d1['c'] = 123  #To add a key in the existing dictionary
print(d1)

#e.Write a Python script to concatenate following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3) : dic4.update(d)   #concatenates all the dictionarys into a new dictionary
print(dic4)

'''Tuple'''
#a.Write a Python program to create a tuple with different data types.
difDatatype = ('Hello', 10, 15.456)   #tuple containing multiple datatypes
#print(difDatatype)

#b.Write a Python program to create a tuple with numbers and print one item.
numbers = (1, 2, 3, 4, 5)
one = numbers[0]
print(one)

#c.Write a Python program to add an item in a tuple.
numbers = numbers + (6,)  #adds a new item at the end of the tuple
print(numbers)

#d.Write a Python program to convert a tuple to a string.
def  convertToString(tuple) :   #logic to convert tuple to string
    #intializing an empty string
    str = ''
    for item in tuple:
        str = str + item
    return str


tuple = ('a','b','c','d','e')   #defining tuple
str = convertToString(tuple)
print(str)

#e.Write a Python program to find the length of a tuple.
print(len(tuple))  #finds length of tuple

'''Set'''
#a.Write a Python program to add member(s) in a set and clear a set.
set1 = {'hello', 'pyhton'}  #defining set
print(set1)   #prints set
set1.add('program')  #adds a value
print(set1)
set1.clear()  #clears a set
print(set1)

#b.Write a Python program to remove an item from a set if it is present in the set.
phone = {'samsung' , 'iphone' , 'realme'}
print(phone)
phone.remove('iphone')  #removes an item from set
print(phone)

#c.Write a Python program to create an intersection, Union, difference of sets.
n1 = {1, 2, 3}
n2 = {3, 4, 5}
#print(vegetables)
print(n1.union(n2))  #prints union of sets
print(n1.intersection(n2))  #prints intersection of sets
print(n1.difference(n2))  #prints differences of sets

#d.Write a Python program to find maximum and the minimum value in a set.
set = { 10 ,63 , 7483 , 128}
print(max(set))  #prints maximum value from set
print(min(set))  #prints minimum value from set

#e.Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
##for list:
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))  #prints the most frequent element to occur in the list

#for tuple:
def countX(tup, x):
    count = 0
    for ele in tup:
        if (ele == x):
            count = count + 1
    return count

tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8
print(countX(tup, enq))  #prints the occurance of the given value
print(countX(tup, enq1))
print(countX(tup, enq2))
