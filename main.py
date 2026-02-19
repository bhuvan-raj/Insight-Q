from insight_q.infrastructure.process_repository import ProcessRepository
from insight_q.app.use_cases.get_processes import GetProcesses
from insight_q.app.use_cases.group_applications import GroupApplications


def main():
    repository = ProcessRepository()
    get_processes = GetProcesses(repository)

    processes = get_processes.execute()

    grouping = GroupApplications()
    applications = grouping.execute(processes)

    print("\nRunning Applications:\n")

    for app in applications[:10]:
        print(
            f"{app.name} | "
            f"Processes: {len(app.processes)} | "
            f"CPU: {round(app.total_cpu,2)}% | "
            f"MEM: {round(app.total_memory,2)}%"
        )


if __name__ == "__main__":
    main()
