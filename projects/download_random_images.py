import multiprocessing
import requests

def downloadimages(url , name):
    print(f"started downloading {name}")
    res = requests.get(url)
    open(f"files/file{name}.jpg", 'wb').write(res.content)
    print(f"finished downloading {name}")

if __name__=='__main__':
    url = 'https://picsum.photos/200/300'
    proc = []
    for i in range(100):
        p = multiprocessing.Process(target=downloadimages, args=[url, i])
        p.start()
        proc.append(p)

    for p in proc:
        p.join()
