from db.user_db import UserInDB
from typing import Dict
from db.user_db import update_user, get_user
from db.rooms_db import RoomsInDB
from db.rooms_db import get_room, update_room
from models.user_models import UserIn, UserOut
from models.rooms_models import RoomsIn, RoomsOut
from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware
api = FastAPI()
origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", "https://seasonhotel-app.herokuapp.com"
]


api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.get("/")
async def root():
   
    return {"message" : "Bienvenido a Season Hotels"}

@api.get("/home")
async def root():
    message: str
    message = "Bienvenido a nuestro Season Hotels"
    return message

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")
    return  {"Autenticado": True}

@api.get("/user/room/{username}")
async def get_reserva(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return  user_out

@api.get("/user/tipo_room/{username}")
async def get_rooms(username: str):
    room_in_db = get_room(username)
    if room_in_db == None:
        raise HTTPException(status_code=401, detail="La habitación no existe")
    room_out = RoomsOut(**room_in_db.dict())
    return room_out

@api.get("/user/season/{username}")
async def get_season(username: str):
    room_in_db = get_room(username)
    if room_in_db == None:
        raise HTTPException(status_code=402, detail="La temporada no existe")
    room_out = RoomsOut(**room_in_db.dict())
    return room_out
