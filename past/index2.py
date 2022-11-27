import requests

url = "https://nha.chotot.com/toan-quoc/mua-ban-nha-dat?page=11&fbclid=IwAR3WwHSC9jKqOASOzJRJwj4_H_2Fh5pjC4gklRvYBGwu7-5t3JE_DbYoNMQ"

payload={}
headers = {
  'authority': 'www.nhatot.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
  'accept-language': 'en-US,en;q=0.6',
  'cache-control': 'max-age=0',
  'cookie': 'showInsertAdToolTip=true; isOnboardSimilarAd=true; isEntitlementProtectionTooltipVeh=true; searchInfo={%22originalAdId%22:138593906%2C%22page%22:%226000%22%2C%22position%22:1%2C%22ad_source%22:%22classifyad%22}; isOnboardCalFina=true; __cf_bm=shdegLG0QRkEOCW_.P73VMg3jupHmU6U4ZgbYs8RWNk-1669560818-0-AXYhrrPENIPPnEnJT/Nj7paQDGPjOczd6Gxwr9J0THfvIbvIJHur/tqQSRTrE1ZjXG3bh9ygiyOK/nCTteAOoIPjqOrO/hurzLmPqWHhQBlVkHLmGAIz6q/M97tLTWsmbVOPGTzwfj7pgQ7EPR3merfBdS1RBaqxbeLyqRAo54tt5cjvoymNYuEDHEhsC5s/iQ==',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'sec-gpc': '1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
