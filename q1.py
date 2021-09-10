from ABS import Stack

def lin_fib(k):
    """ Linear time algorithm for fibonacci sequence"""
    if k == 1:
        return 1, 0 # f0 = 0 for Lucas function to calculate f(n)
    else:
        a, b = lin_fib(k - 1)
        return a + b, a

def kth_Lucas(k):
    """ Uses recursive linear fibonnaci sequence by taking n - 1 and n + 1 of fib sequence to calculate
        the next lucas number in the sequence"""
    if k == 1:
        return 2
    elif k == 2:
        return 1
    else:
        return lin_fib(k - 2)[0] + lin_fib(k)[0]

def Q1():
    f = open("q1_in.txt", "r")
    raw = Stack()
    iter = int(f.readline().strip("\n"))
    for i in range(iter):
        raw.push(int(f.readline().strip("\n")))
    f.close()

    ans = open("q1_out.txt", "w")
    for i in range(iter):
        ans.write(f"{kth_Lucas(raw.pop())}\n")
    ans.close()

Q1()