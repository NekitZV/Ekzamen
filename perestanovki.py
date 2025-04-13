#Метод обработки массива nums так, чтобы массив solution содержал все возможные перестановки

class Class:
    def __init__(self, nums):
        self.nums = nums
        self.solution = []

    def permute(self):
        def generate(current, remaining):
            if not remaining:
                self.solution.append(current)
                return
            for i in range(len(remaining)):
                generate(current + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        self.solution = []
        generate([], self.nums)

    def __str__(self):
        return f"Для массива {self.nums} будут такие перестановки: {self.solution}"

    def mediana(self):
        # простая сортировка (вставками)
        nums = self.nums[:]
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

        n = len(nums)
        if n % 2 == 1:
            return nums[n // 2]
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2
