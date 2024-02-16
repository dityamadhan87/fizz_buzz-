class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        hasil = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                hasil.append("FizzBuzz")
            elif i % 3 == 0:
                hasil.append("Fizz")
            elif i % 5 == 0:
                hasil.append("Buzz")
            else:
                hasil.append(str(i))
        return hasil

n = int(input())
hasil_list = Solution().fizzBuzz(n)
list_to_string = "["
index = 0
for item in hasil_list:
    if index == len(hasil_list) - 1:
        list_to_string += '"' + str(item) + '"]'
        break
    list_to_string += '"' + str(item) + '",'
    index += 1

print(list_to_string)
