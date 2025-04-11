import requests
import time
from datetime import datetime

# ✅ Đọc danh sách mã giftcode từ file
# with open("gift.txt", "r", encoding="utf-8") as f:
#     giftcodes = [line.strip() for line in f if line.strip()]
with open("gift_use_one.txt", "r", encoding="utf-8") as f:
    giftcodes = [line.strip() for line in f if line.strip()]

# ✅ Thông tin người dùng (cần thay bằng của bạn)
# nguyenhuuquynh2008@gmail.com 
# user_info = {
#     "userId": "3201572979494952960",
#     "profileId": "304cb6b0afe06981",
#     "serverId": "30",
#     "gameCode": "946",
#     "roleId": "1801473370578114575",
#     "roleName": "slowd",
#     "level": ""
# }
# # deadheartanytime@gmail.com 
# user_info = {"userId":"3204534136623620096","profileId":"33c5fbb541a5c981","serverId":"30","gameCode":"946","roleId":"1801473370581489933","roleName":"oSloW","level":""}
# acc = "quynh.nguyenhuu@imipgroup.com"
# user_info = {"userId":"3206406653746823168","profileId":"30e66b2b8ef88981","serverId":"36","gameCode":"946","roleId":"1801479968108685418","roleName":"slow36e","level":""}
acc = "nguyenquynhvp.ictu@gmail.com"
user_info = {"userId":"3206406653746823168","profileId":"30e66b2b8ef88981","serverId":"36","gameCode":"946","roleId":"1801479968108685418","roleName":"slow36e","level":""}
# ✅ Token lấy từ trình duyệt
AUTH_TOKEN = "VlBuTUZvaFdyQzVzaVRRT2VaNFhFdGx0N25ZaXlTYU9nQzBzZ29kYm0waz1NaGRJQXVGakpqejFmdnUpa2ROX2YhSjFKV180eTRReHVxRWFSU1IkQlhEM2FfcGdhKlBEWEBaQWJKdkxHdCpFKXNzNHpJTWl4NnMwNXNAcVojbXMrMTM2MDA2NzUzNTk5NDg1NTQyNA=="


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
    
    result_file.write(f"Account: {acc}")
    
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
