import json

import requests


def get_rates(from_curr="EUR", to_curr="ALL"):
    url = "https://www.bkt.com.al/bkt-backoffice/Exchanges/GetExchList"

    payload = {}
    headers = {
        'authority': 'www.bkt.com.al',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'cookie': '_ga=GA1.3.1836769806.1681411575; ASP.NET_SessionId=mgwfqtots5zzu4ixwyqmb4bd; _gid=GA1.3.149033988.1686146517; cookie-sticky-apply=true; _gat=1',
        'pragma': 'no-cache',
        'referer': 'https://www.bkt.com.al/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    for row in data['Data']['result']['RATE_TO_ALL']:
        if row['FROM_CURR_NAME'] == from_curr and row["TO_CURR_NAME"] == to_curr:
            return row , data['Data']['result']['LASTUPDATED']