import phonenumbers
number = input()
from phonenumbers import geocoder
number_country=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(number_country,"en"))

from phonenumbers import carrier
number_service = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(number_service,"en"))