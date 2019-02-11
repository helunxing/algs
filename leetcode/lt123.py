class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices or len(prices)==1:
            return 0
        
        ans=0
        
        dp_once=[0]*len(prices)
        dp_once_max=[0]*len(prices)
        
        provice_min=[0]*len(prices)
        provice_min[len(prices)-1]=prices[len(prices)-1]
        for i in range(len(prices)-2,-1,-1):
            provice_min[i]=provice_min[i+1] if provice_min[i+1]<prices[i] else prices[i]
        
        later_min=prices[0]
        for i in range(1,len(prices)):
            dp_once[i]=prices[i]-later_min
            if prices[i]<later_min:
                later_min=prices[i]    
            dp_once_max[i]=dp_once_max[i-1] if dp_once_max[i-1]>dp_once[i] else dp_once[i]
        
        for i in range(2,len(prices)):
            dp=prices[i]-provice_min[i-1]+dp_once_max[i-2]
            ans = dp if dp>ans else ans
        
        return ans
