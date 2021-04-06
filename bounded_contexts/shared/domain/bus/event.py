from __future__ import annotations


class DomainEvent:
    def __init__(self, aggregate_id: str, event_id: str, occurred_on: str = None):
        self.aggregate_id = aggregate_id
        self.event_id = event_id
        self.occurred_on = occurred_on

    def event_name(self) -> str:
        pass

    def to_primitives(self) -> list:
        pass

    def from_primitives(self, aggregate_id: str, event_id: str, body: list, occurred_on: str) -> DomainEvent:
        pass

    def aggregate_id(self) -> str:
        return self.aggregate_id

    def event_id(self) -> str:
        return self.event_id

    def occurred_on(self) -> str:
        return self.occurred_on


class DomainEventSubscriber:
    def subscribed_to(self) -> list:
        pass


class EventBus:
    def publish(self, domain_event: DomainEvent):
        pass
