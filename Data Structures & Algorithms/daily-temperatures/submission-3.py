class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
    # the objective is to result an array, where each index in the array represents the number of days in the future when a warmer tempearture will appear for the ith day
    # when there is no warmer day in the future, then the index will be 0 instead 
    # the use of a stack in this case: when to append to the stack, when to pop from teh stack? 
    #whats the point of having a stack in this case then? 

    #first, lets try the brute force approach -> we are going to every index, and then its a two pointer approach 

        stack = []
        result = [0] * len(temperatures)
        for index in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[index]: 
                j = stack.pop()
                result[j] = index - j
            stack.append(index)
        return result 
                
            