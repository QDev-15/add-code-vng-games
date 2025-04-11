get authen token and insert to code.
get user info by go to link: https://giftcode.vnggames.com/vn/redeem/946
=> add any code and submit => open dev tool tab "NET WORK" copy urlcm like this:
" =============================== 
curl ^"https://vgrapi-sea.vnggames.com/coordinator/api/v1/code/redeem^" ^
  -H ^"accept: application/json, text/plain, */*^" ^
  -H ^"accept-language: vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5^" ^
  -H ^"authorization: MGNoV3Y0THB3SDJ1TnpqZHF2RGRLRFhJU1FnbGxCSXZWOHNBSUFZK3RLZz16Z0FZTUJueHM5TlZ6WnNkSGVIZVMpOEc3T3N6U25WVXoqSDJwQmhTJFhiYyozWTMzZ2Q0Z2JIak1fKUpFcUdySFl1YkRHayhHQlk5Yk5GemUoNGwrMTM2MDA2NzUzNTk5NDg1NTQyNA==^" ^
  -H ^"content-type: application/json^" ^
  -H ^"origin: https://giftcode.vnggames.com^" ^
  -H ^"priority: u=1, i^" ^
  -H ^"referer: https://giftcode.vnggames.com/^" ^
  -H ^"sec-ch-ua: ^\^"Google Chrome^\^";v=^\^"135^\^", ^\^"Not-A.Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"135^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  -H ^"sec-fetch-dest: empty^" ^
  -H ^"sec-fetch-mode: cors^" ^
  -H ^"sec-fetch-site: same-site^" ^
  -H ^"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36^" ^
  -H ^"x-client-region: VN^" ^
  -H ^"x-request-id: 2a45a8dd-90f8-4227-95a9-1532c743ac61^" ^
  --data-raw ^"^{^\^"userId^\^":^\^"3206406653746823168^\^",^\^"profileId^\^":^\^"30e66b2b8ef88981^\^",^\^"serverId^\^":^\^"36^\^",^\^"gameCode^\^":^\^"946^\^",^\^"roleId^\^":^\^"1801479968108685418^\^",^\^"roleName^\^":^\^"slow36e^\^",^\^"level^\^":^\^"^\^",^\^"code^\^":^\^"eqweqweqwe^\^"^}^"
============================================"

paste to postman and open tab body in postman. this is user info.
