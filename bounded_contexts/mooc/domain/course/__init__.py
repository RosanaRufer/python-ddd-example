from typing import Optional

from bounded_contexts.shared.domain.value_object import CourseId, StringValueObject


class CourseDuration(StringValueObject):
    pass


class CourseName(StringValueObject):
    pass


class Course:
    def __init__(self, _id: CourseId, name: CourseName, duration: CourseDuration):
        self.id = _id
        self.name = name
        self.duration = duration

