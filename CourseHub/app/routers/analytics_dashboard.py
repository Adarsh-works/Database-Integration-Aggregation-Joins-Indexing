from fastapi import APIRouter
from app.services.analytics_service import (
    get_enrollment_analytics,
    get_dashboard
)


router = APIRouter(
    prefix= "/analytics_dashboard",
    tags=["Analytics_Dashboard"]
)

@router.get("/dashboard")
async def dashboard():
    return get_dashboard()