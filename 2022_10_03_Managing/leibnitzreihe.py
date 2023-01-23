import multiprocessing
import math
import time


def leibnitz(q: multiprocessing.Queue, calcs: list):
    answer = 0
    for num in calcs:
        answer += math.pow(-1, num) / (2 * num + 1)
    q.put(answer)


queue = multiprocessing.Queue()
processes = []
proc_amount = 12
almost_pi = 0

if __name__ == '__main__':
    while True:
        try:
            iterations = int(input("Please insert the amount of iterations: "))
            break
        except ValueError:
            print("Please insert a valid number")
    if iterations < 4:
        iterations = 4
    leibn = range(0, iterations)
    x = [leibn[i::proc_amount] for i in range(0, proc_amount)]
    # x = numpy.array_split(numpy.array(l), proc_amount)
    start_time = time.time()
    # x = [l[i:i + int(len(l)/proc_amount)] for i in range(0, len(l), int(len(l)/proc_amount))]
    for i in range(proc_amount):
        # rng_mn, rng_mx = int(iterations / proc_amount * i), int(iterations / proc_amount * (i + 1))
        process = multiprocessing.Process(target=leibnitz, args=(queue, x[i]))
        processes.append(process)
        process.start()
    for proc in processes:
        proc.join()
    finish_time = time.time()
    while not queue.empty():
        almost_pi += queue.get()
    almost_pi *= 4
    str_pi = str(math.pi)
    str_almost_pi = str(almost_pi)
    length = len(str_pi[2:])
    matching = 0
    for p, al_p in zip(str_pi[2:], str_almost_pi[2:]):
        if p == al_p:
            matching += 1
    print(f"The result of {iterations} Iterations of the Leibnitz-Row is done after /"
          f"{round(finish_time - start_time, 2)} Seconds. ({proc_amount} Processes were running)")
    print(f"There are {matching}/{length} Decimals ({round(matching / length * 100, 2)}%) matching in \n{almost_pi}")
