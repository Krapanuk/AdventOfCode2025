import day21
import day22

def test_isInvalid():
    result = day21.isInvalid('1188511885')
    assert result == 1

def test_findOneInvalid():
    rangesArray = [['1188511880', '1188511890']]
    result = day21.findInvalidIDs(rangesArray)
    assert result == 1188511885

def test_findNoneInvalid():
    rangesArray = [['1188511880', '1188511884']]
    result = day21.findInvalidIDs(rangesArray)
    assert result == 0

def test_day2_twoInvalid():
    rangesArray = [['95', '115']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 210

def test_day2_same():
    result = day22.isEachNumberTheSame('1111',1,4)
    assert result == 1

def test_day2_NotTheSameStarting():
    result = day22.isEachNumberTheSame('2111',1,4)
    assert result == 0

def test_day2_NotTheSameEnding():
    result = day22.isEachNumberTheSame('1112',1,4)
    assert result == 0

def test_day2_invalidIDs1():
    rangesArray = [['11', '22']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 33

def test_day2_invalidIDs2():
    rangesArray = [['95', '115']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 210

def test_day2_invalidIDs3():
    rangesArray = [['998', '1012']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 2009

def test_day2_invalidIDs4():
    rangesArray = [['1188511880', '1188511890']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 1188511885

def test_day2_invalidIDs5():
    rangesArray = [['222220', '222224']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 222222

def test_day2_invalidIDs6():
    rangesArray = [['1698522', '1698528']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 0

def test_day2_invalidIDs7():
    rangesArray = [['446443', '446449']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 446446

def test_day2_invalidIDs8():
    rangesArray = [['38593856', '38593862']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 38593859

def test_day2_invalidIDs9():
    rangesArray = [['565653', '565659']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 565656

def test_day2_invalidIDs10():
    rangesArray = [['824824821', '824824827']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 824824824

def test_day2_invalidIDs11():
    rangesArray = [['2121212118', '2121212124']]
    result = day22.findInvalidIDs(rangesArray)
    assert result == 2121212121