"""Explicit workflow state machine primitives."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Transition:
    source: str
    target: str
    actor: str
    reason: str

def validate_transition(t: Transition) -> None:
    if t.source == t.target:
        raise ValueError("source and target must differ")
    if not t.actor.strip() or not t.reason.strip():
        raise ValueError("actor and reason are required")
