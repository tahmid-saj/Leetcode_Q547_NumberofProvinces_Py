class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                # self.stack(isConnected, visited, i)
                self.dfs(isConnected, visited, i)
                provinces += 1
        
        return provinces

    def stack(self, isConnected, visited, city):
        stk = [city]
        visited.add(city)

        while stk:
            city = stk.pop()

            for j in range(len(isConnected[city])):
                if isConnected[city][j] == 1 and j != city and j not in visited:
                    visited.add(j)
                    stk.append(j)
    
    def dfs(self, isConnected, visited, i):
        visited.add(i)

        for j in range(len(isConnected[i])):
            if i != j and isConnected[i][j] == 1 and j not in visited:
                self.dfs(isConnected, visited, j)
