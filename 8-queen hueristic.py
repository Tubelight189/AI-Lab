def heuristic(state):
    h=0
    for i in range(len(state)):
        for j in range(i+1,len(state)):
            if abs(state[i] - state[j]) == abs(j - i):
                h+=1
    return h;

def generate_neighbour(state):
    neighbours = []

    for col in range(len(state)):
        for row in range(len(state)):
            if row!=state[col]:
                new_state=state.copy()
                new_state[col]=row
                neighbours.append(new_state)
    # print(neighbours)
    return neighbours
def hill_climbing(initial_state):
    current=initial_state
    while True:
        neighbours=generate_neighbour(current)
        best_neighbour=min(neighbours,key=heuristic)
        if best_neighbour > current:
            print("Local Minimum Detected")
            return current

        elif best_neighbour== current:
            print("Plateau Detected")
            return current

        current=best_neighbour
state = [0,1,3,2]
print((hill_climbing(state)))
state = [0,4,7,5,7,2,6,3]
print((hill_climbing(state)))
