# Nature of planets
planet_dict = {
    'sun': {
        'traits': ['satwik', 'fiery', 'kshatriya'],
        'friends': ['moon', 'mars', 'jup'], 'enemies': ['sat', 'ven'],
        'neutral': ['merc'], 'lord_of': ['leo'], 'mooltrikona': ('leo', 0, 20),
        'exaltation': ('aries', 10), 'debilitation': ('libra', 10), 'sex': 'male',
        'direction': 'east',
        'karaka_of': ['health', 'power', 'father', 'authority', 'fame', 'name',
                      'govt.', 'royalty', 'medicine', 'eyes', 'wool', 'wood',
                      'places of worship', 'commission', 'paternal uncle',
                      'service (6th H)', 'profession (10th H)', 'courage',
                      'patrimony', 'politician', 'doctor', 'physician'],
        'lucky_stone': ['ruby', 'garnet'],
        'lucky_color': ['orange', 'saffron', 'light red'],
        'lucky_num': [1, 10, 19], 'diety': ['siva', 'fire', 'rudra']},
    'moon': {
        'traits': ['satwik', 'watery', 'vaisya'],
        'friends': ['sun', 'merc'], 'enemies': None,
        'neutral': ['mars', 'jup', 'ven', 'sat'], 'lord_of': ['cancer'],
        'mooltrikona': ('tauras', 3, 30), 'exaltation': ('tauras', 3),
        'debilitation': ('scorpio', 3), 'sex': 'female', 'direction': 'north-west',
        'karaka_of': ['mother', 'travel','heart', 'mind', 'emotions', 'blood',
                      'water', 'places', 'liquids', 'gardening', 'salt', 'sea medicine',
                      'changes', 'hernia', 'left eye', 'foreign travel', 'milk',
                      'popularity', 'pearls', 'petroleum products', 'sea food'],
        'lucky_stone': ['pearl', 'moon stone'],
        'lucky_color': ['white', 'silvery hue'], 'lucky_num': [2, 11, 20],
        'diety': ['durga', 'parvati']},
    'mars': {
        'traits': ['tamsik', 'fiery', 'kshatriya'],
        'friends': ['sun', 'moon', 'jup'], 'enemies': ['merc'],
        'neutral': ['ven', 'sat'], 'lord_of': ['aries', 'scorpio'],
        'mooltrikona': ('aries', 0, 12), 'exaltation': ('capricorn', 28),
        'debilitation': ('cancer', 28), 'sex': 'male', 'direction': 'south',
        'karaka_of': ['courage', 'younger brother', 'stamina', 'diseases',
                      'immovable property', 'enemies', 'blood', 'surgery',
                      'science', 'logic', 'lands', 'fire', 'defence', 'maths',
                      'step-mother', 'passions', 'anger', 'hatred', 'violence',
                      'sins', 'vindictiveness', 'lewdness'],
        'lucky_stone': ['red coral', 'garnet'],
        'lucky_color': ['deep red'], 'lucky_num': [9],
        'diety': ['ganpati', 'hanuman', 'shanmukha kartikeya']},
    'merc': {
        'traits': ['rajsik', 'earthy', 'shudra'],
        'friends': ['sun', 'ven'], 'enemies': ['moon'],
        'neutral': ['mars', 'jup', 'sat'], 'lord_of': ['gemini', 'virgo'],
        'mooltrikona': ('virgo', 15, 20), 'exaltation': ('virgo', 15),
        'debilitation': ('pisces', 15), 'sex': 'male eunuch', 'direction': 'north',
        'karaka_of': ['Intelligenc', 'education', 'friends', 'maths', 'adeptness',
                      'business', 'scientific learnings', 'speech', 'publisher',
                      'printer', 'teaching', 'flowers', 'maternal uncle and aunts',
                      'accountancy', 'clerks', 'nephews', 'adopted sons', 'pearls',
                      'oyesters', 'black magic', 'squint eye', 'laughter', 'smell'],
        'lucky_stone': ['emerald', 'onyx'],
        'lucky_color': ['green', 'brown', 'pastel shades'], 'lucky_num': [5, 14, 23],
        'diety': ['vishnu']},
    'jup': {
        'traits': ['satwik', 'fiery', 'benefic'],
        'friends': ['sun', 'moon', 'mars'], 'enemies': ['merc', 'ven'],
        'neutral': ['sat'], 'lord_of': ['sagittarius', 'pisces'],
        'mooltrikona': ('sagittarius', 0, 10), 'exaltation': ('cancer', 5),
        'debilitation': ('capricorn', 5), 'sex': 'male', 'direction': 'north-east',
        'karaka_of': ['sons', 'husband', 'wealth', 'guru','intelligence','education',
                      'astrology', 'logic', 'scriptures knowledge', 'devotion',
                      'control over senses', 'prosperity', 'paternal grand parents',
                      'good virtues', 'religion', 'faith'],
        'lucky_stone': ['yellow sapphire', 'golden topaz'],
        'lucky_color': ['yellow shades', 'lemon', 'light blue'],
        'lucky_num': [3, 12, 21], 'diety': ['indra', 'shiva', 'brahma']},
    'ven': {
        'traits': ['rajasik', 'airy', 'brahmin'],
        'friends': ['sat', 'merc'], 'enemies': ['sun', 'moon'],
        'neutral': ['mars', 'jup'], 'lord_of': ['tauras', 'libra'],
        'mooltrikona': ('libra', 0, 15), 'exaltation': ('pisces', 27),
        'debilitation': ('virgo', 27), 'sex': 'female', 'direction': 'south-east',
        'karaka_of': ['wife', 'marriage', 'pleasures of senses', 'conveyances',
                      'ornaments', 'luxury articles', 'watery places', 'passions',
                      'sexual desires', 'semen', 'silver', 'gems', 'pearls', 'flowers',
                      'comforts', 'erotism', 'perfumes', 'fragrances', 'good clothes',
                      'wife parents', 'maternal grand parents', 'beauty', 'sour',
                      'youth', 'dance', 'music', 'songs', 'drama','black hair',
                      'voluptuousness', 'libido'],
        'lucky_stone': ['diamond', 'white zircon/coral'],
        'lucky_color': ['pink shades', 'cream'],
        'lucky_num': [6, 15, 24], 'diety': ['indrani', 'lakshmi']},
    }


def nature_of_planet(planet_name, nature):
    '''
    param planet_name: 'sun', 'moon', 'mars', 'merc', 'jup', 'ven', 'sat', 'rahu', 'ketu'
    param nature:'friends', 'enemies', 'neutral', 'direction', 'lord_of', 'karaka_of',
                 'lucky_stone','lucky_color', 'lucky_num', 'exaltation', 'debilitation',
                 'mooltrikona'
    param return:list, ('friends', 'enemies', 'neutral', 'direction', 'lord_of',
                        'karaka_of', 'lucky_stone','lucky_color', 'lucky_num');
                 tuple, ('exaltation', 'debilitation', 'mooltrikona') 
    '''
    return planet_dict[planet_name][nature]


if __name__ == "__main__":
    planet_name = 'merc'
    nature = 'karaka_of'

    tuples = ('exaltation', 'debilitation', 'mooltrikona')
    print(f"{planet_name} {nature}:\n")
    for elem in planet_dict[planet_name][nature]:
        if nature in tuples:
            if isinstance(elem, int):
                print(f"{elem} degree")
            else:
                print(f"{elem}")
            print()
        else:
            print(elem)
