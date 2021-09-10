from ABS import PriorityQueue

def find_priority(p: str) -> int:
    """ Converts employee level to priority"""
    prio_key = {"L1": 3, "L2": 2, "L3": 1}
    return prio_key[p]

def printable(printed, max) -> bool:
    """Ensures that maximum print operations has not been reached"""
    if printed > max:
        return False
    return True

def submitable(submitted, max) -> bool:
    """Ensures that maximum submit operations has not been reached"""
    if submitted > max:
        return False
    return True

def Q4():
    # Defines operations
    SUBMIT = "1"
    PRINT = "2"

    f = open("q4_in.txt", "r")
    ans = open("q4_out.txt", "w")
    max_ops = int(f.readline().strip("\n"))
    max_subs = int(f.readline().strip("\n"))
    max_prints = int(f.readline().strip("\n"))
    subs = 0
    prints = 0

    # Initialise priority queue
    requests = PriorityQueue()

    for i in range(max_ops):
        req = f.readline().strip("\n").split(" ")
        job = req[0]
        # If the operation is a valid submit, the job is enqueued 
        # into priority queue
        if job == SUBMIT and submitable(subs, max_subs):
            p = find_priority(req[1])
            val = int(req[2])
            requests.enqueue((p, val))
            subs += 1
        # If the operation is a valid print, the job of the highest 
        # priority employee is dequeued and written to the text file
        elif job == PRINT and printable(prints, max_prints):
            out = str(requests.dequeue()[1])
            ans.write(f"{out}\n")
            prints += 1
    f.close()
    ans.close()
        
Q4()