from fastapi import Depends, Header, Request
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from api.base_response import make_response
from fastapi.encoders import jsonable_encoder
import logging
from settings import settings


category_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(category_api)
class Category():
    @category_api.get('/category')
    async def get_next_destination(self):
        data = [
            {
                "category_name":"Femdom"
            },
            {
                "category_name":"Cowgirl"
            },
            {
                "category_name":"Doggy"
            },
            {
                "category_name":"Chikan"
            },
            {
                "category_name":"BDSM"
            },
            {
                "category_name":"Office"
            },
            {
                "category_name":"Drunk"
            }
        ]
        return make_response(payload=data)