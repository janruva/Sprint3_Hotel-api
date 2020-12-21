from typing import Dict
from pydantic import BaseModel

class RoomsInDB(BaseModel):
    username: str
    id_room: int 
    tipo_room: str
    camas: str
    ocupacion: str
    superficie: str
    vistas: str
    tarifa_basica: int

database_rooms = Dict[str, RoomsInDB]
database_rooms = {
    "janruva": RoomsInDB(**{"username": "janruva",
                            "id_room": 101,
                            "tipo_room": "Superior",
                           "camas": "Cama medida doble",
                           "ocupacion": "2 personas",
                           "superficie": "25 mt2",
                           "vistas": "Patio",
                           "tarifa_basica": 100000,
                           }),
    "alexis": RoomsInDB(**{"username": "alexis",
                            "id_room": 201,
                            "tipo_room": "Deluxe",
                           "camas": "Cama medida queen",
                           "ocupacion": "2 personas",
                           "superficie": "30 mt2",
                           "vistas": "Museo, plaza o jardines",
                           "tarifa_basica": 200000,
                           }),
     "lorena": RoomsInDB(**{"username": "lorena",
                            "id_room": 301,
                            "tipo_room": "Junior",
                           "camas": "Cama medida king",
                           "ocupacion": "2 personas",
                           "superficie": "45 mt2",
                           "vistas": "Mar, playa",
                           "tarifa_basica": 300000,
                           }),
}

def get_room(username: str):
    if username in database_rooms.keys():
        return database_rooms[username]
    else:
        return None

def update_room(room_in_db: RoomsInDB):
    database_rooms[room_in_db.id_room] = room_in_db
    return room_in_db