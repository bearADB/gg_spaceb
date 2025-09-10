import requests

# Thay URL này bằng Cloud Run URL của bạn
BASE_URL = "http://localhost:8000"

def test_auth():
    url = f"{BASE_URL}/auth"
    payload = {"username": "admin", "password": "12345"}
    response = requests.post(url, json=payload)
    print("Auth response:", response.status_code, response.text)
    if response.status_code == 200:
        return response.json().get("token")
    return None

def test_action1(token):
    url = f"{BASE_URL}/action1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("Action1 response:", response.status_code, response.text)

def test_action2(token):
    url = f"{BASE_URL}/action2"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("Action2 response:", response.status_code, response.text)

if __name__ == "__main__":
    token = test_auth()
    if token:
        print("\n✅ Got token:", token)
        test_action1(token)
        test_action2(token)
    else:
        print("\n❌ Auth failed, cannot test further.")
