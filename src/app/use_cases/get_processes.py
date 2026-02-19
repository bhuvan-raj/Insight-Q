from infrastructure.process_repository import ProcessRepository
from domain.models.process import Process


class GetProcesses:
    def __init__(self, repository: ProcessRepository):
        self.repository = repository

    def execute(self) -> list[Process]:
        return self.repository.get_all_processes()

