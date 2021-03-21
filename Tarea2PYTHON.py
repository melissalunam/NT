from typing import List
import requests
import json 

response = requests.get("https://reqres.in/api/users")

class Datum:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    def __init__(self, id: int, email: str, first_name: str, last_name: str, avatar: str) -> None:
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar


class Support:
    url: str
    text: str

    def __init__(self, url: str, text: str) -> None:
        self.url = url
        self.text = text


class Tarea:
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Datum]
    support: Support

    def __init__(self, page: int, per_page: int, total: int, total_pages: int, data: List[Datum], support: Support) -> None:
        self.page = page
        self.per_page = per_page
        self.total = total
        self.total_pages = total_pages
        self.data = data
        self.support = support


tarea_dict = response.json()
tarea = Tarea(**tarea_dict)

print("Page:", tarea.page)
print("Per Page:", tarea.per_page)
print("Total:", tarea.total)
print("Total Pages:", tarea.total_pages)
print("Data:", tarea.data)
print("Supporting:", tarea.support)