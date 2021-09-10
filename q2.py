from ABS import Stack

def is_operator(ent) -> bool:
    """ Returns boolean for if entry is a valid operator"""
    if (ent == '+' or ent == '-' or ent == '*' or ent == "/"):
        return True
    return False

def do_operation(s: Stack, op):
    """ Takes the stack and the operator and performs the operation"""
    r = s.pop()
    l = s.pop()
    if op == '+':
        s.push(l + r)
    elif op == '-':
        s.push(l - r)
    elif op == '*':
        s.push(l * r)
    else:
        s.push(l // r)

def next_entry(file) -> str:
    """ Rips the next entry from the text file"""
    out = ""
    while True:
        ent = file.read(1)
        if (ent == " " or ent == ""):
            break
        out += ent
    return out

def Q2():
    """ Loops until it reaches EOF, where the next character returned
        from next_entry will be an empty string. Breaking the loop as
        the RPN string is finished. The result is a Stack with one entry. """
    f = open("q2_in.txt", "r")
    exp_stack = Stack()
    while True:
        print(exp_stack)
        c = next_entry(f)
        if c == "":
            break
        if not is_operator(c):
            exp_stack.push(int(c))
        else:
            do_operation(exp_stack, c)
    f.close()
    ans = open("q2_out.txt", "w")
    ans.write(str(exp_stack.pop()))
    ans.close()
    
Q2()