from fastapi import APIRouter, status
from app.schemas.course import CourseCreate
from app.services.course_service import create_course

router = APIRouter(
    prefix= "/courses",
    tags=["Courses"]
)

@router.post("/", status_code = status.HTTP_201_CREATED)
async def add_course(course: CourseCreate):
    return create_course(course)