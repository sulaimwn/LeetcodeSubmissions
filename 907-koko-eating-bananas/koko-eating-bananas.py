class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #basically do a binary search of 1 -> max(piles)
        #when ur selecting an index u calculate how many hours itd take  . if its too high move ur k value search area lower and vice versa

        l = 1
        r = max(piles)

        res = r #our final k value
        #by default we set it to max(piles)
        # a value thats guaranteed legal but possibly inefficient
        # min is used later to move it lower to possible k values


        #binary search
        while l<=r:
            k=(l+r) //2 # floor div
            hours = 0

            #calculate hours
            for p in piles:
                hours+=math.ceil(p/k) #ceiling div piles[p] by assumed k 
                # for example k=4 in 11 would take   2.75--> 3 hrs  .  3 hrs at that index
            
            if hours <= h: #<= bcs even if it hits h=8 . doesnt mean its smallest k
            

                res=min(res,k) #grabs the smallest possible k after moving the bounds 
                
                #hours is less than h so we move the search area down . move right bound down
                r=k-1
            else:
                l=k+1
                #hours is greater than h. so we need to move our l value up
        return res