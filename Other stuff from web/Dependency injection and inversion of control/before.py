import os


class ApiClient:

    def __init__(self) -> None:
        self.git_lfs_path = os.getenv("GIT_LFS_PATH")  # <-- dependency
        self.num_of_cpu = int(os.getenv("NUMBER_OF_PROCESSORS"))  # <-- dependency


class Service:

    def __init__(self) -> None:
        self.api_client = ApiClient()  # <-- dependency


def main() -> None:
    service = Service()  # <-- dependency
    print(service.api_client.git_lfs_path)
    print(service.api_client.num_of_cpu)


if __name__ == "__main__":
    main()
