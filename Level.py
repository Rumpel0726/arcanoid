from init_glob_vars import *
from Brick import make_brick


class Level():
    def draw(self, level_bricks):
        for i in range(len(level_bricks)):
            if level_bricks[i].get_visible() == 1:
                level_bricks[i].draw()
            #print(level_bricks[i].get_visible)


# Чтение уровней из файла (один раз при запуске)
def load_levels(file_name_):
    lines = open(file_name_).readlines()
    levels = []
    for i in range(len(lines)):
        levels.append(parse_level(lines[i]))
    return levels


# Строка из файла -> матрица кодов кирпичей
def parse_level(line_):
    return ast.literal_eval(line_)


# Заполним массив кирпичами по матрице уровня
def make_level_bricks(level_):
    level_bricks = []
    for i in range(len(level_)):
        for j in range(len(level_[i])):
            # Заполним массив кирпичами если не равно 0
            if level_[i][j] != 0:
                level_bricks.append(make_brick(level_[i][j], j, i))
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
