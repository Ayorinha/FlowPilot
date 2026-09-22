from __future__ import annotations
from dataclasses import dataclass, field
@dataclass
class Workflow:
    steps: dict[str, str] = field(default_factory=dict)
    def add(self, name: str, after: str | None = None) -> None:
        if not name.strip() or name in self.steps: raise ValueError("step name must be unique and non-empty")
        if after is not None and after not in self.steps: raise KeyError(after)
        self.steps[name] = after or ""
        self.order()
    def order(self) -> list[str]:
        roots = [n for n, parent in self.steps.items() if not parent]; result: list[str] = []
        while roots:
            node = roots.pop(0); result.append(node)
            roots.extend(c for c, p in self.steps.items() if p == node and c not in result and c not in roots)
        if len(result) != len(self.steps): raise ValueError("workflow contains a cycle")
        return result
