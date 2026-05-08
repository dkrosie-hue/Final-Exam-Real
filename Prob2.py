
def racman(n): ## Recursion
    if n == 0:
        return 0
    else:
        if racman(n-1) - n > 0:
            return racman(n-1) - n
        else:
            return racman(n-1) + n

def racaman(n):
    if n == 0:
        return 0
    seq = [0] #a_0 starting case
    for i in range(1, n+1):
        potential = seq[i-1] - i
        if potential > 0 and potential not in seq:
            seq.append(potential)
        else:
            seq.append(seq[i-1] + i)
    return seq[-1]

if __name__ == "__main__":
    print(racman(4))
