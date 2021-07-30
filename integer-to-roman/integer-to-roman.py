class Solution:        
    def findClosest(self, x, num_to_roman):
        if x==0:
            return ''
        result = ''
        if x in num_to_roman:
            return num_to_roman[x]
        current_min = float('inf')
        for k, v in num_to_roman.items():
            if abs(k-x)<abs(x-current_min) and k<x and len(v)==1 and 3*k>=x:
                current_min = k
                result = v
        if x-current_min<=3:
            return result+(x-current_min)*'I'
        if x-current_min<=30:
            return result+(x-current_min)//10*'X'
        if x-current_min<=300:
            return result+(x-current_min)//100*'C'
        if x-current_min<=3000:
            return result+(x-current_min)//1000*'M'
        return result
        
    def intToRoman(self, num: int) -> str:
        num_to_roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
        i = 1
        result = ''
        while num//(10**(i-1))>0:
            close = self.findClosest(num%(10**i), num_to_roman)
            result += close[::-1]
            num -= num%(10**i)
            i += 1
        return result[::-1]