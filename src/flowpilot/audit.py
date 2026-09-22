from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class WorkflowEvent:
    step: str
    action: str
    timestamp: datetime

def event(step: str, action: str) -> WorkflowEvent:
    if not step or not action: raise ValueError("step and action are required")
    return WorkflowEvent(step, action, datetime.now(timezone.utc))
