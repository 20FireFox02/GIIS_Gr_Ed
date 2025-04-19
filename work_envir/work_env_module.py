from wind_init_module import pg,clock

from constant_module import FPS

class work_env():
    def work(self):
        pg.display.update()
        clock.tick(FPS)