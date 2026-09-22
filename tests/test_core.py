from flowpilot.core import *

def test_order():w=Workflow();w.add("a");w.add("b","a");assert w.order()==["a","b"]
