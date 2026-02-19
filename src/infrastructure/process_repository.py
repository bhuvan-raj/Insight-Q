import psutil


class ProcessRepository:
    def get_all_processes(self):
        processes = []

        for proc in psutil.process_iter(["pid", "name", "cpu_percent"]):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        return processes

