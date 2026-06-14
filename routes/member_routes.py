from fastapi import APIRouter, HTTPException
from database.member_db import MembersDB

db_members = MembersDB()

router = APIRouter()


@router.post('/members')
def loc_create_member(data: dict):
    result = db_members.create_member(data)
    return {"meesage": f"Creating members {result} successfully."}


@router.get('/members')
def loc_get_all_members():
    result = db_members.get_all_members()
    return {"message": f"Successful displayed {result}"}


@router.get('/members/{id}')
def loc_get_member_by_id(id: int):
    result = db_members.get_member_by_id(id)
    if result is None:
        raise HTTPException(status_code=404, detail="detail not found")
    return {"message": f"Successful displayed {result}"}


@router.patch('/members/{id}')
def loc_update_member(id: int, data: dict):
    result = db_members.update_member(id, data)
    if not result:
        raise HTTPException(status_code=404, detail="invalid input")
    return {"message": "Updating successfully."}


'''@router.patch('/members/{id}/deactivate')
pass

@router.patch('/members/{id}/activate')
pass'''