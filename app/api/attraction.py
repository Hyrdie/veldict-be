from fastapi import Depends, Header, Request
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from api.base_response import make_response
from fastapi.encoders import jsonable_encoder
import logging
from settings import settings


attraction_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(attraction_api)
class Attraction():
    @attraction_api.get('/attraction')
    async def get_next_destination(self):
        data = [
            {
                "city":"Kab Magelang",
                "tour_name":"Merapi Mount Tour",
                "star_review":4,
                "total_review":200,
                "price":"Rp300.000"
            },
            {
                "city":"Kab Jogja",
                "tour_name":"Parangtritis Beach",
                "star_review":5,
                "total_review":350,
                "price":"Rp100.000"
            },
            {
                "city":"Kab Bandung",
                "tour_name":"Bukit Bintang",
                "star_review":3,
                "total_review":150,
                "price":"Rp50.000"
            },
            {
                "city":"Kab Bekasi",
                "tour_name":"Transera Park",
                "star_review":4,
                "total_review":100,
                "price":"Rp85.000"
            }
        ]
        return make_response(payload=data)