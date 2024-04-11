class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # val=0
        # l=len(digits)
        # j=l-1
        # for i in range(0,l):
        #     val+=digits[i]*(10**j)
        #     j-=1

        #Solution-2L
        # str_dig=""
        # for i in digits:
        #     str_dig += str(i)

        # return [int(i) for i in str(int(str_dig)+1)]

        #Solution-3:
        l=len(digits)-1
        if digits[l] == 9:
                while digits[l] == 9:
                    digits[l]=0
                    
                    if l == 0:
                        digits.insert(0,1)
                        l-=1
                        break
                    l-=1
                if l>=0:
                    digits[l] += 1

        else:
            digits[l] += 1

        return digits
