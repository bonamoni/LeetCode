class Solution:
    def trap(self, height: List[int]) -> int:
        l=w=0
        r=len(height)-1
        lm=height[0]
        rm=height[len(height)-1]
        while l<r:
            if height[l]<height[r]:
                if height[l]>lm:
                    lm=height[l]
                else:
                    w+=lm-height[l]
                l+=1
            else:
                if height[r]>rm:
                    rm=height[r]
                else:
                    w+=rm-height[r]
                r-=1
        return w
        
        