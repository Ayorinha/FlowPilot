from dataclasses import dataclass,field
@dataclass
class Workflow:
 steps:dict[str,str]=field(default_factory=dict)
 def add(self,name,after=None):
  if name in self.steps:raise ValueError("step already exists")
  if after is not None and after not in self.steps:raise KeyError(after)
  self.steps[name]=after or ""
 def order(self):
  roots=[n for n,p in self.steps.items() if not p];result=[]
  while roots:
   n=roots.pop(0);result.append(n);roots += [c for c,p in self.steps.items() if p==n and c not in result and c not in roots]
  if len(result)!=len(self.steps):raise ValueError("workflow contains a cycle")
  return result
