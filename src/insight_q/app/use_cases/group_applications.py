from collections import defaultdict
from typing import List

from insight_q.domain.models.process import Process
from insight_q.domain.models.application import Application


class GroupApplications:
    def execute(self, processes: List[Process]) -> List[Application]:
        grouped = defaultdict(list)

        for process in processes:
            key = process.name.lower()  # simple grouping strategy
            grouped[key].append(process)

        applications = []

        for name, procs in grouped.items():
            app = Application(name=name, processes=procs)
            app.calculate_totals()
            applications.append(app)

        return applications
