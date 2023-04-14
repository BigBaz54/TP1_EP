import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import stairs

import ex1
import ex2

import numpy as np


def cmtc(P0, M, T0):
    """
    P0 : initial state probability vector
    M : transition matrix
    T0 : observation duration
    """
    n = len(P0)

    # X tracks the evolution of the state of the system
    X = []
    # t tracks the time spent in each state
    t = [0]

    # Compute Q
    Q = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i!=j:
                Q[i, j] = M[i, j] / (- M[i, i])

    # States are integers
    states = range(n)

    # Initial state
    state = random.choices(states, P0)[0]
    X.append(state)

    # Initial time
    t.append(ex2.var_alea_exp(-M[state, state]))

    while (t[-1] < T0):
        # Compute the next state
        p = [(i, Q[state, i]) for i in range(n)]
        state = ex1.var_alea(p)
        X.append(state)
    
        # Compute the time spent in the new state
        t.append(t[-1] + ex2.var_alea_exp(-M[state, state]))
    
    stairs(X, t)
    print("X: ", X)
    print("t: ", t)
    plt.title("Evolution of the state of the system")
    plt.xlabel("Time")
    plt.ylabel("State")
    plt.show()

if __name__ == "__main__":
    P0 = [0.4, 0.3, 0.3]
    M = np.array([[-0.2, 0.1, 0.1], [0.1, -0.2, 0.1], [0.1, 0.1, -0.2]])
    T0 = 100
    # cmtc(P0, M, T0)

    P0 = [1, 0]
    M = np.array([[-1000, 1000], [2000, -2000]])
    T0 = 5
    cmtc(P0, M, T0)