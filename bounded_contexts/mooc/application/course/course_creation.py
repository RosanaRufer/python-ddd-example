from bounded_contexts.mooc.domain.course import CourseName, CourseDuration, Course
from bounded_contexts.mooc.domain.course.course_events import CourseCreatedDomainEvent
from bounded_contexts.mooc.domain.course.course_repository import CourseRepository
from bounded_contexts.shared.domain.bus.event import EventBus
from bounded_contexts.shared.domain.value_object import CourseId


class CourseCreator:
    def __init__(self, course_repository: CourseRepository, bus: EventBus):
        self.course_repository = course_repository
        self.bus = bus

    def invoke(self, id: CourseId, name: CourseName, duration: CourseDuration):
        course = Course(id, name, duration)
        self.course_repository.save(course)
        # :lookleft: :lookright:
        self.bus.publish(CourseCreatedDomainEvent(
            aggregate_id=str(course.id),
            event_id='',
            name='',
            duration='',
        ))