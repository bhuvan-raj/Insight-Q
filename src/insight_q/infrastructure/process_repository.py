import psutil
from datetime import datetime
from insight_q.domain.models.process import Process



class ProcessRepository:
    def get_all_processes(self) -> list[Process]:
        processes = []

        for proc in psutil.process_iter(
            ["pid", "name", "cpu_percent", "memory_percent",
             "username", "status", "create_time"]
        ):
            try:
                info = proc.info

                process = Process(
                    pid=info["pid"],
                    name=info["name"] or "Unknown",
                    cpu_percent=info["cpu_percent"] or 0.0,
                    memory_percent=round(info["memory_percent"] or 0.0, 2),
                    user=info.get("username"),
                    status=info.get("status", "unknown"),
                    start_time=datetime.fromtimestamp(info["create_time"])
                    if info.get("create_time")
                    else None,
                )

                processes.append(process)

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        return processes
