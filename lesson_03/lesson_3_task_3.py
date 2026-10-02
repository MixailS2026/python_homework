from address import Address
from mailing import Mailing


from_adr = Address("656039", "Барнаул", "Советской Армии", "133Б", "148")
to_adr = Address("630000", "Новосибирск", "Ленина", "48", "115")


shipment = Mailing(
    to_address=to_adr,
    from_address=from_adr,
    cost=450.50,
    track="RU1234567899",
)


addr_from = shipment.from_address
addr_to = shipment.to_address

print(
    f"Отправление {shipment.track} "
    f"из {addr_from.index}, {addr_from.city}, {addr_from.street}, "
    f"{addr_from.house} - {addr_from.apartment} "
    f"в {addr_to.index}, {addr_to.city}, {addr_to.street}, "
    f"{addr_to.house} - {addr_to.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)
