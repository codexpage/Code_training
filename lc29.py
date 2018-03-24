#每次减一个太慢了，TLE
#采用每次翻倍的减法，收敛更快
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==0:
            return 0
        ispositive = (dividend<0) == (divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        quotient=0
        while dividend>=divisor:
            d=divisor
            i=1
            while dividend>=d:
                dividend-=(d)
                quotient+=i
                i <<= 1
                d <<= 1
        quotient = quotient if ispositive else -quotient
        return min(max(-2147483648, quotient), 2147483647)
            
        
        