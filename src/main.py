from infrastructure.process_repository import ProcessRepository
from app.use_cases.get_processes import GetProcesses


def main():
    repository = ProcessRepository()
    use_case = GetProcesses(repository)

    processes = use_case.execute()

    print("\nRunning Processes:\n")

    for p in processes[:10]:
        print(
            f"{p.pid} | {p.name} | CPU: {p.cpu_percent}% | "
            f"MEM: {p.memory_percent}% | {p.status}"
        )


if __name__ == "__main__":
    main()
