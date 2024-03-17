from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/ping",
    tags=["healthy"],
)


@router.get("")
async def ping():
    return {'ping': 'pong'}