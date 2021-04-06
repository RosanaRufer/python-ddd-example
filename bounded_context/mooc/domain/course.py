from typing import Optional

from bounded_context.shared.domain.value_object import CourseId, StringValueObject


class CourseDuration(StringValueObject):
    pass


class CourseName(StringValueObject):
    pass


class Course:
    def __init__(self, _id: CourseId, name: CourseName, duration: CourseDuration):
        self.id = _id
        self.name = name
        self.duration = duration


class CourseDoesntExistException(Exception):
    pass


class CourseRepository:
    def save(self, course: Course):
        pass

    def search(self, _id: CourseId) -> Optional[Course]:
        pass
