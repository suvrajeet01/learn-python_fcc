def iterative_funcions(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

print(iterative_funcions(5))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp

print(recur_factorial(5))


def recur_fact(m):
    if m == 1: return m
    else: return m * recur_fact(m-1)

print(recur_fact(5))














def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter+pocket)
        
print(permute("ABC", ""))




from math import factorial

def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i-1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i-1] > str[q]:
                q += 1
            temp = str[i-1]
            str[i-1] = str[q]
            str[q] = temp
s = 'abc'
s = list(s)
permutations(s)


