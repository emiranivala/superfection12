import requests
import time
from config import KOYEB_URL

url = KOYEB_URL  # Using URL from config

while True:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("✅ Keep-alive request successful")
        else:
            print(f"⚠️ Server returned status code: {response.status_code}")
    except requests.exceptions.Timeout:
        print("❌ Request timed out - server took too long to respond")
        time.sleep(30)  # Wait longer before retry on timeout
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed - please check your internet connection")
        time.sleep(60)  # Wait even longer on connection errors
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred: {str(e)}")
        time.sleep(30)  # Standard delay for other errors
    else:
        time.sleep(20)  # Normal delay between successful requests
