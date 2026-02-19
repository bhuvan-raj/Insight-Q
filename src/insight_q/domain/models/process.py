from dataclasses import dataclass
from datetime import datetime


@dataclass
class Process:
    pid: int
    name: str
    cpu_percent: float
    memory_percent: float
    user: str | None
    status: str
    start_time: datetime | None

