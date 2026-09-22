from flowpilot.approval import Approval,validate_approval

def test_approval_requires_reason():
    try: validate_approval(Approval("human","approved",""))
    except ValueError: return
    raise AssertionError("expected ValueError")
