import requests
import threading
import time


rs = []

def handler(i):
    t1 = time.time()
    # url = 'http://taojy123.cn:3000'
    # url = 'http://taojy123.cn:8080'
    url = 'http://taojy123.cn:5000'
    requests.get(url)
    print(i)
    t2 = time.time()
    t = int(t2 - t1)
    rs.append((t, i))


for i in range(3000):
    print(i)
    time.sleep(0.005)
    t = threading.Thread(target=handler,  args=(i, ))
    t.start()

print('--------------')
time.sleep(30)
print('=============')

rs.sort()
print(rs)
print('total:', len(rs))

