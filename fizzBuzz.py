class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

n = int(input())
list_result = Solution().fizzBuzz(n)
list_to_string = "["
index = 0
for item in list_result:
    if index == len(list_result) - 1:
        list_to_string += '"' + str(item) + '"]'
        break
    list_to_string += '"' + str(item) + '",'
    index += 1

print(list_to_string)
