class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        result = False
        if not prerequisites:
            return True 
        seen: Dict[int, List[int]] = defaultdict(list) #storing the course number, and then values is the neighbors
        done = set()
        on_path = set()
        for i in range((len(prerequisites))):
            curr_course = prerequisites[i][0] 
            neighbor = prerequisites[i][1] #single value
            seen[curr_course].append(neighbor)
        #now we have an adjacency list representation of the course numbers and their neighbors 
        #we are going to do DFS on this adjacency list 


        def helper(value) -> bool: #returns true or false, helper checks if that node has a cycle 
            if value in on_path:
                return True #cycle present
            if value in done:
                return False #already checked, so no need to go through again 
            on_path.add(value)
            for neighbor in seen[value]:
                if helper(neighbor):
                    return True 
            on_path.remove(value)
            done.add(value)
            return False 
        
        for item in range(numCourses):
            if helper(item):
                return False
            
        return True 
                
        
        
        

    #array of arrays - where in one array, you must take course b first if you want to take course a 
    #numcourses is the total number of courses that you have to take 
    #return true if its possible to finish all courses, otherwise false 

    #graph problem 
    # we have nodes that have edges coming out of the, and this is directed. so the nodes with the edges coming out of them means that they must take X class in order to go to Y class. 
    # coming from example 2, we can see it as two nodes who have edges that are pointing to each other, and that is a cycle. the main case where we are not able to finish all the courses is if there is a cycle present. 
    #so first we are going to build the graph, we are going to do node, and then a list of its neighbors