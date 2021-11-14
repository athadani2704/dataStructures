# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        r, c = rand7(), rand7()
        while (7*(r-1)+c)>40:
            r, c = rand7(), rand7()
        return 1+(7*(r-1)+c)%10