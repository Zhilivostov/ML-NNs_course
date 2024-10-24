

def x_powered(x: float = 1, n: int = 1) -> float:
    accumulator = 1
    k = 0
    while k < n:
        k+=1 
        accumulator*=x

    return accumulator

#=====================================================================================================================================

def max_list(list_of_numbers: list = []) -> float:
    if len(list_of_numbers) == 0:
        pass
    max_list: float  = list_of_numbers[0]
    k: int = 0
    while k < len(list_of_numbers):
        if list_of_numbers[k] > max_list:
            max_list = list_of_numbers[k]
        k+=1
    return max_list

#=====================================================================================================================================

def n_row_pascal_triangle(n: int = 0) -> list:
    #base = [[0, 1, 0]]
    base = [0, 1, 0]
    print(base)
    for i in range(1, n):
        new_base = []
        b = len(base)
        for j in range(b):
            if j != b:
                new_base.append(base[j-1]+base[j])
        new_base.append(0)
        print(new_base)
        base = new_base

    return base

#=====================================================================================================================================

def sort_list(lst: list = None) -> list:
    k: int = len(lst)
    print(k)
    if k == 0 or k == 1:
        return lst
    n: int = 0
    state: bool = False
    new_go: bool = False
    while state == False:
        if lst[n+1] <= lst[n]:
            n+=1
        else:
            t = lst[n+1]
            lst[n+1] = lst[n]
            lst[n] = t
            n+=1
            new_go = True
        if n >= k - 1:
            if new_go == True:
                n = 0
                new_go = False
            else:
                state = True
    return lst

#=====================================================================================================================================

class NeuralNetwork():
    def __init__(self, weight: int = 1, nick: str = None):
        self.weight = weight
        self.dataset = []
        self.nickname = nick

    def forward(self, data: list = None) -> None:
        for i in range(len(data)):
            self.dataset.append(data[i]*self.weight)

    def backward(self, loss: float = 6e-3) -> list:
        output = []
        for i in range(len(self.dataset)):
            output.append(self.dataset[i]/loss)
        return output
                
#=====================================================================================================================================

import numpy as np

nn = NeuralNetwork(weight = 3, nick = "doggy")
#data = np.random.rand(100, 1)[0]
data = [2, 4, 8]

nn.forward(data)
#loss = np.random.rand(1)[0]
loss = 0.5

prediction = nn.backward(loss)

print(prediction)

#a = n_row_pascal_triangle(5)
#print(x_powered(2, 5))
#print(max_list(a))
#print(sort_list(a))