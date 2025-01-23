import requests
import time

# URL endpoint
url = "https://faucet.testnet.humanity.org/api/claim"

# Headers untuk request
headers = {
    "Host": "faucet.testnet.humanity.org",
    "Cookie": "_ga_L8M0X9GC83=GS1.1.1737654982.1.1.1737655132.0.0.0; _ga=GA1.1.1412965588.1737654982; _ga_1CH0N1F8LL=GS1.1.1737654982.1.1.1737655132.0.0.0; _lfa=LF1.1.8d9012dc47919afe.1737654982901; _ga_QLK92ZLL2G=GS1.1.1737655132.1.1.1737655135.0.0.0",
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
    time.sleep(10)
