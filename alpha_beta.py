import math


class ALPHABETA:
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

    def alpha_beta(self):
        alpha = -math.inf
        beta = math.inf
        if 'max_agent' in self.map.get(self.node):
            return self.max_agent(self.node,alpha,beta)
        if 'min_agent' in self.map.get(self.node):
            return self.min_agent(self.node,alpha,beta)
        if 'terminal' in self.map.get(self.node):
            return int(self.map[self.node][1])

    def max_agent(self,state,alpha,beta):
        if 'terminal' in self.map.get(state):
            return int(self.map[state][1])
        value = -math.inf
        for node in self.map[state][1:]:
            value = max(value,self.min_agent(node,alpha,beta))
            if value >= beta:
                return value
            alpha = max(value,alpha)
        return value

    def min_agent(self,state,alpha,beta):
        if 'terminal' in self.map.get(state):
            return int(self.map[state][1])
        value = math.inf
        for node in self.map[state][1]:
            value = min(value,self.max_agent(node,alpha,beta))
            if value <= alpha:
                return value
            beta = min(value,beta)
        return value


input = ALPHABETA('A','adversarial.txt')
output = input.alpha_beta()
print(output)
