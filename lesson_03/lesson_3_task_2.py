from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'iPhone 14', '+7925367888'),
    Smartphone('Samsung', 'Galaxy A54', '+7921333894'),
    Smartphone('Xiaomi', 'Redmi Note 13 Pro', '+7933189774'),
    Smartphone('Honor', 'P60 Pro', '+722698778'),
    Smartphone('Vivo', 'X90 Pro', '+7926378465')
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
