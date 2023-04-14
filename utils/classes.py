import datetime


class Operetion:
    """
    Инициализируем элемент класа
    """
    def __init__(self, state, date_, amount, name, description, from_, to):
        self.state = state
        self.date = datetime.date.fromisoformat(date_[0:10])
        self.amount = amount
        self.name = name
        self.description = description
        self.from_ = from_
        self.to = to


    def separetion(self):
        """
        Маскирует номера отправителя и получателя, в зависимости карта это или счет.
        """
        # Проверяем, есть адрес отправления или нет
        if self.from_ is not None:
            # Проверяем, счет это или карта
            if self.from_[0:4] == 'Счет':
                number_card_from = self.from_[-20:]
                tupe_card_from = self.from_[:-20]
            else:
                number_card_from = self.from_[-16:]
                tupe_card_from = self.from_[:-16]

            # Маскирвем номер
            if len(number_card_from) == 20:
                number_card_from = '**' + number_card_from[-4:] + " "
            elif len(number_card_from) == 16:
                number_card_from = number_card_from[0:4] + ' ' + \
                                    number_card_from[4:6] + '**' + \
                                    ' ' + '****' + ' ' + number_card_from[-4:] + " "
            self.from_ = tupe_card_from + number_card_from
        else:
            self.from_ = ''

        # Проверяем, есть адрес получания или нет
        if self.to is not None:
            # Проверяем, счет это или карта
            if self.to[0:4] == 'Счет':
                number_card_to = self.to[-20:]
                tupe_card_to = self.to[:-20]
            else:
                number_card_to = self.to[-16:]
                tupe_card_to = self.to[:-16]
            # Маскирвем номер
            if len(number_card_to) == 20:
                number_card_to = '**' + number_card_to[-4:]
            elif len(number_card_to) == 16:
                number_card_to = number_card_to[0:4] + ' ' + \
                                  number_card_to[4:6] + '**' + \
                                  ' ' + '****' + ' ' + number_card_to[-4:]
            self.to = tupe_card_to + number_card_to

    def return_operation(self):
        """
        Возвращаем информацию в нужной нам форме
        """
        return f'''{self.date.strftime('%d.%m.%Y')} {self.description}
{self.from_}-> {self.to}
{self.amount} {self.name}
'''
