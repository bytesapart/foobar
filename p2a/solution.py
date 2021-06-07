# If one looks at the examples, and does some more mental arithmetic
# one can realise that greedy rationing is exponential growth and
# conservative rationing is a fibonacci series, of course, this is
# assuming that there are no repeats of henchmen of the same rank that
# come to take ration, that is, a queue only has 1 of each rank, and is
# a sorted queue in increasing order.

def greedy_rationing(total_lambs):
    pay = 1  # Keep the base pay as 1 for the lowest henchman.
    henchman_number = 0  # The henchman number
    while True:
        henchman_number += 1
        if total_lambs <= 0:
            break
        pay *= 2
        total_lambs -= pay

    return henchman_number


def conservative_rationing(total_lambs):
    previous_pay = 0  # Previous pay, because we need to just add enough over this for cond 2 to fulfil
    pay = 1  # base pay as the least integer
    henchman_number = 0  # THe henchman number
    while True:
        henchman_number += 1
        if total_lambs <= 0:
            break
        temp = previous_pay + pay
        previous_pay = pay
        pay = temp
        total_lambs -= pay
    return henchman_number


def solution(total_lambs):
    return conservative_rationing(total_lambs) - greedy_rationing(total_lambs)


print('Solution: %d' % solution(143))
