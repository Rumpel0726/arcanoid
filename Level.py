from init_glob_vars import *
from Brick import Brick


class Level():
    def __init__(self):
        self.levels = open('data/levels.txt').readlines()
        self.level = ast.literal_eval(self.levels[0])
        self.cnt_brick = 0

    def draw(self, level_bricks):
        self.level = ast.literal_eval(self.levels[0])
        for i in range(len(level_bricks)):
            if level_bricks[i].get_visible() == 1:
                level_bricks[i].draw()
            #print(level_bricks[i].get_visible)

    # Заполним массив кирпичами
    def fill_level(self, level_bricks, l_num):
        self.level = ast.literal_eval(self.levels[l_num])
        # Заполним массив кирпичами
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                # Заполним массив кирпичами если не равно 0
                if self.level[i][j] != 0:
                    brick = Brick()
                    if self.level[i][j] == 1:
                        brick.set_color(st.RED)
                        brick.set_strong(1)
                    if self.level[i][j] == 2:
                        brick.set_color(st.YELLOW)
                        brick.set_strong(2)
                        brick.bonus = 1
                    if self.level[i][j] == 3:
                        brick.set_color(st.ORANGE)
                        brick.bonus = 2
                    if self.level[i][j] == 4:
                        brick.set_color(st.BLUE)
                        brick.bonus = 3
                    brick.set_pos(j, i)
                    level_bricks.append(brick)

    def get_brick_count(self, level_bricks):
        self.cnt_brick = 0
        for i in level_bricks:
            if i.disp == 1:
                self.cnt_brick += 1
        return self.cnt_brick
