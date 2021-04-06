from bounded_contexts.shared.domain.bus.event import DomainEvent


class CourseCreatedDomainEvent(DomainEvent):
    def __init__(self, aggregate_id: str, event_id: str, name: str, duration: str, occurred_on: str = None):
        super().__init__(aggregate_id, event_id, occurred_on)
        self.name = name
        self.duration = duration

    def from_primitives(self, aggregate_id: str, event_id: str, body: list, occurred_on: str) -> DomainEvent:
        return super().from_primitives(aggregate_id, event_id, body, occurred_on)

    def event_name(self) -> str:
        return 'course.created'

    def to_primitives(self) -> list:
        return [
            ('name', self.name),
            ('duration', self.duration)
        ]

    def name(self) -> str:
        return self.name

    def duration(self) -> str:
        return self.duration
