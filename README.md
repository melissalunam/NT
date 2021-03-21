Para esta actividad, utilicé la API pública: https://reqres.in/ . <br>
En el programa Postman, puse la siguiente URL: https://reqres.in/api/users , para obtener con GET, todos los usuarios. <br> 
El archivo JSON estará como Tarea2JSON.json . <br>
El archivo PYTHON estará como Tarea2PYTHON.py .

Para convertir el archivo de JSON a Python se hizo lo siguiente: <br> 
>1. Los datos que se pueden visualizar en el código son "page", "per_page", "total", "total_pages", etc., son los que están entre comillas y del lado izquierdo del signo ":".
<br>Todo aquello que contenga cada dato (lado derecho, después del signo ":"), será el valor; por ejemplo, con el primer dato "page" su valor es 1, con el segundo dato "per_page" su valor es 6 y así sucesivamente.
<br>Los valores que estén entre comillas serán cadenas de caracteres (aún cuando sea un número entre comillas) y los valores que no estén entre comillas serán valores numéricos.
>2. Los elementos raíz son fáciles de identificar, ya que son aquellos que contienen atributos, por ejemplo, "Support" contiene como atributos "url" y "text". <br> Como no se especifica el objeto raíz, lo que hicimos fue crear uno llamado Tarea.
>3. En el código podemos ver que sólo tenemos una lista llamada "data", ésta se pudo diferenciar de las demás porque sus datos están entre dos corchetes.
>4. Para los elementos raíz, en código Python, quedaron de la siguiente manera: <br>
```
class Support:
    url: str
    text: str

    def __init__(self, url: str, text: str) -> None:
        self.url = url
        self.text = text

```
```
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
```
>Y la lista quedó de la siguiente manera: <br>
```
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
        self.avatar = avatar
```
