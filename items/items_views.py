from typing import Annotated
from fastapi import Path, APIRouter


router = APIRouter(prefix="/items")


@router.get("/")
def get_items():
    return ["item_1", "item_2"]


@router.get("/latest")
def get_latest_item():
    return {"item": {"id": 0, "name": "latest"}}


@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(..., gt=1, lt=1_000_000)]):
    return {"item": {"id": item_id}}
