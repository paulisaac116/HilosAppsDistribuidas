from time import sleep, perf_counter
from threading import Thread

def task(id):
    print('Starting task... {}'.format(id))
    sleep(2)
    print('Finishing task... {}'.format(id))
    id*id*id*id

start_time = perf_counter()

# will create 10 execution threads

threads = []

for n in range(1,10):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = perf_counter()
print('It takes: {}'.format(end_time - start_time))