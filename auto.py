import requests
import time
from datetime import datetime

# ✅ Đọc danh sách mã giftcode từ file
# with open("gift_use_one.txt", "r", encoding="utf-8") as f:
#     giftcodes = [line.strip() for line in f if line.strip()]
with open("gift1.txt", "r", encoding="utf-8") as f:
    giftcodes = [line.strip() for line in f if line.strip()]

# ✅ Thông tin người dùng (cần thay bằng của bạn)
link = "https://giftcode.vnggames.com/vn/redeem/946"
# account start
manageAcc = {
    "comebackvs1": {
        "info": {
            "userId": "3216562732197855232",
            "profileId": "332f45f0f761e981",
            "serverId": "107",
            "gameCode": "946",
            "roleId": "1801558040830296116",
            "roleName": "kid1",
            "level": "",
            "code": "12323"
            },
        "auth": "WGVIQW9ydlJ2Um5QUlRDZ0p0RkIyaFJxRWlvcmdPL1BZLzBFbkFXVmdSTT0yVnJDcU5fZWdEKWpIODkoYUdSSzZtUkVyKHg2SyFnT29DSnp5VVN4NzVwWTFIUGlzKGpDZE9JZ2J1NDhVczZDeClUaDVJTmNXZzBHN0N6b2xCOUArMTM3NDc0NDI2MTg2NjE5Mjg5Ng=="
    },
    "comebackvs2": {
        "info": {
            "userId": "3217190153209102336",
            "profileId": "332c676f83250981",
            "serverId": "107",
            "gameCode": "946",
            "roleId": "1801558040830388258",
            "roleName": "kid2",
            "level": "",
            "code": "123123"
            },
        "auth": "eEd6dTN2RnB1SGd6VUdtMmFMWmlJbDVUWkZERnFObGRQcnVlaEt2cWExQT1IMzVAMnAqJGtQc3Y4cEMzMm8xSzMoUyNreFY3ME1uZ09zMktXYzhQOU1POUkpZWhDcGc3UCREdndyOVJGNksoak8qIVYzamI5eXNjNkhoVlM2RWgrMTM3NDc1MTU1NTg3MjY4MTk4NA=="
    },
    "comebackvs3": {
        "info": {
            "userId": "3217192254024466432",
            "profileId": "332c647473e50981",
            "serverId": "107",
            "gameCode": "946",
            "roleId": "1801558040830482445",
            "roleName": "kid3",
            "level": "",
            "code": "1232"
            },
        "auth": "ZTVvbVp2TG80eEhSTlc3ZkEzcFBmTnBNQk5WODBtK1dJRjVTSElaNzZxQT1ob1NsY25QMDJDV1BEUHZwJEJwMGlNWW5aSCptRHVoTFpnR1owQGskRWR5c3diNl8kbnNuclIpU1BMY3lLNDkjRlJsSTZYbWlETkdNbVNRUVhNYTUrMTM3NDc1OTM2ODU1NjYwNTQ0MA=="
    },
    "comebackvs4": {
        "info": {
            "userId": "3236067817373089792",
            "profileId": "330dff992962f981",
            "serverId": "107",
            "gameCode": "946",
            "roleId": "1801558040830603371",
            "roleName": "kid4",
            "level": "",
            "code": "12123"
            },
        "auth": "SWpJeXhNc1ZaUU42Q2dtSHVRajAwV0dheC9KNFRscGx3Z2xJcS9vRi9paz1vRi1aT3VRQS1WbUA2NTl5WCkwQjl0VGFObmcjVSFaKTJQeEx2YTIzaUBQdG9qbmoyOU9JKTZlcDl0cTlNVDhJeVBaNFZzWGNMayozOGJHNW5YNFArMTM3NDc2NjM0MDM2MzY4MTc5Mg=="
    },
    "comebackvs5": {
        "info": {"userId":"3217195281360044032","profileId":"332c65d48da1e981","serverId":"107","gameCode":"946","roleId":"1801558040830699554","roleName":"kid5","level":"","code":"12323"},
        "auth": "N0tIaVUwKzZHcXFFeStMSTZzaC9KcHpSa1JRYm9xWndidVBUTUpwV1FqZz1iNm5DUHMxWF9Uc3lMJDQ2MU1QRzlZWmxLb1hkcjRfclpSMHBHRE5pdWhzVlhlekFPVl8hX0cjLVVDaHhfVlNpWnRaZ0ZQRDBvRG4qaTlSYnhCQzUrMTM3NDc3MTMwNjkwNjE1NzA1Ng=="
    },
    "comebackvs6": {
        "info": {"userId":"3209577257987686400","profileId":"311923431b66e981","serverId":"107","gameCode":"946","roleId":"1801558040830787601","roleName":"kid6","level":"","code":"123123"},
        "auth": "akdTak0rVWtGRmhqOVNQRGV6UjZ4Q25zTVdWaDFpWEdZc3RPOFg5clpZST1VbXZMVUo1MFEhKVUzbEA0dUE3cUVrb1JLcClmdVpLeHFIQzhHUTU0d3ppQ2NUOEpBYzdiI2shZTA5b1dPUzNsKVhBNU4tT1F4ZVBsWTYhdW5kNXorMTM3NDc3ODU4NTg5ODU3MzgyNA=="
    },
    "comebackvs7": {
        "info": {"userId":"3217197265211113472","profileId":"332c7a3392e1e981","serverId":"107","gameCode":"946","roleId":"1801558040830873672","roleName":"kid7","level":"","code":"12323"},
        "auth": "d3ZCMHNRaWVnYjU1aE5ld1JwMmc2YkNpSk8xeXRKRTNCK1lCTG5ianllcz1ocikjYVRGR09SUzFVOUxTYnhabG9Wa1AoQ1YwU01ieCpTbnc1a1poUXN1Qy0za1E0d01lV0MhNE5CM3kzUkN1X2kpWlNHQF8xelhzYWdpcUxJd0ErMTM3MTgzODY3Njg3Njc5NTkwNA=="
    },
    "comebackvs8": {
        "info": {"userId":"3217200108909740032","profileId":"332c7be68c250981","serverId":"107","gameCode":"946","roleId":"1801558040830955619","roleName":"kid8","level":"","code":"23123"},
        "auth": "K2ltK2wzOTVUV2lxaUZMdVd0SHBWQ1RrSXoyb2UySnJuNzFIRHp4anBnbz0oWjFLOVFyQk9DSmlEU3IzI25OdE00WHlEekRFQ0dENDB1VVVzU25FVEVKd3BIX0FJQnQjWVlLQkVhUm5ZVkB2a19wckxCaXNuOVVzOFdRUUk5MSgrMTM3NTAwOTYzMTI0NDE0ODczNg=="
    },
    "comebackvs9": {
        "info": {"userId":"3217203199538905088","profileId":"332c797ebb650981","serverId":"106","gameCode":"946","roleId":"1801556941280850179","roleName":"kid9","level":"","code":"131232"},
        "auth": "cGxJZHBzaGp1TldqRVFRWkJpQ3lZTklWNG9xV3drT3EwRWh1N3JDb3NmUT12eG5vc1E4IylSbm1haGVfVVh3KUF5RCluUlFQZGprKDZEeGtnblJSTGgqeU04d0BxRjFSMXFIM2R4cHFhbm9XZUBlb0VQMnMpcWVQdjkobm9VdSErMTM3NTAxMDMwODMzODE2NzgwOA=="
    },
    "forever_vp": {
        "info": {"userId":"3236551504758956032","profileId":"3302dbd997e52981","serverId":"106","gameCode":"946","roleId":"1801556941281970438","roleName":"kid10","level":"","code":"312323"},
        "auth": "akcyMDhnTlRBcmMzLytiNkNGb3luUTBrd21lRDh5ZkwxRmZTS1NSVVUyRT10YWhRM1lKQFRZUnlBMEF2c0hETXZOMChlNkQjdU9kYUQjY0h3RDJpSDhmcTVNKmdXS1hVJFlZWkQkRHJUalZ5UFBydDkyYmdiWHp2X2ZuLXY0cEkrMTM3NTAwNzYyODE4NjMwMDQxNg=="
    }
}

# account end

# acc7 => w1 + MP khi diet quai

accName = "comebackvs3"
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
            log = f"[{accName}]:[{code}] → {status_msg}"
        except Exception as e:
            log = f"[{accName}]:[{code}] → LỖI: {e}"

        print(log)
        result_file.write(log + "\n")
        time.sleep(1)  # Đợi 1 giây để tránh spam quá nhanh
