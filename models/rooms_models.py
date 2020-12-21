from pydantic import BaseModel
from datetime import datetime

class RoomsIn(BaseModel):
    username: str
    tipo_room: str

class RoomsOut(BaseModel):
    username: str 
    id_room: int
    tipo_room: str
    camas: str
    ocupacion: str
    superficie: str
    vistas: str
    tarifa_basica: int