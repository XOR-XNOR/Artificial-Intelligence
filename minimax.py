import math

class MINIMAX:
    def __init__(self,node,text):
        self.node = node
        self.text = text

        self.map = {}
        with open(text) as file:
            for line in file:
                a = line.split()
                key = a[0]
                value = a[1:]
                self.map[key] = value

    def minimax(self):
        if 'max_agent' in self.map.get(self.node):
            return self.max_value(self.node)
        if 'min_agent' in self.map.get(self.node):
            return self.min_value(self.node)
        if 'terminal' in self.map.get(self.node):
            return int(self.map[self.node][1])

    def max_value(self,state):
        if 'terminal' in self.map.get(state):
            return int(self.map[state][1])
        value = -math.inf
        for node in self.map[state][1:]:
            value = max(value, self.min_value(node))
        return value

    def min_value(self,state):
        if 'terminal' in self.map.get(state):
            return int(self.map[state][1])
        value = math.inf
        for node in self.map[state][1]:
            value = min(value, self.max_value(node))
        return value


input = MINIMAX('A','adversarial.txt')
output = input.minimax()
print(output)