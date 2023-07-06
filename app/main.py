import uvicorn
from fastapi import FastAPI
from settings import settings
from fastapi.middleware.cors import CORSMiddleware
from orm import db
from orm.db_setup import database, engine
import logging

description = """
    VELDICT Microservices.

    ## Alive

    For checking if the service is up
"""

db.metadata.create_all(engine)

app = FastAPI(title=settings.APP_NAME, description=description)

logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

origins = settings.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS
)

@app.get("/alive")
async def getInfo():
    return {
        "desc":"Microservices for veldict-be"
    }

@app.on_event("startup")
async def startup():
    logger.info("veldict-be service is up!!!")

@app.on_event("shutdown")
async def shutdown():
    logger.info("shutting down veldict-be service...")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)