class Data:
    def __init__(self, value):
        self.value = value
        
    def __abs__(self):
        return self.value * 10
my_value = Data(4.2)
print(abs(my_value))