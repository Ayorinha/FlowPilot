from flowpilot.state import Transition,validate_transition

def test_transition_requires_reason():
    try: validate_transition(Transition("a","b","human",""))
    except ValueError: return
    raise AssertionError("expected ValueError")
