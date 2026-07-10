from fastapi import APIRouter
from app.services.analytics_service import get_enrollment_analytics

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/enrollments")
async def enrollment_analytics():
    return get_enrollment_analytics()