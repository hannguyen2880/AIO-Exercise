class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0
    
    def is_full(self):
        return len(self.__stack) == self.__capacity
    
    def push(self, value):
        if self.is_full():
            raise Exception("Overflow")
        self.__stack.append(value)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.__stack.pop()
    
    def top(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.__stack[-1]