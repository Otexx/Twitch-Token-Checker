import requests

def check_token(token):
    headers = {
        'Authorization': f'OAuth {token}'
    }
    response = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers)
    if response.status_code == 200:
        print(f"\033[32mToken is valid!\033[0m")
        with open('valid_tokens.txt', 'a') as f:
            f.write(token + '\n')
        return True
    else:
        print(f"\033[31mToken is invalid.\033[0m")
        with open('invalid_tokens.txt', 'a') as f:
            f.write(token + '\n')
        return False

with open('tokens.txt', 'r') as f:
    tokens = f.read().splitlines()

for token in tokens:
    check_token(token)

print(f"\033[34mFinished Checking\n Valid Tokens: {len(open('valid_tokens.txt').readlines())} | Invalid Tokens: {len(open('invalid_tokens.txt').readlines())}\033[0m\n")
