from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] 
        dq = deque() #init empty deque
        dq.append(0) #adds and inits the deque first 
        for i in range(len(nums)):
            while dq and (nums[dq[-1]] <= nums[i]):
                dq.pop()
            dq.append(i)

            if dq[0] <= i - k: #front index fell outside the window 
                dq.popleft() 

            if i >= k - 1: #window is complete, record the answer 
                res.append(nums[dq[0]])
        return res 
        
#basically when the rightmost is less than or equal to the next number
#we are just going to rip that number out and replace that with the incoming
#number. otherwise, if the rightmost is more than or equal, just append the 
#index of that index. 

#deque: [2]
#nums: [1]


#keeping a deque of indices (deque = doubly edged queue where you can pop from
#both sides of the queue. 
#maintain an invariant that the values at those indices are in decreasing order
#from front to back