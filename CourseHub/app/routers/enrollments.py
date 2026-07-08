from fastapi import APIRouter, status

from app.schemas.enrollment import EnrollmentCreate
from app.services.enrollment_service import createEnrollment

router = APIRouter(
    prefix ="/enrollments",
    tags=["Enrollments"]
)

@router.post("/", status_code= status.HTTP_201_CREATED)
async def enroll_student(enrollment: EnrollmentCreate):
    return createEnrollment(enrollment)
