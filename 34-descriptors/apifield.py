import requests

class ApiField:
    def __init__(self, key):
        self.key = key

    def __get__(self, obj, type=None):
        r = requests.get(obj.url())
        r.raise_for_status()
        return r.json()[self.key]

class Person:
    name = ApiField('name')
    height = ApiField('height')

    def __init__(self, id):
        self.id = id

    def url(self):
        return f'https://swapi.co/api/people/{self.id}/'


class Film:
    title = ApiField('title')

    def __init__(self, id):
        self.id = id

    def url(self):
        return f'https://swapi.co/api/films/{self.id}/'

p = Person(5)
print(p.height)

f = Film(2)
print(f.title)









