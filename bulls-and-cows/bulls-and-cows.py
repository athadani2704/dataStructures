class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sec, bulls, cows = {}, 0, 0
        for val in secret:
            sec[val] = sec.get(val, 0)+1
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls += 1
                sec[secret[i]] -= 1
        for i in range(len(secret)):
            if secret[i]!=guess[i] and guess[i] in sec and sec[guess[i]]>0:
                cows += 1
                sec[guess[i]] -= 1
        return str(bulls)+"A"+str(cows)+"B"
        
# - store freq of digits in sec and gu
# - create empty dicts bulls and cows
# - loop through each digit of secret
#     - check if the digit is same in both secret and guess
#         - if yes then 
#             - increment bulls[digit] by 1
#             - decrement sec[digit] by 1
#         - otherwise check if digit in guess is present in sec and sec[digit]>0
#             - if yes then
#                 - increment cows[digit] by 1
#                 - decrement sec[digit] by 1
            