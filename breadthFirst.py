class BFS:
    def __init__(self,start,stop,text):
        self.start = start
        self.stop = stop
        self.text = text

        self.map = {}
        with open(text) as newfile:
            for line in newfile:
                a = line.split()
                key = a[0]
                value = a[1:]
                self.map[key] = value

    def bfs(self):
        queue = []
        queue.append((self.start, []))
        visited = list()

        while queue:
            currentState, step = queue.pop(0)
            if currentState in visited:
                continue
            if currentState == self.stop:
                return step+[currentState]

            visited.append(currentState)
            for successor in self.map[currentState]:
                queue.append((successor, step+[currentState]))

input = BFS('D','H','search.txt')
output = input.bfs()
print(output)