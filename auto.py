import requests
import time
from datetime import datetime

# ✅ Đọc danh sách mã giftcode từ file
with open("gift_use_one.txt", "r", encoding="utf-8") as f:
    giftcodes = [line.strip() for line in f if line.strip()]
# with open("gift.txt", "r", encoding="utf-8") as f:
#     giftcodes = [line.strip() for line in f if line.strip()]

# ✅ Thông tin người dùng (cần thay bằng của bạn)
link = "https://giftcode.vnggames.com/vn/redeem/946"
# account start
manageAcc = {
    "comebackvs1": {
        "info": {
            "userId": "3204549693749542912",
            "profileId": "33c5f2a0ab65c981",
            "serverId": "93",
            "gameCode": "946",
            "roleId": "1801473370585278761",
            "roleName": "slow123",
            "level": "",
            "code": "MUSTREAM"
        },
        "auth": "R1h6NTZJRWZoaWZnNHZobkJiUXpCWVRGRW9TT0lUM0NjVlc1K0Y5VmoxUT1FIVYzb3NCb2ZoX0std01aWlRVMVJTZCp3ITNFREFfVFk4ZkxRR1VnMXZiSHNUS2dEeWNEYTdkSi0tNi1yRzVFWHpqV3Ejc24obC0yQVUxdXdMdE8rMTM3MjE5NTczOTg3NzU2ODUxMg=="
    },
    "comebackvs2": {
        "info": "",
        "auth": ""
    },
    "comebackvs3": {
        "info": "",
        "auth": ""
    },
    "comebackvs4": {
        "info": "",
        "auth": ""
    },
    "comebackvs5": {
        "info": "",
        "auth": ""
    },
    "comebackvs6": {
        "info": "",
        "auth": ""
    },
    "comebackvs7": {
        "info": {
            "userId": "3217197265211113472",
            "profileId": "332c7a3392e1e981",
            "serverId": "93",
            "gameCode": "946",
            "roleId": "1801542645300502569",
            "roleName": "slowa",
            "level": "",
            "code": "4234"
        },
        "auth": "d3ZCMHNRaWVnYjU1aE5ld1JwMmc2YkNpSk8xeXRKRTNCK1lCTG5ianllcz1ocikjYVRGR09SUzFVOUxTYnhabG9Wa1AoQ1YwU01ieCpTbnc1a1poUXN1Qy0za1E0d01lV0MhNE5CM3kzUkN1X2kpWlNHQF8xelhzYWdpcUxJd0ErMTM3MTgzODY3Njg3Njc5NTkwNA=="
    },
    "comebackvs8": {
        "info": "",
        "auth": ""
    },
    "comebackvs9": {
        "info": "",
        "auth": ""
    },
    "comebackvs10": {
        "info": "",
        "auth": ""
    }
}

# account end

accName = "comebackvs7"
acc = manageAcc[accName] # type: ignore
user_info = acc["info"]
# user_info["serverId"] = "" # server thứ : vd: 93
# user_info["roleName"] = "" # tên nv

# ✅ Token lấy từ trình duyệt
AUTH_TOKEN = acc["auth"]


# Token lay tu file
# Đọc token từ file
with open("token-nguyenquynhvp.ictu.txt", "r") as token_file:
    AUTH_TOKEN = token_file.read().strip()
# ✅ API URL
url = "https://vgrapi-sea.vnggames.com/coordinator/api/v1/code/redeem"

headers = {
    "accept": "application/json, text/plain, */*",
    "authorization": AUTH_TOKEN,
    "content-type": "application/json",
    "origin": "https://giftcode.vnggames.com",
    "referer": "https://giftcode.vnggames.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "x-client-region": "VN"
}

# ✅ Mở file result.txt để ghi kết quả
with open("result.txt", "w", encoding="utf-8") as result_file:
    result_file.write(f"Kết quả nhập giftcode - {datetime.now()}\n\n")
    
    result_file.write(f"🕒 Thời gian: {datetime.now()}\n\n")
    
    result_file.write(f"Account: {acc} - {link}")
    
    result_file.write("👤 Thông tin người dùng:\n")
    for k, v in user_info.items():
        result_file.write(f"  {k}: {v}\n")
    result_file.write("\n===========================\n")
    
    for code in giftcodes:
        payload = {**user_info, "code": code}
        try:
            response = requests.post(url, json=payload, headers=headers)
            result = response.json()
            # Tùy API, bạn có thể kiểm tra message, statusCode, v.v.
            status_msg = result.get("message") or str(result)
            log = f"[{code}] → {status_msg}"
        except Exception as e:
            log = f"[{code}] → LỖI: {e}"

        print(log)
        result_file.write(log + "\n")
        time.sleep(1)  # Đợi 1 giây để tránh spam quá nhanh


