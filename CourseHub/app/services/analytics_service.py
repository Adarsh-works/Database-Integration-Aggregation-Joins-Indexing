from app.core.db import database

enrollments_collection = database["enrollments"]
courses_collection = database["courses"]
users_collection = database["users"]

def get_enrollment_analytics():
    pipeline = [{
        "$addFields": {
            "userObjectId": {
                "$toObjectId": "$userId"
            },
            "courseObjectId": {
                "$toObjectId": "$courseId"
            }
        }
    },

    {
        "$lookup": {
            "from": "users",
            "localField": "userObjectId",
            "foreignField": "_id",
            "as": "student"
        }
    },
    {
        "$unwind": "$student"
    },
    {
    "$lookup": {
        "from": "courses",
        "localField": "courseObjectId",
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
            "studentName": "$student.name",
            "studentEmail": "$student.email",
            "courseTitle": "$course.title",
            "price": "$course.price"
        }
    }
    ]


    result = enrollments_collection.aggregate(pipeline)
    return list(result)

def get_dashboard():
        pipeline = [
            {
                "$facet": {
                    "totalEnrollments": [
                        {
                            "$count": "count"
                        }
                    ],
                    "recentEnrollments": [
                        {
                            "$sort": {
                                "_id": -1
                            }
                        },
                        {
                            "$limit": 5
                        },
{
    "$project": {
        "_id": {"$toString": "$_id"},
        "userId": 1,
        "courseId": 1
    }
}
                    ]
                }
            }
        ]

        dashboard = list(enrollments_collection.aggregate(pipeline))[0]

        total_users = users_collection.count_documents({})
        total_courses = courses_collection.count_documents({})

        return {
    "totalUsers": total_users,
    "totalCourses": total_courses,
    "totalEnrollments": (
        dashboard["totalEnrollments"][0]["count"]
        if dashboard["totalEnrollments"] else 0
    ),
    "recentEnrollments": dashboard["recentEnrollments"]
}


