import requests
from bs4 import BeautifulSoup

class House:
  id: str
  price: int = 0
  bedroom_amount: int = 0
  bathroom_amount: int = 0
  area: float = 0
  floor_amount: int = 0
  air_conditioner: int = 0
  bbq: int = 0
  receptionists: int = 0
  gym: int = 0
  garden: int = 0
  library: int = 0
  park: int = 0
  playground: int = 0
  guard: int = 0
  pool: int = 0
  tennis_court: int = 0
  wifi: int = 0
  location: str = ''
  type: str = ''
  near_transport: int = 0
  furnished: str = ''
  feature_count: int = 0

  def __str__(self):
    return "Info of house: {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(self.id,\
      self.price, self.bedroom_amount, self.bathroom_amount, self.area, self.floor_amount, self.bbq,\
      self.receptionists, self.gym, self.garden, self.library, self.park, self.playground, self.guard,\
      self.pool, self.tennis_court, self.wifi, self.location, self.type, self.near_transport, self.furnished, self.feature_count)

  def increase_feature_count(self):
    self.feature_count += 1

allHouses = []

# 

url = "https://www.dotproperty.com.vn/houses-for-sale/hồ-chí-minh?page=2"

# url ="https://www.dotproperty.com.vn/condos-for-sale/h%E1%BB%93-ch%C3%AD-minh?near_transport=1&furnished=partly&page=7"

def crawl_by_topic(house_type, house_location, house_near_transport_status, house_furnish_status):
  if house_location != '':
    house_location = '/'+house_location
  if house_near_transport_status != '':
    house_near_transport_status = '&near_transport={}'.format(house_near_transport_status)
  if house_furnish_status != '':
    house_furnish_status = '&furnished={}'.format(house_furnish_status)
  for i in range(1,51):
    url = 'https://www.dotproperty.com.vn/{}-for-sale{}?page={}{}{}'.format(house_type, house_location, i, house_near_transport_status, house_furnish_status)
  pass


house_types = ['condos', 'townhouses', 'houses', 'villas', 'land', 'commercial-property', 'offices', 'retail-spaces', 'shophouse', 'warehouses', 'hotels']

house_locations = [
'an-giang', 'bà-rịa-vũng-tàu', 'bắc-giang', 'bắc-kạn', 'bắc-ninh', 
'bạc-liêu', 'bình-dương', 'bình-định',  'bình-phước', 'bình-thuận', 
'bến-tre', 'cà-mau', 'cần-thơ', 'cao-bằng', 'đà-nẵng', 'đắk-lắk',
'điện-biên', 'đắk-nông', 'đồng-nai', 'đồng-tháp', 'gia-lai',
'hà-nội', 'hà-giang', 'hà-nam', 'hà-tĩnh', 'hải-dương',
'hải-phòng', 'hậu-giang', 'hòa-bình', 'hồ-chí-minh', 'hưng-yên', 
'kiên-giang', 'khánh-hòa', 'kon-tum', 'lai-châu', 'lâm-đồng',
'lạng-sơn', 'lào-cai', 'long-an', 'nam-định', 'nghệ-an', 
'ninh-bình', 'ninh-thuận', 'phú-thọ', 'phú-yên', 'quảng-bình',
'quảng-ninh', 'quảng-trị', 'quảng-nam',  'quang-ngai', 'sóc-trăng',
'sơn-la', 'thanh-hoa',  'tây-ninh', 'thái-bình', 'thái-nguyên',
'thừa-thiên-huế', 'tiền-giang', 'trà-vinh', 'tuyên-quang', 'vĩnh-long',
'vĩnh-phúc', 'yên-bái',''
]

house_near_transport_statuses = ['1','']

house_furnish_statuses = ['fully','partly','unfurnished','']

# for house_type in house_types:
#   for house_location in house_locations:
#     for house_near_transport_status in house_near_transport_statuses:
#       for house_furnish_status in house_furnish_statuses:
#         crawl_by_topic(house_type, house_location, house_near_transport_status, house_furnish_status)





payload={}
headers = {
  'authority': 'www.dotproperty.com.vn',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
  'accept-language': 'en-US,en;q=0.5',
  'cache-control': 'max-age=0',
  'cookie': 'user_language=eyJpdiI6Im9nbG5zRXJORmNWdUxEUWp1ZzV0NUE9PSIsInZhbHVlIjoiSU82VlNBMzl6b3o3bXpFMHdNakdDdz09IiwibWFjIjoiODFkZTU4MzRlMTc1M2I3OTM5NWVmYzQ3NWQyN2NiZGQ4NzBiNjQ2MDg4ZDEwMmQ3NDJmNDU4ZmNhYjFjMjhiMSJ9; dot_property_group_idu=eyJpdiI6IjBCN3BHK1I4d3pvdnlqTEtGQmZsOVE9PSIsInZhbHVlIjoiZ2ZLYnNOT1wvclJ2MWlDOTRnRXlhZVNwSENjUmVRKzNBNDRzNUhSb1N6YWdqOEV5a3czWm90RE54bTRhQWJXMDAiLCJtYWMiOiJlNDI2NzUwZmE5MjJjOWQ0Y2NiMGUwZmQ2NWNkNTRjYTJmZGZkNWU1YjdiYjkyNTEwYjQ5ZWUxN2Q4YWYwNmU2In0%3D; vn_propert_alert_box=Wed Nov 23 2022 15:44:39 GMT+0700 (Indochina Time); XSRF-TOKEN=eyJpdiI6Ijd4dm14UnJqSjA0U20wNGt2dGxlUVE9PSIsInZhbHVlIjoiZHhINkNDTjVFRjJYZlpvekg2QTI3cVFvN2MySHJnQ2lVNW5xejl1WE1sZG9kMUJkd01oWmQ1NDFNYUZ0QUZpOWloeEtONlwvUkFBV2ViK1NraldRc1hRPT0iLCJtYWMiOiIzZmY2ZmUyMmIxYTIzOTRlMGJjMGE4ZTljYzBjZjI2ZDA4ZmI4OTU3NzIwODgwNmM0MTJiZmFmMzdiZTVhNzM2In0%3D; dot_property_group=eyJpdiI6IkZianBpb1U1Y09vK0RKMkcxSk5hOHc9PSIsInZhbHVlIjoiQ1JzQzhmd0QzbHZKUWlGeTVxUmRHXC9ZS1JPM0poQ1VOUG1JeFdNQjJZMGdlUCs4d2Fib1ZwdWxLN2xGSTFwWFY5eVlOalMxU1Y0UW5IVUwyMEgzZkxnPT0iLCJtYWMiOiIwMThhY2QzMTEwMjIwMmI1NmExYjAzZWI4NGE5OWJkNWI3Zjc0MzRhZDllN2Y3N2Q5NTcyNWFmZTI4ZmFjODIzIn0%3D; XSRF-TOKEN=eyJpdiI6ImR3MXlJRlVCVlVsV3JiRG9MSDlYOEE9PSIsInZhbHVlIjoibDFSU2ptYVJEVDNJbzQ5ZjlGUGE2SjFKSjd5bWd3UTdcL2NDVmRSc1h2aEhzR09GTGV6WWZleHlnemphbmNxSE5rYTh4WHQwTjNuTlZLVEt6TmpYclR3PT0iLCJtYWMiOiI0MjIyZDZjM2NiZWUzZDFmNzdlMjM2ZjYzNDhjMmU3OWYwYTI4ODgyNWExNmYwMzY4ZjNjZGYxOTgxY2ZkYThhIn0%3D; dot_property_group=eyJpdiI6InhuUVlkNjE5dkdnSHA3MlN0UzQ5d3c9PSIsInZhbHVlIjoiSlwvU1VZNEJyQVBWZDBrOFwvR29ScEs5Z01GakJiWDh5M0NrOGUxbjVZYjFyZXJVZXRZcVEzVytWQWdMc0xRNDQxZnlPcVdybVFtNmI5XC9OWXhLVTZodUE9PSIsIm1hYyI6ImFhMjZiYTk3ZDdlMDMxY2Y1NzBlMmVhY2I1OTY0ODU3YjEwMGRlMjJlNWExZThhZjRlMTI5NWM1ZjBiMWQxN2YifQ%3D%3D; dot_property_group_idu=eyJpdiI6Ikw3TG41YThFXC9vYjRvYVwvM2pNNUtvQT09IiwidmFsdWUiOiJrMDFra1JkZjF3WHNabkViZkVzT21EamozVkhwRVwvTTFjYU14WnJEdVlCQk4ycllldjl0Q1BvZFAwWlNLcVBCUyIsIm1hYyI6ImJjNTg1MjgwMGQ5M2ZlNTllZTZkZDJjMWM2ZGYxY2MwNmY4NGZhNmIzZDg3OTZjNDk3M2E1ZTBmMTM1MjJjMTgifQ%3D%3D; user_language=eyJpdiI6Im1tOVFDTFVkZkRHUGtYc1NSNUVTemc9PSIsInZhbHVlIjoicFwvZVdOVmxOb2pZSEZITEw4NURLTlE9PSIsIm1hYyI6IjExY2U5MDgzN2JiNmM2MTdjZGQzZDMxMzY0NzYxNjM5ZDhjMzhmOTMxNTFkNzMyNzYxZDA0MGYwNDVmMzIwNDAifQ%3D%3D',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'sec-gpc': '1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

soup = BeautifulSoup(response.content, 'lxml')

all_houses = soup.select('div.right-block')

print("Length of search lists: ", len(all_houses))

def get_info(house):
  houseInstance = House()

  # price
  try:
    price_text = (house.select_one('div.price').text).split()
    if len(price_text) == 3 and  price_text[2] == 'tỷ':
      price = int(float(price_text[1])*10**9)
    else:
      price = int(price_text[1].replace(',',''))
    houseInstance.price = price
    houseInstance.increase_feature_count()
  except:
    print('Error when crawling price')

  try:
    try:
      house_a_tag = house.find_all('a', href = True)[1]
      house_url = house_a_tag['href']
      house_response = requests.request("GET", house_url, headers=headers, data=payload)
    except:
      house_a_tag = house.find_all('a', href = True)[0]
      house_url = house_a_tag['href']
      house_response = requests.request("GET", house_url, headers=headers, data=payload)
  except:
    print('Error when crawling house url')
  house_soup = BeautifulSoup(house_response.content, 'lxml')

  # ID
  try:
    id_tag_parent = house_soup.select('div.section-title > div.pull-right > p.internal-ref')
    id = str(id_tag_parent[0]).split('ID tin rao: ')[1].split('\n')[0]
    houseInstance.id = id
    houseInstance.increase_feature_count()
  except:
    print('Error when crawling ID')
  #
  key_features = house_soup.select('ul.key-featured > li.text-center')

  try:
    for feature in key_features:
      amount = feature.span.text
      name = feature.text.split(amount)[1]

      # amount of bedroom
      if name == 'Phòng Ngủ':
        bedroom_amount = amount
        houseInstance.bedroom_amount = bedroom_amount
        houseInstance.increase_feature_count()

      # amount of bathroom
      elif name == 'Phòng Tắm':
        bathroom_amount = amount
        houseInstance.bathroom_amount = bathroom_amount
        houseInstance.increase_feature_count()
      
      # area
      elif name == 'Diện tích':
        area = float(amount.split()[0])
        houseInstance.area = area
        houseInstance.increase_feature_count()
      
      # amount of floor
      elif name == 'Số tầng':
        floor_amount = amount
        houseInstance.floor_amount = floor_amount
        houseInstance.increase_feature_count()
  except:
    print("Error when crawling key features")

  try:
    facilities_li_tag = house_soup.select('ul.facilities > li')
    for facility in facilities_li_tag:
      name = facility.text.strip()

      if name.encode() == 'Máy lạnh':
        houseInstance.air_conditioner = 1
        houseInstance.increase_feature_count()      
        
      elif name == 'Khu vực BBQ':
        houseInstance.bbq = 1
        houseInstance.increase_feature_count()

      elif name == 'Nhân viên lễ tân':
        houseInstance.receptionists = 1
        houseInstance.increase_feature_count()

      elif name == 'Phòng tập':
        houseInstance.gym = 1
        houseInstance.increase_feature_count()

      elif name == 'Sân vườn':
        houseInstance.garden = 1
        houseInstance.increase_feature_count()

      elif name == 'Thư viện':
        houseInstance.library = 1
        houseInstance.increase_feature_count()

      elif name == 'Bãi đậu xe':
        houseInstance.library = 1
        houseInstance.increase_feature_count()

      elif name == 'Sân chơi':
        houseInstance.playground = 1
        houseInstance.increase_feature_count()

      elif name == 'Bảo vệ':
        houseInstance.guard = 1
        houseInstance.increase_feature_count()

      elif name == 'Hồ bơi':
        houseInstance.pool = 1
        houseInstance.increase_feature_count()

      elif name == 'Sân Tennis':
        houseInstance.tennis_court = 1
        houseInstance.increase_feature_count()

      elif name == 'WiFi':
        houseInstance.wifi = 1
        houseInstance.increase_feature_count()
  except:
    print('Error when crawling facilities')

  print(houseInstance)

try:
  for each_house in all_houses:
    get_info(each_house)
except Exception as e:
  print(e)

# try:
#   get_info(all_houses[13])
# except Exception as e:
#   print(e)