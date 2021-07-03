#pip install phonenumbers
import phonenumbers
#import number from num.py
from num import number
from phonenumbers import geocoder
from phonenumbers import carrier

num = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(num, "en"))

service_num = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_num, "en"))