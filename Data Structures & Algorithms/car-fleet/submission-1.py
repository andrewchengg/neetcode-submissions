class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = [] 
        for i in range(len(position)):
            lst.append((position[i],speed[i]))
        lst.sort(key=lambda x: x[0], reverse=True)
        #now we have a list of tuples, where the first element is the position
        stack = []
        for j in range(len(position)):
            pos = lst[j][0]
            spd = lst[j][1]
            time = (target - pos) / spd
            if j == 0:
                stack.append(time)
            else:
                curr = stack[-1] 
                if time > curr:
                    stack.append(time)
        return len(stack)

        
            