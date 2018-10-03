# -*- coding: utf-8 -*-
"""
To find out what is there in the given 'tithi'. Which category it belongs to.
Whether the tithi is 'malefic' or 'benefic'. Whether certain work or journey can
be commenced on given 'tithi'.
"""


class Tithi:
    '''
    Attributes:
        tithi_comb: dict, certain combinations are inauspicious.
        shunya_tithi: dict, tithi's which are considered shunya (not good).
        avoid_journey: list, tithi's which are avoidable to commence work or journey.
        asp_work: list, tithi's which are avoidable to commence auspicious work.
    '''
    tithi_comb = {(12, 'sun'): ('dagdha', 'hutashan'), (4, 'sun'): 'visha', (11, 'mon'): 'dagdha',
                  (6, 'mon'): ('visha', 'hutashan'), (5, 'tue'): 'dagdha', (7, 'tue'): ('visha', 'hutashan'),
                  (3, 'wed'): 'dagdha', (2, 'wed'): 'visha', (8, 'wed'): 'hutashan', (6, 'thu'): 'dagdha',
                  (8, 'thu'): 'visha', (9, 'thu'): 'hutashan', (8, 'fri'): 'dagdha', (9, 'fri'): 'visha',
                  (10, 'fri'): 'hutashan', (9, 'sat'): 'dagdha', (7, 'sat'): 'visha', (11, 'sat'): 'hutashan'}

    shunya_tithi = {'chaitra': [(8, 'shukla'), (8, 'krishna'), (9, 'shukla'), (9, 'krishna')],
                    'vaisakha': [(12, 'shukla'), (12, 'krishna')],
                    'jyestha': [(13, 'shukla'), (14, 'krishna')], 'asadha': [(6, 'krishna'), (7, 'shukla')],
                    'shravana': [(2, 'shukla'), (2, 'krishna'), (3, 'shukla'), (3, 'krishna')],
                    'bhadra': [(1, 'shukla'), (1, 'krishna'), (2, 'shukla'), (2, 'krishna')],
                    'asvina': [(10, 'shukla'), (11, 'shukla'), (10, 'krishna'), (11, 'krishna')],
                    'kartika': [(5, 'krishna'), (14, 'shukla')],
                    'maghsar': [(7, 'shukla'), (8, 'shukla'), (7, 'krishna'), (8, 'krishna')],
                    'pausa': [(4, 'shukla'), (5, 'shukla'), (4, 'krishna'), (5, 'krishna')],
                    'magha': [(5, 'krishna'), (6, 'shukla')],
                    'phalguna': [(4, 'krishna'), (3, 'shukla')]}

    avoid_journey = [4, 6, 8, 12]

    asp_work = [4, 8, 12, 14]

    def __init__(self, tithi, start, end, day, paksh, month):
        '''
        :param tithi: int; date as per vedic astrology
        :param start: hh:mm:ss; start of the tithi
        :param end: hh:mm:ss; end of the tithi
        :param day: str; english week day
        :param paksh: str; Phase of the moon, waxing moon is 'shukla paksh',
        the waning moon is 'krishna paksh'
        :param month: str; Hindi lunar month; 'chaitra', 'vaisakha', 'jyeshtha', 'asadha', 'shravana', 'bhadra',
         'asvina', 'kartika', 'maghsar', 'pausa', magha', 'phalguna'
        '''
        self.tithi = tithi
        self.start = start
        self.end = end
        self.day = day
        self.paksh = paksh
        self.month = month

    def is_good_to_start(self, dt_list=avoid_journey):
        '''
        Returns:
            'NO' for inauspicious tithi, 'YES' otherwise
        '''
        if self.tithi in dt_list and self.paksh == 'shukla':
            return "NO"
        else:
            return 'YES'

    def is_good_to_start_auspicious_work(self, dt_list=asp_work):
        '''
        Returns:
            'NO' for inauspicious tithi, 'YES' otherwise
        '''
        if self.tithi in dt_list:
            return 'No'
        else:
            return 'YES'

    # TODO Add def for religious propitiation, need time module ; pp-14 (Scientific Analysis of Horoscope)

    def get_nature_of_tithi(self, dt_dict=tithi_comb):
        '''
        Returns:
            'tuple' of tithi nature if malefic, 'Not malefic' otherwise
        '''
        k = (self.tithi, self.day)
        if k in dt_dict:
            return dt_dict[k]
        else:
            return 'Not Malefic'

    # TODO karna (half of tithi)
    # TODO yoga

    def __str__(self):
        return(f"({self.tithi}, {self.start}, {self.end}, {self.day}, {self.paksh}, {self.month})")


if __name__ == "__main__":
    foo = Tithi(6,0, 0, 'mon', 'krishna', 'jyestha')
    assert foo.is_good_to_start() == 'YES'
    assert foo.is_good_to_start_auspicious_work() == 'YES'
    foo_1 = Tithi(6, 0, 0, 'mon', 'shukla', 'jyestha')
    assert foo_1.is_good_to_start() == 'NO'
    assert foo_1.is_good_to_start_auspicious_work() == 'YES'
    assert foo_1.get_nature_of_tithi() == ('visha', 'hutashan')
    print(foo_1)

