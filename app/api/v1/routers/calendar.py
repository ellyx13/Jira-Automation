from fastapi import APIRouter
from ..services import calendar as calendar_services
from .. import schemas
router = APIRouter(
    prefix="/api/v1/calendar",
    tags=["calendar"],
)



@router.post("", status_code=201, responses={
                201: {"model": schemas.calendar.CalendarResponse, "description": "Create event success"}
                })
async def create_event(data: dict):
    print(data)
    result  = await calendar_services.create_event(data)
    return result