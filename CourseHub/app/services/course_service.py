from bson import ObjectId
from fastapi import HTTPException, status

from app.core.db import database
from app.schemas.course import CourseCreate
from app.utils.helpers import serialize_doc

course_collection = database["courses"]
users_collection = database["users"]


def create_course(course: CourseCreate):

    instructor = users_collection.find_one(
    {
        "_id": ObjectId(course.instructorId),
        "role": "instructor"
    } )

    if not instructor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Instructor not found"
        )
    result = course_collection.insert_one(
        course.model_dump()
    )
    created_course = course_collection.find_one(
        {"_id": result.inserted_id}
    )
    return serialize_doc(created_course)
    

    
