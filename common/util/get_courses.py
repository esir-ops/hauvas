from django.contrib.auth.models import User


def get_professor_courses(user: User):
    professor = user.professor

    courses = []

    for course in professor.courses.all():
        course_content = {
            "course_id": course.id,
            "title": course.title,
            "code": course.code,
            "codename": course.codename,
            "department": course.department.abbr,
            "semester": course.semester.__str__(),
        }
        courses.append(course_content)
    return courses
