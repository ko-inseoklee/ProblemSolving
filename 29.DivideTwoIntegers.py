class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = True
        result = 0
        
        limit = pow(2,31) - 1
        
        if(-(limit + 1) > dividend > limit):
            return -1
        if(divisor == 0 or -(limit + 1) > divisor > limit):
            return -1
        
        if(divisor == 1):
            return dividend
        if(divisor == -1):
            if(dividend > limit + 1):
                return -(limit + 1)
            if(dividend < -limit):
                return limit
            return -dividend
        
        dend = dividend
        sor = divisor
        
        if(sor < 0):
            sor = -sor
            sign = not sign
        if(dend < 0):
            dend = -dend
            sign = not sign
            
        if(sor > dend):
            return 0
        
        a = dend
        b = sor
        
        exp = 1
        while(a >= b):
            exp += 1
            b = pow(sor, exp)
        
        exp -= 1
        b = pow(sor, exp)
        
        while(a >= sor):
            if(a >= b):
                a -= b
                result += pow(sor,exp-1)
            else:
                exp -= 1
                b = pow(sor,exp)
        
        if(sign):
            if(result > limit):
                return limit
            return result
        else:
            return -result
        