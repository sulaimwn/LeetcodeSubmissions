class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1

        possiblevalues=[]
        while l<r:
            lv=height[l]
            rv=height[r]
            
            width=r-l

            curh=min(lv,rv)

            possiblevalues.append(width*curh)

            if lv<rv:
                l+=1
            elif rv<lv:
                r-=1
            else:
                l+=1
            
        return max(possiblevalues)
