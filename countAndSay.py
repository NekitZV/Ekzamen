#Метод, выполняющий операцию «Посчитай и скажи» num раз по принципу: countAndSay(1) = "1"


class Class:
    def __init__(self, num):
        self.num = num
        self.solution = ""

    def countAndSay(self):
        result = "1"
        for _ in range(1, self.num):
            result = self._say(result)
        self.solution = result

    def _say(self, s):
        result = ""
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result += str(count) + s[i - 1]
                count = 1
        result += str(count) + s[-1]  # не забываем добавить последнюю группу
        return result

    def __str__(self):
        return f"Выполнение операции {self.num} раз дает ответ {self.solution}"
