from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/user1/')
async def get_user1(db: Session = Depends(get_db)):
    try:
        return await service.get_user1(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user1/')
async def post_user1(id: int, first_name: Annotated[str, Query(max_length=100)], last_name: Annotated[str, Query(max_length=100)], age: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_user1(db, id, first_name, last_name, age)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user1/id/')
async def put_user1_id(id: int, first_name: Annotated[str, Query(max_length=100)], last_name: Annotated[str, Query(max_length=100)], age: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_user1_id(db, id, first_name, last_name, age)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user1/id')
async def delete_user1_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user1_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user2/')
async def get_user2(db: Session = Depends(get_db)):
    try:
        return await service.get_user2(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user2/id')
async def get_user2_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user2_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user2/id/')
async def put_user2_id(id: int, first_name: Annotated[str, Query(max_length=100)], last_name: Annotated[str, Query(max_length=100)], age: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_user2_id(db, id, first_name, last_name, age)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user2/id')
async def delete_user2_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user2_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user1/id')
async def get_user1_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user1_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user2/')
async def post_user2(id: int, first_name: Annotated[str, Query(max_length=100)], last_name: Annotated[str, Query(max_length=100)], age: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_user2(db, id, first_name, last_name, age)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

