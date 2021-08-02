class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ''
        if len(palindrome)==2:
            if palindrome[0]!=palindrome[1]:
                return ''
            elif palindrome[0]=='a':
                return 'ab'
            else:
                return 'a'+palindrome[1]
        is_odd = False
        if len(palindrome)%2:
            is_odd = True
        for i in range(len(palindrome)):
            if palindrome[i]!='a':
                if (is_odd and i!=len(palindrome)//2) or not is_odd:
                    result = palindrome[:i]+'a'
                    if i+1<len(palindrome):
                        result += palindrome[i+1:]
                    return result
        return palindrome[:-1]+'b'