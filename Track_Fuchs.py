import requests
from datetime import datetime
from time import sleep
import platform

def notification_sound():
    if platform.system() == "Windows":
        # print("Windows")
        import winsound
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
    elif platform.system() == "Darwin":
        # print("Mac")
        import os
        os.system('afplay /System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Resources/Sounds/AnimationFlyToDownloads.aiff')

def notify_me():
    doctor_url = 'https://www.doctolib.de/gemeinschaftspraxis/muenchen/fuchs-hierl'
    counter = 0
    while counter <= 20: # Notify me for the next 20X30 seconds before the availabilty check again.
        print('***', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("*** Book appointment:", doctor_url)
        notification_sound()
        sleep(30) # Wait for another 30 seconds for another notification
        counter += 1


def check_availability():
    url = 'https://www.doctolib.de/availabilities.json'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
 
    while True:
        today = datetime.today().strftime('%Y-%m-%d')
        ### Biontech 
        payload_biontech = {
        'start_date': today,
        # visit_motive_ids for Astra: '2820336'
        # visit_motive_ids for Biontech: '2820334'
        # For testing, use Astra to trigger notification
        'visit_motive_ids': '2820334',
        'agenda_ids': '466608',
        'insurance_sector': 'public',
        'practice_ids': '25230',
        'limit': '4'}

        json_biontech = requests.get(url, headers=headers, params=payload_biontech).json()
            
        if json_biontech['message'] == 'Diese Termine stehen zu einem späteren Zeitpunkt wieder für eine Online-Buchung zur Verfügung. ':
            print('***', 'Vaccine not available')
            print('***', datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ': Appointment will be checked again in 20 minutes.')
            sleep(1200)
        else:
            print("*** Vaccine available")
            notify_me()

if __name__ == '__main__':
    print("*** That is the sound notification if a vaccine appointment becomes available:")
    notification_sound()
    print('*** If you do not here any sound, please check the volume and restart this script.')
    print('*** If still no sound, please contact the creator.')
    check_availability()