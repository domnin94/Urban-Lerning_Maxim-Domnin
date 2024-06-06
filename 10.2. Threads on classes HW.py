import time
from collections import defaultdict
from threading import Thread

class Knights(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super(Knights, self).__init__(*args, **kwargs)
        self.name = name
        self.enemies = 100
        self.skill = skill
        self.day = 0


    def run(self):
        print(f'{self.name}, на нас напали!')
        self.day += 1
        self.enemies -= self.skill
        print('{}, сражается {} день(дня), врагов осталось {}'.format(
                self.name, self.day, self.enemies), flush=True)
        while self.enemies > 0:
            time.sleep(2)
            self.day += 1
            self.enemies -= self.skill
            print('{}, сражается {} день(дня), врагов осталось {}'.format(
                self.name, self.day, self.enemies), flush=True)
            if self.enemies == 0:
                print('{} одержал победу, спустя {} дней!'.format(self.name, self.day), flush=True)




sir_lancelot = Knights(name='Sir Lancelot', skill=10)
sir_galahad = Knights(name='Sir Galahad', skill=20)

sir_lancelot.start()
sir_galahad.start()

sir_lancelot.join()
sir_galahad.join()
