import requests

# Thay URL này bằng Cloud Run URL của bạn
BASE_URL = "https://spaceb2-732200390205.europe-west1.run.app"

def get_token(username: str, password: str):
    url = f"{BASE_URL}/token"
    data = {
        "username": username,
        "password": password
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)
    print("Login response:", response.status_code, response.text)
    if response.status_code == 200:
        return response.json().get("access_token")
    return None

def call_action(endpoint: str, token: str):
    url = f"{BASE_URL}/{endpoint}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(f"{endpoint} response:", response.status_code, response.text)

if __name__ == "__main__":
    # 1. Login để lấy token
    token = get_token("admin", "12345")
    if not token:
        print("❌ Login failed")
        exit(1)
    
    print("\n✅ Got token:", token)
    
    # 2. Gọi action1
    call_action("action1", token)
    
    # 3. Gọi action2
    call_action("action2", token)
