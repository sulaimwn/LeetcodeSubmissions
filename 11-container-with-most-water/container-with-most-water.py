class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1

        maxArea=0
        while l<r:
            lv=height[l]
            rv=height[r]
            
            width=r-l

            curh=min(lv,rv)

            curA=width*curh
            maxArea = max(maxArea, curA)


            if lv<rv:
                l+=1
            elif rv<lv:
                r-=1
            else:
                l+=1
            
        return maxArea
