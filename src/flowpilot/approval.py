"""Human approval gate for consequential workflow actions."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Approval:
    actor: str
    decision: str
    reason: str
def validate_approval(approval: Approval) -> None:
    decision = approval.decision.strip().casefold()
    if decision not in {"approved", "rejected"}: raise ValueError("decision must be approved or rejected")
    if not approval.actor.strip() or not approval.reason.strip(): raise ValueError("actor and reason are required")