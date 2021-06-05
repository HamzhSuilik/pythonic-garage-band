from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band,Guitarist,Bassist,Drummer,Musician


def test_version():
    assert __version__ == '0.1.0'

def test_0():
    actual = ''
    expected = ''
    assert expected == actual

# A Band instance should have a name attribute which is a string.
def test_1():
    band = Band('first Band')
    actual = band.name
    expected = 'first Band'
    assert expected == actual

# A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
def test_2():
    list = [Guitarist('Guitar'),Bassist('joni'),Drummer('Haman')]
    band = Band('first Band',list)
    actual = [member.name for member in band.members]
    expected = [member.name for member in list]
    assert actual == expected

# A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
def test_3():
    list = [Guitarist('Guitar'),Bassist('joni'),Drummer('Haman')]
    band = Band('first Band',list)
    actual = band.play_solos()
    expected = [arr.play_solo() for arr in list]
    assert  actual == expected

# A Band instance should have appropriate __str__ and __repr__ methods.
def test_4():
    list = [Guitarist('Guitar'),Bassist('joni'),Drummer('Haman')]
    band = Band('first Band',list)
    actual = band.__str__()
    expected = """Band Name : first Band
Members names : 
Guitar
joni
Haman"""
    assert  actual == expected
    actual = band.__repr__()
    expected = 'Name : first Band'
    assert  actual == expected
# A Band should have a class method to_list which returns a list of previously created Band instances
def test_5():
    list = [Guitarist('Guitar'),Bassist('joni'),Drummer('Haman')]
    band = Band('first Band',list)
    actual = band.to_list()
    expected = list
    assert  actual == expected
# Musician Subclass Tests
# Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
def test_6():
    guitarist = Guitarist('name')
    actual = guitarist.__str__()
    expected = """Name : name 
 Musical Instrument : Guitar 
 Sound : Rhythm"""
    assert  actual == expected
# Each kind of Musician instance should have a get_instrument method that returns string.
def test_7():
    guitarist = Guitarist('name')
    actual = guitarist.get_instrument()
    expected = 'Guitar'
    assert  actual == expected
# Each kind of Musician instance should have a play_solo method that returns string.
def test_8():
    guitarist = Guitarist('name')
    actual = guitarist.play_solo()
    expected = 'Rhythm'
    assert  actual == expected