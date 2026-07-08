from bson import ObjectId
from fastapi import HTTPException, status
from app.schemas.review import ReviewCreate
from app.core.db import database
from app.utils.helpers import serialize_doc


users_collection = database["users"]
course_collection = database["courses"]
enrollments_collection = database["enrollments"]
reviews_collection = database["reviews"]

def create_review(review: ReviewCreate):
    student = users_collection.find_one(
        {
            "_id": ObjectId(review.userId),
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
            "_id": ObjectId(review.courseId)
        }
    )
    if not course:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Course not found"
        )
    
    enrollment = enrollments_collection.find_one(
        {
          "userId": review.userId,
          "courseId": review.courseId
        }
    )
    if not enrollment:
        raise HTTPException(
            status_code = status.tatus.HTTP_403_FORBIDDEN,
            detail =  "Student is not enrolled in this course"
        )
    
    existing_review = reviews_collection.find_one(
        {
            "userId": review.userId,
            "courseId": review.courseId
        }
    )
    if existing_review:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Review already exists"
        )

    result = reviews_collection.insert_one(
        review.model_dump()
    )

    created_review = reviews_collection.find_one(
        {
            "_id":result.inserted_id
        }
    )
    return serialize_doc(created_review)
    