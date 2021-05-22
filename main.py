from gateway import GithubAPI

def get_response(github_gateway: GithubAPI):
    return github_gateway.get_github_response()

def is_even_number(number: int):
    if number % 2 == 0:
        return True
    return False

if __name__ == "__main__":
    gateway =  GithubAPI()
    response = get_response(gateway).json()
    print(response)
