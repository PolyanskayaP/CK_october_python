class RealString:
    def __init__(self, word):
        self.word = word 
    def __len__(self):
        return len(self.word)
    def __cmp__(self, b): #для == и !=
        if len(self.word) > len(b):
            return -1
        elif len(self.word) < len(b):   
            return 1
        else:
            return 0
    def __lt__(self, b):
        return len(self.word) < len(b) 
    def __gt__(self, b):
        return len(self.word) > len(b)
    def __le__(self, b):
        return len(self.word) <= len(b)
    def __ge__(self, b):
        return len(self.word) >= len(b)   
    def __eq__(self, b):
        return len(self.word) == len(b) 
'''    def __ne__(self, b):
        return len(self.word) != len(b)'''

    
a = RealString('привет')
b = RealString('ййй')

print(a == b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)
print(a > 'яяя')
print(b == 'aaa')
