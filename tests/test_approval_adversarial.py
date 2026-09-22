from flowpilot.approval import Approval, validate_approval
def test_approval_accepts_normalized_decision(): validate_approval(Approval("human", " APPROVED ", "reviewed"))