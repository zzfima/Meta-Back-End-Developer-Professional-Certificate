import os


class ApiClient:

    def __init__(self, git_lfs_path_key: str, num_of_cpu_key: str) -> None:
        self.git_lfs_path = os.getenv(git_lfs_path_key)
        self.num_of_cpu = int(os.getenv(num_of_cpu_key))


class Service:

    def __init__(self, api_Client: ApiClient) -> None:
        self.api_client = api_Client


def main() -> None:
    service = Service(ApiClient("GIT_LFS_PATH", "NUMBER_OF_PROCESSORS"))
    print(service.api_client.git_lfs_path)
    print(service.api_client.num_of_cpu)


if __name__ == "__main__":
    main()
