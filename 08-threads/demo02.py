import http.client
import json
from threading import Thread
def get_character_films(id):
    conn = http.client.HTTPSConnection("swapi.co")
    conn.request("GET", f"/api/people/{id}/")
    r1 = conn.getresponse()
    data1 = json.load(r1)
    return data1['films']

class Counter:
    def __init__(self, total):
        self.count = total

    def take(self):
        self.count -= 1
        print(f"Remaining: {self.count}")



class FilmLoader(Thread):
    def __init__(self, url, counter):
        super().__init__()
        self.url = url
        self.counter = counter

    def run(self):
        conn = http.client.HTTPSConnection("swapi.co")
        conn.request("GET", self.url)
        r1 = conn.getresponse()
        data2 = json.load(r1)

        self.result = data2['title']
        self.counter.take()
        return data2['title']



films = get_character_films('1')
c = Counter(len(films))
loaders = [FilmLoader(url, c) for url in films]

for loader in loaders:
    loader.start()

for loader in loaders:
    loader.join()
    print(loader.result)