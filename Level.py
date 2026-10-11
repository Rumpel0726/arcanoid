from init_glob_vars import *
from Brick import make_brick


class Level():
    def __init__(self):
        self.levels = open('data/levels.txt').readlines()
        self.level = ast.literal_eval(self.levels[0])

    def draw(self, level_bricks):
        self.level = ast.literal_eval(self.levels[0])
        for i in range(len(level_bricks)):
            if level_bricks[i].get_visible() == 1:
                level_bricks[i].draw()
            #print(level_bricks[i].get_visible)

    # Заполним массив кирпичами
    def fill_level(self, l_num):
        self.level = ast.literal_eval(self.levels[l_num])
        level_bricks = []
        # Заполним массив кирпичами
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                # Заполним массив кирпичами если не равно 0
                if self.level[i][j] != 0:
                    level_bricks.append(make_brick(self.level[i][j], j, i))
        return level_bricks


# Количество целых кирпичей
def count_visible_bricks(level_bricks):
    cnt_brick = 0
    for i in level_bricks:
        if i.disp == 1:
            cnt_brick += 1
    return cnt_brick


# Уровень пройден, если осталось меньше 10 кирпичей
def is_level_win(level_bricks):
    return count_visible_bricks(level_bricks) < 10
