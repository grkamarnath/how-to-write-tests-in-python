from gateway import GithubAPI

def get_response(github_gateway: GithubAPI):
    return github_gateway.get_github_response()


if __name__ == "__main__":
    gateway =  GithubAPI()
    response = get_response(gateway).json()
    print(response)
