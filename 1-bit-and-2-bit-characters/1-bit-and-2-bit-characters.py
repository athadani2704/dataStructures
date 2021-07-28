class Solution:
    def isValidTwo(self, arr, i):
        if i==0:
            return True if arr[i]==0 else False
        if arr[i]==0:
            return True
        if i==1:
            return True if arr[i-1]==1 else False
        if arr[i-1]==0:
            return False
        else:
            return self.isValidTwo(arr, i-2)
        
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)==1 or bits[-2]==0:
            return True
        if len(bits)==2:
            return True if bits[0]==0 else False
        return self.isValidTwo(bits, len(bits)-2)