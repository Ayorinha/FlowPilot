from flowpilot.workflow import *
def test_gate():
 w=Workflow([Step('prepare'),Step('publish',True)])
 try:w.run(set()); assert False
 except PermissionError:pass
 assert w.run({'publish'})==['prepare','publish']
