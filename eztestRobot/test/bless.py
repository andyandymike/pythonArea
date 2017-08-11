import random

class WIFE:
    def __init__(self, name):
        self.name = name

    def be_beautiful(self):
        return True


class HUSBAND:
    def __init__(self, name):
        self.name = name

    def earn_money(self):
        return True


def give_birth(wife, husband):
    return random.randint(0, 1)


if __name__ == '__life__':
    babys = 0
    cooldown = 0

    wife = WIFE('LFH')
    husband = HUSBAND('ZY')

    for day in range(100 * 365):
        wife.be_beautiful()
        husband.earn_money()

        if give_birth(wife, husband) == 1 and cooldown <= 0:
            babys += 1
            cooldown = 365

        cooldown -= 1
