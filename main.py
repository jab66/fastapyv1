from fastapi import FastAPI, Body

app=FastAPI()

# lista para ser usada por los endpoints
cars = [
    {
        "id":1, 
        "marca":"FIAT",
        "fundacion":1899,
        "pais":"Italia",
        "sede":"Turin",
        "fundador":"Giovanni Agnelli"
    },
    { 
        "id":2, 
        "marca":"FORD",
        "fundacion":1903,
        "pais":"Estados Unidos",
        "sede":"Dearborn",
        "fundador":"Henry Ford"
    },
    { 
        "id":3, 
        "marca":"BMW",
        "fundacion":1916,
        "pais":"Alemania",
        "sede":"Munich (Baviera)",
        "fundador":"Castiglioni, Rapp, Popp, Otto"
    },
    { 
        "id":4, 
        "marca":"CITROEN",
        "fundacion":1919,
        "pais":"Francia",
        "sede":"PSA Poissy Plant",
        "fundador":"André Citroën"
    }    
]


# Documentacion 
app.title = "Aplicacion API"
app.version = "2.0.0"


# mensaje de bienvenida
# http://localhost:8080/
@app.get('/', tags=['Home'])
def get_home():
    return "Bienvenidos a la Aplicacion API"

# obtener un auto por su ID
# http://localhost:8080/car/3
@app.get('/car/{id}', tags=['Home'])
def get_car(id:int):
    for car in cars:
        if car['id'] == id:
            return car
    return []

# obtener la lista completa de los autos
# http://localhost:8080/cars
@app.get('/cars', tags=['Home'])
def get_cars():
    return cars

# obtener un auto por el nommbre de la marca
# http://localhost:8080/car?marca=FIAT
@app.get('/car', tags=['Home'])
def get_car_by_name(marca:str):
    for car in cars:
        if car['marca'] == marca:
            return car
    return []

# agregar a la lista un nuevo auto
#{
#    "id": 5,
#    "marca": "RENAULT",
#    "fundacion": 1898,
#    "pais": "Francia",
#    "sede": "Boulogne-Billancourt",
#    "fundador": "Louis Renault"
#}
@app.post('/car', tags=['Home'])
def save_car (id:int = Body(), 
              marca:str = Body(), 
              fundacion:int = Body(), 
              pais:str = Body(), 
              sede:str = Body(), 
              fundador:str = Body()):
    cars.append(
        {
            "id":id,
            "marca":marca,
            "fundacion":fundacion,
            "pais":pais,
            "sede": sede,
            "fundador": fundador
        }
    )
    return cars
