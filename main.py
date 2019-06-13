
from libs.user import User


def main():
    """
    Create user object and use the C-Car API.
    Test application and prepare real time use cases
    :return:
    """
    Driver = User(car='audiA3', mode='kierowca')
    Driver.connect_to_device()
    Driver.get_actual_gas_level()
    Driver.get_actual_speed()

    print 'speed: %s, gas level: %s' % (Driver.speed, Driver.gas)


if __name__ == '__main__':
    main()