#Creating stack class
class Stack:
    #Initializing self method
    def __init__(self):
        self.stack = []

    #Creating function named push to perform push operation on stack
    def push(self, value):
        self.stack.append(value)

    #Creating function named pop to remove top most element in stack
    def pop(self):
        if self.check_is_Empty():
            print("Stack is Empty!!\n")
        else:
            self.stack.pop()

    #Creating funtion to check if stack is empty or not
    def check_is_Empty(self):
        return self.stack == []

    #Creating function traversal to traverse through whole stack
    def traversal(self):
        print(f' stack =  {self.stack[::-1]}')


#Creating object of class stack
s = Stack()

#providing multiple choices to the user
print("Enter from below option : \n")
while True:
    print("1. push")
    print("2. pop")
    print("3. traversal")
    print("4. check is Empty")
    print("5. Quit.")

    option = int(input())

    if option == 1:
        print("Enter element : ")
        element = int(input())
        s.push(element)
    elif option == 2:
        s.pop()
    elif option == 3:
        s.traversal()
    elif option == 4:
        status = s.check_is_Empty()
        print(f'Empty Status : {status}\n')
    elif option == 5:
        break
    else:
        print("Enter proper choice!!\n")
        continue
