from dataclasses import dataclass
@dataclass(frozen=True)
class Step: name:str; requires_approval:bool=False
class Workflow:
 def __init__(self,steps): self.steps=steps
 def run(self,approved):
  pending=[s.name for s in self.steps if s.requires_approval and s.name not in approved]
  if pending: raise PermissionError(f'approval required: {pending[0]}')
  return [s.name for s in self.steps]
