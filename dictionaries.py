def run():
    my_dictionary = {
       'key1': 1,
       'key2': 2,
       'key3': 3,
    }
    print(my_dictionary)

    country_poblation = {
        'Argentina': 44_938_712,
        'Brasil': 210_147_125,
        'Colombia': 50_372_424,
    }
    # print(country_poblation['Argentina'])
    # for country in country_poblation.values():
    #     print(country)
    for country, poblation in country_poblation.items():
        print(f'{country} has {poblation}')
    
if __name__ == '__main__':
    run()