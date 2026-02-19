from infrastructure.process_repository import ProcessRepository


def main():
    repo = ProcessRepository()
    processes = repo.get_all_processes()

    print("\nRunning Processes:\n")

    for p in processes[:10]:
        print(p)


if __name__ == "__main__":
    main()

