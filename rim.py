#Метод, переводящий число в римскую систему счисления

def cache_decorator(func):
    cache = {}
    def wrapper(self):
        if self.num in cache:
            print("Берем число из кэша...")
            self.solution = cache[self.num]
        else:
            print("Вычисляем число...")
            result = func(self)
            cache[self.num] = result
            self.solution = result
        return self.solution
    return wrapper

class Class:
    def __init__(self, num):
        self.num = num
        self.solution = ""

    @cache_decorator
    def intToRoman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        num = self.num
        roman = ""
        i = 0
        while num > 0:
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
       	    i += 1
        return roman

    def __str__(self):
        return f"Число {self.num} в римской системе счисления равно {self.solution}"
