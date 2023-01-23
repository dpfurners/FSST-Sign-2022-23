iterations = 16
proc_amount = 4

for i in range(proc_amount):
    print([lst[i::n] for i in range(n)])
    print((iterations/proc_amount) * i)
    print((iterations/proc_amount) * (i + 1) - 1)
