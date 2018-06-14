def city_country(c_name,c_country):
    string_name = c_name + ',' + c_country
    return string_name


while True:
    print("\nPlease input the city_name and city of country:")
    c_name = input('请输入城市名：')
    if c_name == 'q':
        break
    c_country = input('请输入城市所属的国家：')
    if c_country == 'q':
        break


    final_name = city_country(c_name,c_country)
    print(final_name.title())
