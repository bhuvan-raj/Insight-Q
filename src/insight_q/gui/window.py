from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem
)
from PySide6.QtCore import QTimer

from insight_q.infrastructure.process_repository import ProcessRepository
from insight_q.app.use_cases.get_processes import GetProcesses
from insight_q.app.use_cases.group_applications import GroupApplications


class MonitorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Insight-Q")
        self.setGeometry(200, 200, 900, 500)

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["Application", "Processes", "CPU %", "Memory %"]
        )

        # Setup architecture objects
        self.repository = ProcessRepository()
        self.get_processes = GetProcesses(self.repository)
        self.group_applications = GroupApplications()

        # Auto refresh
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_data)
        self.timer.start(2000)

        self.refresh_data()

    def refresh_data(self):
        processes = self.get_processes.execute()
        applications = self.group_applications.execute(processes)

        self.table.setRowCount(len(applications[:10]))

        for row, app in enumerate(applications[:10]):
            self.table.setItem(row, 0, QTableWidgetItem(app.name))
            self.table.setItem(row, 1, QTableWidgetItem(str(len(app.processes))))
            self.table.setItem(row, 2, QTableWidgetItem(str(round(app.total_cpu, 2))))
            self.table.setItem(row, 3, QTableWidgetItem(str(round(app.total_memory, 2))))
