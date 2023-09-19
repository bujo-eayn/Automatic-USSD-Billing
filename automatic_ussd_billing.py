import os
import time

# Define the USSD code to be dialed
ussd_code = "*100%23"
# m-pesa services option
mpesa_option=10
# lipa na m-pesa option
lipa_na_mpesa_option=6
# buy good and services option
buy_good_and_services_option=2
# Define the till number
till_number = "000000"
# define amount
amount=0

# Use the os.system() method to dial the USSD code
os.system(f"adb shell am start -a android.intent.action.CALL -d tel:{ussd_code}")
# Wait for the USSD code to load
time.sleep(3)

# Send option 1 key event to select "M-Pesa" option
os.system("adb shell input keyevent 8")  # send "1"
os.system("adb shell input keyevent 66")  # send "enter"

# Send option 10 key event to select "M-PESA services" option
os.system(f"adb shell input text {mpesa_option}")
os.system("adb shell input keyevent 66")  # send "enter"

# Send option 6 key event to select "Lipa Na M-PESA" option
os.system(f"adb shell input text {lipa_na_mpesa_option}")
os.system("adb shell input keyevent 66")  # send "enter"

# Send option 2 key event to select "Buy Good and Services" option
os.system(f"adb shell input text {buy_good_and_services_option}")
os.system("adb shell input keyevent 66")  # send "enter"

# Entering the till number
os.system(f"adb shell input text {till_number}")
os.system("adb shell input keyevent 66")  # send "enter"

# Entering the ampount
os.system(f"adb shell input text {amount}")
os.system("adb shell input keyevent 66")  # send "enter"

# Entering PIN number
pin_number=input("Enter your PIN number : ")
os.system(f"adb shell input text {pin_number}")
os.system("adb shell input keyevent 66")  # send "enter"

# confirming the transaction
choice=1
os.system(f"adb shell input text {choice}")
os.system("adb shell input keyevent 66")  # send "enter"

# Display payment confirmation message
print("Payment confirmed. Thank you for using our service.")