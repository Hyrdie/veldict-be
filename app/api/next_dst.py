from fastapi import Depends, Header, Request
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from api.base_response import make_response
from fastapi.encoders import jsonable_encoder
import logging
from settings import settings


next_dst_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(next_dst_api)
class NextDestination():
    @next_dst_api.get('/next-destination')
    async def get_next_destination(self):
        data = [
            {
                "name":"Singapore",
                "image":"https://images.unsplash.com/photo-1600664356348-10686526af4f?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHNpbmdhcG9yZXxlbnwwfHwwfHx8MA%3D%3D"
            },
            {
                "name":"Japan",
                "image":"https://www.state.gov/wp-content/uploads/2019/04/Japan-2107x1406.jpg"
            },
            {
                "name":"Thailand",
                "image":"https://a.cdn-hotels.com/gdcs/production17/d398/4fc00310-ba03-4511-8028-c29f05535f08.jpg?impolicy=fcrop&w=800&h=533&q=medium"
            },
            {
                "name":"Malaysia",
                "image":"https://media.istockphoto.com/id/503588918/id/foto/cakrawala-kuala-lumper-saat-senja.jpg?s=612x612&w=0&k=20&c=1eSs3AhoTRa4RSV3TP9tcYhN0A0Cy8UbrbOXfckrmvg="
            }
        ]
        return make_response(payload=data)