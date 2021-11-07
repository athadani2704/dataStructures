class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        elif num1=="1" or num2=="1":
            return num2 if num1=="1" else num1
        maps = {i:ord(i)-48 for i in "0123456789"}
        invert = {i:chr(i+48) for i in range(10)}
        a = b = 0
        for val in num1:
            a = a*10+maps[val]
        for val in num2:
            b = b*10+maps[val]
        prod = a*b
        result = []
        while prod:
            prod, r = divmod(prod, 10)
            result.append(invert[r])
        return "".join(result[::-1])