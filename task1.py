class Country:
    def __init__(self, name, currency, official_languages):
        self.__name = name
        self.__currency = currency
        self.__official_languages = official_languages

    @property
    def name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def currency(self):
        return self.__currency

    def set_currency(self, currency):
        if isinstance(currency, int):
            self.__currency = currency

    @property
    def official_languages(self):
        return self.__official_languages

    def set_official_languages(self, official_languages):
        if isinstance(official_languages, int):
            self.__official_languages = official_languages

    def display_info(self):
        print(f'Name: {self.__name}\n'
              f'Currency: {self.__currency}\n'
              f'Official_languages: {self.__official_languages}\n')


switzerland = Country('Switzerland', 'Swiss franc', 'German, French, Italian')
print(switzerland.display_info())