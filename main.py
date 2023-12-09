from fastapi import FastAPI
from routers.views import routers

app = FastAPI(title='Affiliation service')


app.include_router(routers)
