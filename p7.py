n = int(input()) #takes int input

while n: #loop executes until n
    n=n-1 #decreasing n by one
    str=input() #taking string input
    half_string = len(str) // 2 #dividing string into two parts

    if(len(str)%2==0): #executes when division is even
        if sorted(str[half_string:]) == sorted(str[:half_string]): #checks if sorted first half of string is equal to sorted second half of string or not
            print('YES') #if condition is true prints YES
        else:
            print('NO') #if condition is false prints NO

    else:  #executes when division is odd
        if sorted(str[:half_string]) == sorted(str[half_string + 1:]): ##checks if sorted second half of string is equal to the sorted first half of string after it's just next element
            print('YES') #if condition is true prints YES
        else:
            print('NO') #if condition is false prints NO