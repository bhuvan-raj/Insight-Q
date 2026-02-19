from dataclasses import dataclass, field
from typing import List
from insight_q.domain.models.process import Process


@dataclass
class Application:
    name: str
    processes: List[Process] = field(default_factory=list)
    total_cpu: float = 0.0
    total_memory: float = 0.0

    def calculate_totals(self) -> None:
        self.total_cpu = sum(p.cpu_percent for p in self.processes)
        self.total_memory = sum(p.memory_percent for p in self.processes)

