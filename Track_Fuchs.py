import requests
from datetime import datetime
from time import sleep
today = datetime.today().strftime('%Y-%m-%d')

doctor_url = 'https://www.doctolib.de/gemeinschaftspraxis/muenchen/fuchs-hierl'
url = 'https://www.doctolib.de/availabilities.json'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

available = False

while available != True:
    ### Biontech 
    payload_biontech = {
    'start_date': today,
    'visit_motive_ids': '2820334',
    'agenda_ids': '466608',
    'insurance_sector': 'public',
    'practice_ids': '25230',
    'limit': '4'}

    json_biontech = requests.get(url, headers=headers, params=payload_biontech).json()
        
    if json_biontech['message'] == 'Diese Termine stehen zu einem späteren Zeitpunkt wieder für eine Online-Buchung zur Verfügung. ':
        print('*** Check again later!')
        sleep(5)
    else:
        print("*** Vaccine available")
        print("*** Open following website:", doctor_url)
        available = True 



# if json_biontech['message'] == 'Diese Termine stehen zu einem späteren Zeitpunkt wieder für eine Online-Buchung zur Verfügung. ':
#     print('Check again later!')
# else:
#     print("Vaccine available")
#     print("Open following website:", doctor_url)
  
### Astra  
# payload_astra = {
# 'start_date': today,
# 'visit_motive_ids': '2820336',
# 'agenda_ids': '466608',
# 'insurance_sector': 'public',
# 'practice_ids': '25230',
# 'limit': '4'}
# json_astra = requests.get(url, headers=headers, params=payload_astra).json()
# if json_astra['message'] == 'Diese Termine stehen zu einem späteren Zeitpunkt wieder für eine Online-Buchung zur Verfügung. ':
#     print('Check again later!')
# else:
#     print("Vaccine available")
#     print("Open following website:", doctor_url)