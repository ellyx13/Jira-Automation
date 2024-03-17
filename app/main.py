from fastapi import FastAPI
from api.v1.routers import ping
from api.v1.routers import calendar




app = FastAPI()



app.include_router(ping.router)
app.include_router(calendar.router)