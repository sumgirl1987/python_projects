from address import Address
from mailing import Mailing

to_address = Address('123456', 'Moscow', 'Vinogradnaya', 28, 115)
from_address = Address('654321', 'Saint-Petersburg', 'Verbnnaya', 30, 29)
full_mail = Mailing(to_address, from_address, 2500, '158974632')

print(f"Отправление {full_mail.track} из {full_mail.from_address.zipcode}, "
      f"{full_mail.from_address.city}, {full_mail.from_address.street}, "
      f"{full_mail.from_address.house} - {full_mail.from_address.apartment}"
      f" в {full_mail.to_address.zipcode}, {full_mail.to_address.city}, "
      f"{to_address.street}, {to_address.house} - {to_address.apartment}."
      f" Стоимость {full_mail.cost} рублей.")
