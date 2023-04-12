import datetime


class Operetion:
    """

    """
    def __init__(self, state, date_, amount, name, description, from_=None, to=None):
        self.state = state
        self.date = datetime.date.fromisoformat(date_[0:10])
        self.amount = amount
        self.name = name
        self.description = description
        self.from_ = from_
        self.to = to
        self.tupe_card_from = ''
        self.number_card_from = ''
        self.tupe_card_to = ''
        self.number_card_to = ''

    def separetion(self):
        if self.from_ is not None:
            if self.from_[0:4] == 'Счет':
                self.number_card_from = self.from_[-20:]
                self.tupe_card_from = self.from_[:-20]
            else:
                self.number_card_from = self.from_[-16:]
                self.tupe_card_from = self.from_[:-16]
        if len(self.number_card_from) == 20:
            self.number_card_from = '**' + self.number_card_from[-4:] + " "
        elif len(self.number_card_from) == 16:
            self.number_card_from = self.number_card_from[0:4] + ' ' + \
                                    self.number_card_from[4:6] + '**' + \
                                    ' ' + '****' + ' ' + self.number_card_from[-4:] + " "
        if self.to is not None:
            if self.to[0:4] == 'Счет':
                self.number_card_to = self.to[-20:]
                self.tupe_card_to = self.to[:-20]
            else:
                self.number_card_to = self.to[-16:]
                self.tupe_card_to = self.to[:-16]
        if len(self.number_card_to) == 20:
            self.number_card_to = '**' + self.number_card_to[-4:]
        elif len(self.number_card_to) == 16:
            self.number_card_to = self.number_card_to[0:4] + ' ' + \
                                  self.number_card_to[4:6] + '**' + \
                                  ' ' + '****' + ' ' + self.number_card_to[-4:]

    def print_operation(self):
        return f'''{self.date.strftime('%d.%m.%Y')} {self.description}
{self.tupe_card_from}{self.number_card_from}-> {self.tupe_card_to}{self.number_card_to}
{self.amount} {self.name}
'''
