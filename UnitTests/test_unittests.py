import day12  # Name deiner Datei ohne .py anpassen


def test_empty():
    result = day12.findZeros([])
    assert result == 0


def test_moveRight():
    rotations_list = [['R', 10]]  # 50 -> 60
    result = day12.findZeros(rotations_list)
    assert result == 0


def test_moveLeft():
    rotations_list = [['L', 10]]  # 50 -> 40
    result = day12.findZeros(rotations_list)
    assert result == 0


def test_moveRightTo100():
    rotations_list = [['R', 50]]
    result = day12.findZeros(rotations_list)
    assert result == 1


def test_moveLeftTo0():
    rotations_list = [['L', 50]]
    result = day12.findZeros(rotations_list)
    assert result == 1


def test_moveRigthTo100_moveLeftTo0():
    rotations_list = [['R', 50], ['L', 50], ['R', 50]]
    result = day12.findZeros(rotations_list)
    assert result == 2


def test_moveRigthTo100_moveLeftRightTo100_moveLeft():
    rotations_list = [['R', 50], ['L', 50], ['R', 50], ['L', 50]]
    result = day12.findZeros(rotations_list)
    assert result == 2


def test_flipZeroLiftRightLeftRight():
    rotations_list = [['L', 50], ['L', 50], ['R', 50], ['R', 50], ['R', 50]]
    result = day12.findZeros(rotations_list)
    assert result == 3


def test_passZeroRightManyTimes():
    rotations_list = [['R', 150]]
    result = day12.findZeros(rotations_list)
    assert result == 2


def test_passZeroLeftManyTimes():
    rotations_list = [['L', 150]]
    result = day12.findZeros(rotations_list)
    assert result == 2


def test_passZeroRightVeryManyTimes():
    rotations_list = [['R', 350]]
    result = day12.findZeros(rotations_list)
    assert result == 4


def test_passZeroLeftVeryManyTimes():
    rotations_list = [['L', 350]]
    result = day12.findZeros(rotations_list)
    assert result == 4


def test_passZeroLeftRightVeryManyTimes():
    rotations_list = [['L', 350], ['R', 300]]
    result = day12.findZeros(rotations_list)
    assert result == 7