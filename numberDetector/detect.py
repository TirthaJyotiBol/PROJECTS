import phonenumbers
from phonenumbers import timezone, carrier, geocoder

citizen = input("Are You Indian or American\n")

if(citizen == "Indian"):
    number_in_string = input("Enter Your number with\n")
    num = "+91" + number_in_string

if(citizen == "American"):
    number_in_string = input("Enter Your number with\n")
    num = "+1" + number_in_string


phone = phonenumbers.parse(num)    # Phone number into Integer
time = timezone.time_zones_for_number(phone)
carrier_data = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(phone)
print(time)
print(carrier_data)
print(reg)