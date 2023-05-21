#importing data from the module
#importing data from googlesheets

from pushbullet import Pushbullet
import gspread
import pandas as pd

#to access the spread sheet with its credentials
credentials = {
  "type": "service_account",
  "project_id": "elite-cascade-380814",
  "private_key_id": "6ef409f7b6d5865db4d6e0cb87ecdf1698fe1869",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCpmMHfQ4d4df6a\njCLHPAlWNWzbBx+rDTTPNuidX5sczRjVXOOhxRWvMSxdelF7PVzMkykvowC4x+fL\nAym1g2laCseanX2KKdRJKwaweEyjooVnbYD1O2GctYr2rORADEmHBiJBhz9UdpFO\nQeTI+YmRkBKDF5SZxCjgzUTf9YIXX1ysvZcuw2nwkkrpGyKnR9iQWa+2p+ueXZ8d\nr5NipzH8eeYD6RaRSxnpoaDwxrLQg5aut1Z5j95kkIO20zEGcN9ZK1AB3YWYwrWn\njyEN0vitciAW141ICpS9NEZmd/CFHfJn3mbcQfKXRakLD+9RI20qaA2zGT9Bsi9T\nxK1uQTgLAgMBAAECggEADQSXORJ/Zw0zllxUXROsKcxfBy70TNZuK8usrkvE5cCO\ne+4t4OB2aiStoZ0+fOW4ZlGTcz8hUo2xqqEbBf5Iy2sRaDpXhQ/x5g3h7RDG3Taf\n49EBeZFtzDAZMxcRTCNFT5J2da4ye8LAI5AmRhD1cNFswlhAhU8LzjmjZEd9jVqa\nAKkaNZxskaUkNUVuJ+mJCrbr6TlsFbsV4hFxQuNX/bKh3swj09aRnKmtGv1YwqX7\ndIdMh23AG/9WHmL3mVq0dKUruvqsGG2IQlJfp4iwiMmY6CY/xCyHDWd0xBqmE7ko\n4XSbiqMRTM7OwKmRXMEUGKGLPx1/pQ1TwON9dSoikQKBgQDdEuOOtb2ICKFedSZ2\nzZ/uXNgEHip+v+sN7oUuGF0JjbD773/7oocUu8YVewVZe47DcASE/nIESimBP3JE\nKP8OFcRekgcx83KVY+U2V/17SEBnSGERZcgeBhDoJcAQZ1ikipknyot0kE1/nFQc\nU77zdhJS45hTaZPsqGboFHSEWwKBgQDEY+3I7R7pNITrAc2rC0N2Dvg8kphhici3\npiD9Yd8ksLS7soylLOG3goXvUoREzFS4p5GpKjAej/xJzVooXS/52vhkT/w8VU7e\npk5xrJR5lGm9znr3bBQ+lnDwz8xzeTuQ9NU9EnH5Ahqca0hHNIjK8GCgVwKTHZv+\nNkHKGeCqEQKBgQDDOlIQjfhBMHXo54W/Npk8s2rkQAuBAVS/adrcuRE4RZN8+KTK\nAF5P9f7Yq1ovCokpmDu1gsoHdcKva+spvBZ5RsmyRjzqZLXUrXIWip/EBisxyl5G\nMd8GfI7jo6q4EbvbGrZjyF9c4a4+ujwhA+fGMoe+AVVcnAjQ3mp6Gs5GrwKBgDbk\nb3wvuuoYAebl9CSQ22ROPtg/aVQp/O5IAwSPrJ1Gvt2PxHwOlXCDjQgdmlbYff22\n6KHN5vFD8ZJ3UXHiyhweNjtjl+8NMSROe7KOOFnbP8sLwZcSoH318s98ZXsJMbsM\nk+WkGDMvgVyjJ+qvJmUC1x858sBIEGf3pl/k58ThAoGAGx105Zu2UAm+gd9bIA7s\nW2a/msN1jrURi/R+OqV+pXCB4IVuqI7WcppicHSBAFcqQcPKbPIgbewaoYC5kVit\nGars46pM8EbYUH4D5mV2UueIEDXF8zT3ExtXvj+Lf7sRDSF8L78MeiqCbfjzzZmJ\nzSEmiOmbY+2GAQo6p/bfwRA=\n-----END PRIVATE KEY-----\n",
  "client_email": "jatayudata@elite-cascade-380814.iam.gserviceaccount.com",
  "client_id": "105457486913542123709",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/jatayudata%40elite-cascade-380814.iam.gserviceaccount.com"
}
gc = gspread.service_account_from_dict(credentials)
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1oDJDaWNkQFLqAAX7etAXUBPqTftHyDw2qSuynhQ2NE8/edit#gid=0')
worksheet = sht2.get_worksheet(0)
rows = worksheet.get_all_records()
df = pd.DataFrame(rows)
#for alert messege
def messege_allert():
    API_KEY="o.v6EKbSMDOE1GqNdtqoOA9tPaRdnaFoew"
    file={"txt":'YOU HAVE REACHED YOUR DAILY AVERAGE CONSUMPTION \nSAve_allert',}
    TEXT=file['txt']
    pb=Pushbullet(API_KEY)
    push=pb.push_note('PLS',TEXT)

def messege():
    API_KEY="o.v6EKbSMDOE1GqNdtqoOA9tPaRdnaFoew"
    date=df.iloc[1][0]
    a=Today_energy_consumption(date)
    b=df.iloc[1]
    file={"txt":f"{a}{b}",}
    TEXT=file['txt']
    pb=Pushbullet(API_KEY)
    push=pb.push_note('Allert',TEXT)
#for uncertain currentflow times............
cur=df.iloc[1]
surge={}
b=float(cur[3])
if b>38:
    surge[cur[1]]=cur[3]
def allert():
    return(surge)
#-------for alert------
a=df.iloc[1][0]
thr = 3.0
sam = df.query("date == @a")
l = sam["energy"]
s = 0.0
for i in l:
    i = float(i)
    s = s + i
    a=s/3600
    if a >= thr:
        d= messege_allert()
        print (d,"Danger!!!")
        break

#query-1:
def Today_energy_consumption(date):

    sem_info = df.query("date == @date")# where a is taken from input of chatbot
    energy_column = sem_info["energy"]
    consumption = 0.0
    for k in energy_column:
        consumption += k
    return(consumption/3600)
#query-2
def compare_days(date1,date2):
    to=0
    bo=0
    sem_info = df.query("date == @date1")
    l = sem_info["energy"]
    sem_info = df.query("date == @date2")
    h = sem_info["energy"]
    for i , j in zip(l,h):
        to+=i
        bo+=j
        p=to/3600
        d=bo/3600
    return ("date1 consumption:", p , "date2 consumption:" ,d , "difference:",abs(p-d))
#query-3
def pricing_per(units):
    if(units < 50):
        amount = units * 2.60
        surcharge = 25
    elif(units <= 100):
        amount = 130 + ((units - 50) * 3.25)
        surcharge = 35
    elif(units <= 200):
        amount = 130 + 162.50 + ((units - 100) * 5.26)
        surcharge = 45
    else:
        amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
        surcharge = 75
    #surcharges are not added because we are taking pricing per day surcharges are added for monthly charges...........

    total = amount# + surcharge
    print("\nElectricity Bill = %.2f"  %total)
    return total


#chatbot.........................

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Create a bot object with the API token
bot = telegram.Bot(token='6001383871:AAEarO8FdemUkfkus-IwcZfu8wU4_OprfaQ')

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('SAVE ALLERT WELCOMES YOU😊, MONITORING MADE SIMPLE AND EASE😀..\nType /help to see all available commands ')

def help(update, context):
    """Send a message when the command /help is issued."""
    help_message = '''
    Available commands:
    /usage - Show the daily usage of energy
    /Present_Status - Show the current details of the system i.e current,voltage,power factor
    /Pricing - per day pricing
    /comparision - show the difference in usage in different days
    /message_alert - an allert message that gives the time at which the high currents drawn
    /Alert  - Gives an save allert message about the times when unusual current flow/sudden surges has taken
    '''
    update.message.reply_text(help_message)

def pricing(update, context):
    he_message= '''
     Please enter date in following format /pricing <space> YYYY/MM/DD<space> ....
        '''
    update.message.reply_text(he_message)
    date = update.message.text

    # Split the message into two numerical inputs
    try:
        date1,date2 = date.split()[1:]
        date1 = str(date1)
        date2= str(date2)

    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid input. ")
        return
    units=float(Today_energy_consumption(date1))
    #units = int(input(" Please enter Number of Units you Consumed : "))
    price=pricing_per(units)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"price for your consumption is: {price}.")


    # Get the user's message



def comparision(update, context):
    he_message= '''
     Please enter two dates separated by a space in format /comparision <space> YYYY/MM/DD <space> YYYY/MM/DD.
        '''
    update.message.reply_text(he_message)
    # Get the user's message
    date = update.message.text

    # Split the message into two numerical inputs
    try:
        date1, date2 = date.split()[1:]
        date1 = str(date1)
        date2 = str(date2)
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid input. ")
        return

    # Calculate the sum of the inputs
    output = compare_days(date1,date2)

    # Send the output back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{output} units😊.")

def usage(update, context):
    he_message= '''
     Please enter date format /usage <space> YYYY/MM/DD<space> ....
        '''
    update.message.reply_text(he_message)
    # Get the user's message
    date = update.message.text

    # Split the message into two numerical inputs
    try:
        date1,date2 = date.split()[1:]
        date1 = str(date1)
        date2= str(date2)

    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid input. ")
        return

    # Calculate the sum of the inputs
    output = Today_energy_consumption(date1)

    # Send the output back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{output} units😊.")

def Present_Status(update,context):
    nth_row = 1
    d = df.iloc[nth_row]
    update.message.reply_text('present status of all the parameters of your house is: ')
    update.message.reply_text(f"{d}")

def Alert(update,context):
    c=allert()
    update.message.reply_text('These are the times when a sudden surges/unusual current flow has taken place: ')
    if c is None:
        update.message.reply_text("None")
    else:
        update.message.reply_text(f"{c}")


def  message_alert(update,context):
    c=messege()
    update.message.reply_text('now you get a messege allert with all parameters ')



# Create an Updater object to receive messages from the bot
updater = Updater(token='6001383871:AAEarO8FdemUkfkus-IwcZfu8wU4_OprfaQ', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('Alert', Alert))
dispatcher.add_handler(CommandHandler('message_alert',message_alert))
usage = CommandHandler('usage',usage)
dispatcher.add_handler(usage)
comparision = CommandHandler('comparision',comparision)
dispatcher.add_handler(comparision)
dispatcher.add_handler(CommandHandler('Present_Status', Present_Status))
pricing = CommandHandler('pricing',pricing)
dispatcher.add_handler(pricing)
# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C to stop it
updater.idle()