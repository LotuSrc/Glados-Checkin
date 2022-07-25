import requests
import os
import message

GLADOS_URL = "https://glados.rocks/api/user/checkin"

if __name__ == "__main__":
    # cookie
    # _ga=GA1.2.1996250465.1603113107; _gid=GA1.2.2109452833.1633938779; koa:sess=eyJ1c2VySWQiOjQxMDcxLCJfZXhwaXJlIjoxNjU5ODU4OTcwNzQ2LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=KUKllBOsSjUlpowUhCof1cAAefU
    headers = {
        "content-type": "application/json;charset=UTF-8",
        # "cookie": os.environ["COOKIE"],
        "cookie": "_ga=GA1.2.1379394489.1658736607; _gid=GA1.2.816068111.1658736607; __cf_bm=SqahpucjFEFmhv3_yqmV_wpb0BhBDQ8FCCJ0xHqjlKI-1658736627-0-AYE0F72jHGjdHAIvwT0xrB5/hHg6t9BnwKW/WwbXwIPWSismLhi/JtbOj819kQB5Ru8I9CxAhF3fdxjL5vIV82N2fwGP39LLRMEDq2jPJ+ws+2mTBvCwFXvo2wT2OehNpQ==; koa:sess=eyJ1c2VySWQiOjQxMDcxLCJfZXhwaXJlIjoxNjg0NjU2NzA3NDQ1LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=pNAyR14Q5uNRVCFxbgPjKRVHrvc; Cookie=enabled; Cookie.sig=lbtpENsrE0x6riM8PFTvoh9nepc",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
    }   

    data = {
        "token": "glados.network",
    }

    response = requests.post(GLADOS_URL, json=data, headers=headers)
    print(headers)
    print(response.status_code)
    print(response.json())
    print(response.status_code, response.json()["message"])

    msg = response.json()["message"]
    dingtalk_token = os.environ.get('DINGTALK_TOKEN')
    if dingtalk_token:
        ret = message.dingtalk(f"签到状态: {response.status_code} {msg}", dingtalk_token)
        print('send_dingtalk_message', ret)