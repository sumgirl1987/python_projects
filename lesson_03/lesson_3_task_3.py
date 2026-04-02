from address import Address
from mailing import Mailing

full_mail = Mailing('Moscow', 'Saint-Petersburg', 2500, '158974632')
to_address = Address('123456', 'Moscow', 'Vinogradnaya', 28, 115)
from_address = Address('654321', 'Saint-Petersburg', 'Verbnnaya', 30, 29)

print(f"Отправление {full_mail.track} из {from_address.zipcode}, "
      f"{from_address.city}, {from_address.street}, {from_address.house} - "
      f"{from_address.apartment} в {to_address.zipcode}, {to_address.city}, "
      f"{to_address.street}, {to_address.house} - {to_address.apartment}."
      f" Стоимость {full_mail.cost} рублей.")
