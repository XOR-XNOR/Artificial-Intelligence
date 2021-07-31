class DFS:
    def __init__(self,start,stop,file):
        self.start = start
        self.stop = stop
        self.file = file

        self.map = {}
        with open(self.file) as newfile:
            for line in newfile:
                a = line.split()
                key = a[0]
                values = a[1:]
                self.map[key] = values

    def dfs(self):
        stack = []
        stack.append((self.start,[]))
        visited = list()

        while stack:
            currentState, step = stack.pop()
            if currentState in visited:
                continue
            if currentState==self.stop:
                return step+[currentState]

            visited.append(currentState)
            for successor in self.map[currentState]:
                stack.append((successor, step+[currentState]))


input = DFS('D','H','search.txt')
output = input.dfs()
print(output)

