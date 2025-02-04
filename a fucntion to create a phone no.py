
def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=1 ,area=123,first=457,last=333)

print(phone_num)


#an example of keyword arguments