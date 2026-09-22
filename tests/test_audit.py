from flowpilot.audit import event

def test_event_is_timestamped():
    e=event("approve-payment","approved")
    assert e.step=="approve-payment"
    assert e.timestamp.tzinfo is not None
