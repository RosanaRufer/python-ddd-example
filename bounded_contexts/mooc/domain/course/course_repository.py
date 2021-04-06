from typing import Optional

from bounded_contexts.mooc.domain.course import Course
from bounded_contexts.shared.domain.value_object import CourseId


class CourseDoesntExistException(Exception):
    pass


class CourseRepository:
    def save(self, course: Course):
        pass

    def search(self, _id: CourseId) -> Optional[Course]:
        pass
