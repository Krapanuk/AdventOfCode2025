import day31
import day32

def test_findOneInvalid1():
    result = day31.findHighestJoltageCombi('987654321111111')
    assert result == 98

def test_findOneInvalid2():
    result = day31.findHighestJoltageCombi('811111111111119')
    assert result == 89

def test_findOneInvalid3():
    result = day31.findHighestJoltageCombi('234234234234278')
    assert result == 78

def test_findOneInvalid4():
    result = day31.findHighestJoltageCombi('818181911112111')
    assert result == 92



def test_findOneInvalid21():
    result = day32.findHighestJoltageCombi('987654321111111')
    assert result == 987654321111

def test_findOneInvalid22():
    result = day32.findHighestJoltageCombi('811111111111119')
    assert result == 811111111119

def test_findOneInvalid23():
    result = day32.findHighestJoltageCombi('234234234234278')
    assert result == 434234234278

def test_findOneInvalid24():
    result = day32.findHighestJoltageCombi('818181911112111')
    assert result == 888911112111