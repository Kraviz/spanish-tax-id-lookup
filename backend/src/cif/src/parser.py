import pandas as pd
import os
from django.conf import settings


class Parser(object):

    def __init__(self, cif):

        self.cif = cif

    @property
    def organization(self):
        s = self.cif[0].lower()

        mapper = pd.read_csv(os.path.join(settings.BASE_DIR, 'cif/src/data/organization_mapper.csv'),
                             index_col=0, sep=';', squeeze=True)

        if s in mapper.index:
            return mapper.ix[s]

        return 'Organization Type Not Found'

    @property
    def province(self):
        s = self.cif[1:3]

        mapper = pd.read_csv(os.path.join(settings.BASE_DIR, 'cif/src/data/province_mapper.csv'),
                             index_col=0, sep=';', squeeze=True)
        mapper.index = mapper.index.astype('str')

        if s in mapper.index:
            return mapper.ix[s]

        return 'Province Not Found'

    @property
    def correlative_number(self):
        return self.cif[3:8]

    @property
    def control_digit(self):

        return self.cif[8]

    @property
    def validator(self):

        digits = self.cif[1:8]

        evens = [digits[1], digits[3], digits[5]]
        a = sum(map(int, evens))

        odds = [digits[0], digits[2], digits[4], digits[6]]
        b = list(map(lambda x: str(2*int(x)), odds))
        b = sum(list(map(lambda x: sum([int(i) for i in x]), b)))

        c = str(sum([a, b]))

        if c == 0:
            r = 0
        else:
            r = 10 - int(c[-1])

        _list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        return _list[r-1]
