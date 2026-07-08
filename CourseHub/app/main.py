from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import client
from app.routers.users import router as users_router
from app.routers.courses import router as course_router
from app.routers.enrollments import router as enroll_router
from app.routers.reviews import router as review_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        client.admin.command("ping")
        print("MongoDB Connected")
    except Exceeption as e:
        print(f" MongoDb connection error: {e}")
    yield
    print("Application shutting down")

app = FastAPI(lifespan=lifespan)

app.include_router(users_router)
app.include_router(course_router)
app.include_router(enroll_router)
app.include_router(review_router)
