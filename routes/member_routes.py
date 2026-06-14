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


'''@router.get('/members/{id}')
pass

@router.patch('/members/{id}')
pass

@router.patch('/members/{id}/deactivate')
pass

@router.patch('/members/{id}/activate')
pass'''