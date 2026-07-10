from app.core.db import database

enrollments_collection = database["enrollments"]


def get_course_analytics():

    pipeline = [
        {
            "$addFields": {
                "courseObjectId": {
                    "$toObjectId": "$courseId"
                }
            }
        },
        {
            "$group": {
                "_id": "$courseObjectId",
                "totalEnrollments": {
                    "$sum": 1
                }
            }
        },
        {
            "$lookup": {
                "from": "courses",
                "localField": "_id",
                "foreignField": "_id",
                "as": "course"
            }
        },
        {
            "$unwind": "$course"
        },
        {
            "$project": {
                "_id": 0,
                "courseTitle": "$course.title",
                "price": "$course.price",
                "totalEnrollments": 1
            }
        }
    ]

    return list(enrollments_collection.aggregate(pipeline))


