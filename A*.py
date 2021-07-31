from queue import PriorityQueue

class AStar:
    def __init__(self,start,stop,text1,text2):
        self.start = start
        self.stop = stop
        self.text1 = text1
        self.text2 = text2

        self.map = {}
        with open(text1) as file1:
            for line in file1:
                node_a, node_b, value = line.split()
                self.map.setdefault(node_a,[]).append((node_b,value))
                self.map.setdefault(node_b,[]).append((node_a,value))

        self.heuristic = {}
        with open(text2) as file2:
            for line in file2:
                key, value = line.split()
                self.heuristic[key] = value

    def astar(self):
        queue = PriorityQueue()
        queue.put((0,self.start,[]))
        visited = list()

        while queue:
            cost, currentState, step = queue.get()
            if cost > 0:
                cost = cost - int(self.heuristic[currentState])
            if currentState in visited:
                continue
            if currentState==self.stop:
                return (step+[currentState],cost)

            visited.append(currentState)
            for successor, newcost in self.map[currentState]:
                queue.put((cost+int(newcost)+int(self.heuristic[successor]), successor, step+[currentState]))

input = AStar('Arad','Bucharest','costSearch.txt','heuristic.txt')
output = input.astar()
print(output)