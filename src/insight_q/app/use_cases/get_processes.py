from insight_q.domain.models.process import Process
from insight_q.infrastructure.process_repository import ProcessRepository



class GetProcesses:
    def __init__(self, repository: ProcessRepository):
        self.repository = repository

    def execute(self) -> list[Process]:
        return self.repository.get_all_processes()

