from fastapi import APIRouter, status
from app.schemas.review import ReviewCreate
from app.services.review_service import create_review

router = APIRouter(
    prefix = "/review",
    tags =["Review"]
)

@router.post("/", status_code = status.HTTP_201_CREATED)
def review_created(review: ReviewCreate):
    return create_review(review)