class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i = 0
        number1 = []
        while i < len(num1):
            number1.append(int(num1[i]))
            i = i + 1
        j = 0
        number2 = []
        while j < len(num2):
            number2.append(int(num2[j]))
            j = j + 1

        k = 0
        power1 = len(number1)-1
        sum1 = 0
        while k < len(number1):
            sum1 = sum1 + number1[k] * pow(10, power1)
            k = k + 1
            power1 = power1 - 1

        h = 0
        power2 = len(number2)-1
        sum2 = 0
        while h < len(number2):
            sum2 = sum2 + number2[h] * pow(10, power2)
            h = h + 1
            power2 = power2 - 1
        return str(sum1 * sum2)

New = Solution()
New.multiply("2","3")