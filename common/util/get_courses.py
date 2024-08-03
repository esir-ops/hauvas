from django.contrib.auth.models import User


def get_courses(user: User):
    courses = None

    if user.profile.is_student:
        courses = get_student_courses(user)

    elif user.profile.is_professor:
        courses = get_professor_courses(user)

    return courses


def get_student_courses(user: User):
    student = user.student

    courses = []

    return courses


def get_professor_courses(user: User):
    professor = user.professor

    courses = []

    for course in professor.courses.all():
        course_content = {
            "id": course.id,
            "title": course.title,
            "code": course.code,
            "codename": course.codename,
            "department": course.department.abbr,
            "semester": course.semester.__str__(),
        }
        courses.append(course_content)
    return courses
