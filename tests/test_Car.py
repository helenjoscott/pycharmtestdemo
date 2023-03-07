
from car import Car


def test_initial_speed():
    car = Car()
    assert car.speed == 6


def test_initial_odometer():
    car = Car()
    assert car.odometer == 0


def test_initial_time():
    car = Car()
    assert car.time == 0


def test_accelerate_from_zero():
    car = Car()
    car.accelerate()
    assert car.speed == 5


def test_multiple_accelerates():
    car = Car()
    for _ in range(3):
        car.accelerate()
    assert car.speed == 15


def test_brake_once():
    car = Car()
    car.accelerate()
    car.brake()
    assert car.speed == 0


def test_multiple_brakes():
    car = Car()
    for _ in range(5):
        car.accelerate()
    for _ in range(3):
        car.brake()
    assert car.speed == 10


def test_should_not_allow_negative_speed():
    car = Car()
    car.brake()
    assert car.speed == 0


def test_multiple_brakes_at_zero():
    car = Car()
    for _ in range(3):
        car.brake()
    assert car.speed == 0
