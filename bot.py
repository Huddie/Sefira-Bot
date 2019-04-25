import os
import requests
from datetime import datetime
from threading import Timer

numbers_list_file = "numbers.txt"
timer = None

def generate_message_for_day(day):
    bracha = "בָּרוּךְ אַתָּה ה' אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, אֲשֶׁר קִדְּשָׁנוּ בְּמִצְוֹתָיו וְצִוָּנוּ עַל סְפִירַת הָעֹמֶר"
    harachaman = "הָרַחֲמָן הוּא יַחֲזִיר לָנוּ עֲבוֹדַת בֵּית הַמִּקְדָּשׁ לִמְקוֹמָהּ, בִּמְהֵרָה בְיָמֵינוּ אָמֵן סֶלָה"

    lines, message = None, None
    filename = 'sefira.txt'

    message = bracha
    message = "{0}\n\n".format(message)

    with open(filename) as f:
        lines = f.readlines()
        start = day + (day * 2)
        end = start+1
        message = "{0}{1}".format(message, lines[start])
        message = "{0}\n".format(message)
        message = '{0}{1}\n'.format(message, lines[end])


    message = '{0}{1}\n'.format(message, harachaman)
    return message

def send_message_to(message, number):
    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:{0}'.format(number)

    response = requests.post(
        'https://api.twilio.com/2010-04-01/Accounts/{0}/Messages.json'.format(os.getenv('TWILIO_ACCOUNT_SID')), 
        data={
            'To':'{0}'.format(to_whatsapp_number), 
            'From':'{0}'.format(from_whatsapp_number), 
            'Body':message 
        },
        auth=(
            '{0}'.format(os.getenv('TWILIO_ACCOUNT_SID')), 
            '{0}'.format(os.getenv('TWILIO_AUTH_TOKEN'))
        )
    )

def calculate_day():
    start = datetime(2019, 4, 21, 20, 0, 0)
    current = datetime.now()
    return abs((start-current).days)

def run():
    message = generate_message_for_day(calculate_day())
    print(message)
    with open(numbers_list_file) as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            send_message_to(message, line)
    update_timer()


def update_timer(bootstrapped=False):
    x = datetime.today()

    day = x.day if bootstrapped else x.day+1

    y = x.replace(
        day=day,
        hour=20, 
        minute=14, 
        second=0, 
        microsecond=0
    )

    delta_t = y - x
    
    secs = delta_t.seconds+1
    print(secs)
    timer = Timer(secs, run)
    timer.start()

def bootstrap():
    update_timer(True)

os.system('source /home/fa18/313/adeh6562/public_html/sefira_bot/Sefira-Bot/.env')
bootstrap()
