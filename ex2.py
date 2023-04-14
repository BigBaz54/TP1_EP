import math
import random

def var_alea_exp(lam):
    x = random.random()
    return -1/lam * math.log(x)

def question_a():
    li = []
    lam = 20
    for i in range(10000):
        li.append(var_alea_exp(lam))
        if i==99:
            print("\nAverage of the first 100 values: ", sum(li)/100)
            print("Variance of the first 100 values: ", sum([x**2 for x in li])/100 - (sum(li)/100)**2)
        if i==999:
            print("\nAverage of the first 1000 values: ", sum(li)/1000)
            print("Variance of the first 1000 values: ", sum([x**2 for x in li])/1000 - (sum(li)/1000)**2)
        if i==9999:
            print("\nAverage of the first 10000 values: ", sum(li)/10000)
            print("Variance of the first 10000 values: ", sum([x**2 for x in li])/10000 - (sum(li)/10000)**2)
    print("\nAverage of the 10000 values: ", sum(li)/10000)
    print("Variance of the 10000 values: ", sum([x**2 for x in li])/10000 - (sum(li)/10000)**2)
    print("\nTheoretical average: ", 1/lam)
    print("Theoretical variance: ", 1/lam**2)
    print()

def question_b():
    qu1 = 0
    qu2 = 0
    lam = 1/15
    for _ in range(100000):
        x = var_alea_exp(lam)
        if x < 10:
            qu1 += 1
        if x < 15 and x > 5:
            qu2 += 1
    print("Probability of a value < 10: ", qu1/100000)
    print("Probability of a value < 15 and > 5: ", qu2/100000)
        

if __name__ == "__main__":
    question_a()
    question_b()


