class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        summ=0
        product=1

        
        while n:
            digit=n%10

            summ += digit
            product *= digit

            n=n//10

        divisor= summ + product
        return temp % divisor == 0