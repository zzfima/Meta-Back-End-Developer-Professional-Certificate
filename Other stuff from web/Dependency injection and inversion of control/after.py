import os


class ApiClient:

    def __init__(self, git_lfs_path_key: str, num_of_cpu_key: str) -> None:
        self.git_lfs_path = git_lfs_path_key
        self.num_of_cpu = num_of_cpu_key


class Service:

    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client


def main(service: Service) -> None:
    service = Service(
        ApiClient(os.getenv("GIT_LFS_PATH"), int(os.getenv("NUMBER_OF_PROCESSORS")))
    )

    print(service.api_client.git_lfs_path)
    print(service.api_client.num_of_cpu)


if __name__ == "__main__":
    service = Service(
        ApiClient(os.getenv("GIT_LFS_PATH"), int(os.getenv("NUMBER_OF_PROCESSORS")))
    )

    main(service)
