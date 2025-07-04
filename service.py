from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_user1(db: Session):

    query = db.query(models.User1)

    user1_all = query.all()
    user1_all = (
        [new_data.to_dict() for new_data in user1_all] if user1_all else user1_all
    )
    res = {
        "user1_all": user1_all,
    }
    return res


async def post_user1(db: Session, id: int, first_name: str, last_name: str, age: str):

    record_to_be_added = {
        "id": id,
        "age": age,
        "last_name": last_name,
        "first_name": first_name,
    }
    new_user1 = models.User1(**record_to_be_added)
    db.add(new_user1)
    db.commit()
    db.refresh(new_user1)
    user1_inserted_record = new_user1.to_dict()

    res = {
        "user1_inserted_record": user1_inserted_record,
    }
    return res


async def put_user1_id(db: Session, id: int, first_name: str, last_name: str, age: str):

    query = db.query(models.User1)
    query = query.filter(and_(models.User1.id == id))
    user1_edited_record = query.first()

    if user1_edited_record:
        for key, value in {
            "id": id,
            "age": age,
            "last_name": last_name,
            "first_name": first_name,
        }.items():
            setattr(user1_edited_record, key, value)

        db.commit()
        db.refresh(user1_edited_record)

        user1_edited_record = (
            user1_edited_record.to_dict()
            if hasattr(user1_edited_record, "to_dict")
            else vars(user1_edited_record)
        )
    res = {
        "user1_edited_record": user1_edited_record,
    }
    return res


async def delete_user1_id(db: Session, id: int):

    query = db.query(models.User1)
    query = query.filter(and_(models.User1.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user1_deleted = record_to_delete.to_dict()
    else:
        user1_deleted = record_to_delete
    res = {
        "user1_deleted": user1_deleted,
    }
    return res


async def get_user2(db: Session):

    query = db.query(models.User2)

    user2_all = query.all()
    user2_all = (
        [new_data.to_dict() for new_data in user2_all] if user2_all else user2_all
    )
    res = {
        "user2_all": user2_all,
    }
    return res


async def get_user2_id(db: Session, id: int):

    query = db.query(models.User2)
    query = query.filter(and_(models.User2.id == id))

    user2_one = query.first()

    user2_one = (
        (user2_one.to_dict() if hasattr(user2_one, "to_dict") else vars(user2_one))
        if user2_one
        else user2_one
    )

    res = {
        "user2_one": user2_one,
    }
    return res


async def put_user2_id(db: Session, id: int, first_name: str, last_name: str, age: str):

    query = db.query(models.User2)
    query = query.filter(and_(models.User2.id == id))
    user2_edited_record = query.first()

    if user2_edited_record:
        for key, value in {
            "id": id,
            "age": age,
            "last_name": last_name,
            "first_name": first_name,
        }.items():
            setattr(user2_edited_record, key, value)

        db.commit()
        db.refresh(user2_edited_record)

        user2_edited_record = (
            user2_edited_record.to_dict()
            if hasattr(user2_edited_record, "to_dict")
            else vars(user2_edited_record)
        )
    res = {
        "user2_edited_record": user2_edited_record,
    }
    return res


async def delete_user2_id(db: Session, id: int):

    query = db.query(models.User2)
    query = query.filter(and_(models.User2.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user2_deleted = record_to_delete.to_dict()
    else:
        user2_deleted = record_to_delete
    res = {
        "user2_deleted": user2_deleted,
    }
    return res


async def get_user1_id(db: Session, id: int):

    user_list2 = aliased(models.User2)
    query = db.query(models.User1, user_list2)

    query = query.join(user_list2, and_(models.User1.id == models.User2.id))

    user_records = query.first()
    user_records = (
        [
            {
                "user_records_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
                "user_records_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
            }
            for s1, s2 in user_records
        ]
        if user_records
        else user_records
    )

    res = {
        "user_record": user_records,
    }
    return res


async def post_user2(db: Session, id: int, first_name: str, last_name: str, age: str):

    record_to_be_added = {
        "id": id,
        "age": age,
        "last_name": last_name,
        "first_name": first_name,
    }
    new_user2 = models.User2(**record_to_be_added)
    db.add(new_user2)
    db.commit()
    db.refresh(new_user2)
    user2_inserted_record = new_user2.to_dict()

    user_loop: str = "100"

    for user_loop_list in range(1, 100):

        inner: str = user_loop

        if id > id:
            pass

    res = {
        "user2_inserted_record": user2_inserted_record,
        "test": user_loop,
    }
    return res
