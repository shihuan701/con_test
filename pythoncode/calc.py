class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b==0:
            return '除数不能为0'
        else:
             c = a / b
             return round(c,2)
