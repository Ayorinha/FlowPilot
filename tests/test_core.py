from flowpilot.core import Workflow

def test_order():
    w = Workflow(); w.add("ingest"); w.add("retrieve", "ingest"); w.add("answer", "retrieve")
    assert w.order() == ["ingest", "retrieve", "answer"]

def test_cycle_guard():
    w = Workflow(); w.add("a"); w.add("b", "a"); w.steps["a"] = "b"
    try: w.order()
    except ValueError: pass
    else: raise AssertionError("cycle accepted")
