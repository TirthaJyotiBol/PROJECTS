import phonenumbers
from phonenumbers import timezone, carrier, geocoder

code = input("Enter Your Country Code \n")              # country phone code

number_in_string = input("Enter Your number with\n")
num = code + number_in_string                           # code concatanated with phone number

phone = phonenumbers.parse(num)                         # Phone number with Nationality
time = timezone.time_zones_for_number(phone)            # Timezone -> Asia/Calcutta
carrier_data = carrier.name_for_number(phone, "en")     # Respective Sim Card company
region = geocoder.description_for_number(phone, "en")   # Country

print(phone)
print(time)
print(carrier_data)
print(region)
