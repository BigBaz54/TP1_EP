import random


def var_alea(P):
    """ P est une liste contenant des couples (valeur, proba) """
    n = len(P)
    r=random.random()
    for i in range(n):
        if r<P[i][1]:
            return P[i][0]
        else:
            r=r-P[i][1]

if __name__ == "__main__":
    P = [("64 octets", 0.7), ("128 octets", 0.1), ("512 octets", 0.2)]
    stats = {"64 octets": 0, "128 octets": 0, "512 octets": 0}
    for i in range(100000):
        stats[var_alea(P)] += 1
        if i == 99:
            print("\nStatistiques sur 100 tirages:\n", stats)
        if i == 999:
            print("\nStatistiques sur 1000 tirages:\n", stats)
        if i == 9999:
            print("\nStatistiques sur 10000 tirages:\n", stats)
    print("\nStatistiques sur 100000 tirages:\n", stats)
