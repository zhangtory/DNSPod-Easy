import requests
import json
import time


LOGIN_ID = "你的秘钥ID"
LOGIN_TOKEN = "你的秘钥Token"
DOMAIN = "你的域名，如zhangtory.com"
SUB_DOMAIN = "你的子域名，如www"

dns_headers = {
        "UserAgent": "DDNS MODIFY/1.0.0 (i@zhangtory.com)"
    }


def get_ip():
    headers = {
        "accept": "application/json"
    }
    request = requests.get("http://httpbin.org/ip", headers=headers)
    return json.loads(request.text)["origin"]


def get_dns_info():
    data = {
        "domain": DOMAIN,
        "sub_domain": SUB_DOMAIN,
        "login_token": LOGIN_ID + "," + LOGIN_TOKEN,
        "format": "json",
    }
    result = requests.post("https://dnsapi.cn/Record.List", headers=dns_headers, data=data)
    json_data = json.loads(result.text)
    return {
        "record_id": json_data["records"][0]["id"],
        "record_line_id": json_data["records"][0]["line_id"],
        "value": json_data["records"][0]["value"],
    }


def modify_dns(info):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ": ip changed. Modify.")
    data = {
        "login_token": LOGIN_ID + "," + LOGIN_TOKEN,
        "format": "json",
        "domain": DOMAIN,
        "sub_domain": SUB_DOMAIN,
        "record_id": info["record_id"],
        "record_line_id": info["record_line_id"]
    }
    result = requests.post("https://dnsapi.cn/Record.Ddns", headers=dns_headers, data=data)
    print(result.text)


if __name__ == "__main__":
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ": try to modify ddns.")
    ip_addr = get_ip()
    dns_info = get_dns_info()
    if ip_addr != dns_info["value"]:
        modify_dns(dns_info)
