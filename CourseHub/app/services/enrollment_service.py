from bson import ObjectId
from fastapi import HTTPException, status
from app.core.db import database
from app.schemas.enrollment import EnrollmentCreate
from app.utils.helpers import serialize_doc

users_collection = database["users"]
course_collection = database["courses"]
enrollments_collection = database["enrollments"]
from app.schemas.enrollment import EnrollmentCreate



def createEnrollment(enrollment: EnrollmentCreate):
    student = users_collection.find_one(
        {
            "_id": ObjectId(enrollment.userId),
            "role": "student"
        }
    )
    if not student:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Student not found"
        )
    
    course = course_collection.find_one(
        {
            "_id": ObjectId(enrollment.courseId)
        }
    )

    if not course:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Course not found"
        )

    existing_enrollment = enrollments_collection.find_one(
        {
            "user_id": enrollment.userId,
            "course_id": enrollment.courseId
        }
    )

    if existing_enrollment:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Student is already enrolled in this course"
        )

    result = enrollments_collection.insert_one(
        enrollment.model_dump()
    )

    created_enrollment = enrollments_collection.find_one(
        {
            "_id": result.inserted_id
        }
    )
    return serialize_doc(created_enrollment)