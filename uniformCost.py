from queue import PriorityQueue

class UCS:
    def __init__(self,start,stop,text):
        self.start = start
        self.stop = stop
        self.text = text

        self.map = {}
        with open(text) as newfile:
            for line in newfile:
                node_a,node_b,value = line.split()
                self.map.setdefault(node_a,[]).append((node_b,value))
                self.map.setdefault(node_b,[]).append((node_a,value))

    def ucs(self):
        queue = PriorityQueue()
        queue.put((0,self.start,[]))
        visited = list()

        while queue:
            cost, currentState, step = queue.get()
            if currentState in visited:
                continue
            if currentState==self.stop:
                return (step+[currentState],cost)

            visited.append(currentState)
            for successor, newcost in self.map[currentState]:
                queue.put((cost+int(newcost),successor,step+[currentState]))


input = UCS('Arad','Bucharest','costSearch.txt')
output = input.ucs()
print(output)