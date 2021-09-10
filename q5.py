import heapq

def heapsort(iter):
    """ Heapsorts and returns sorted list"""
    h = []
    for val in iter:
        heapq.heappush(h, val)
    return [heapq.heappop(h) for i in range(len(h))]

def Q5():
    cost = 0
    f = open("q5_in.txt", "r")
    carts = f.readline().strip("\n")
    raw = f.readline().split(" ")
    li = [int(i) for i in raw]
    heap = heapsort(li)
    f.close()

    while True:
        # Creates two temp variables of first items in the heapsorted list
        # Adds them together to get the new cart length
        temp_l = heap.pop(0)
        temp_r = heap.pop(0)
        new_cart_cost = temp_l + temp_r
        # Add the cost of the new cart to the total cost
        cost += new_cart_cost
        # Appends the new cart to the list and performs heapsort 
        # on the list again to resort the new carts
        heap.append(new_cart_cost)
        heap = heapsort(heap)
        # Once the length of the list is one, the entire cost of the
        # rail wagons has been calculated, so the cost can be written
        # to the output file
        if len(heap) == 1:
            ans = open("q5_out.txt", "w")
            ans.write(str(cost))
            ans.close()
            return
        
Q5()