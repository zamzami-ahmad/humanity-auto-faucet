import requests
import time

# URL endpoint
url = "https://faucet.testnet.humanity.org/api/claim"

# Headers untuk request
headers = {
    "Host": "faucet.testnet.humanity.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://faucet.testnet.humanity.org/",
    "Content-Type": "application/json",
    "Origin": "https://faucet.testnet.humanity.org",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
    "Te": "trailers"
}

# Data untuk request
payload = {"address": "YOUR WALLET ADDRESS"}

# Loop untuk mengulangi request setiap 1 menit 5 detik
while True:
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"Status Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error occurred: {e}")

    # Tunggu 1 menit 5 detik sebelum mengirim request berikutnya
    time.sleep(60)
