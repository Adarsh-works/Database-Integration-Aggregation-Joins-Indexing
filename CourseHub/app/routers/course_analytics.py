from fastapi import APIRouter

from app.services.course_analytics_service import get_course_analytics

router = APIRouter(
    prefix= "/courses",
    tags=["Courses"]
)

@router.get("/courses")
async def course_analytics():
    return get_course_analytics()
    