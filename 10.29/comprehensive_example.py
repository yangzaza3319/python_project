# 综合案例

class Game(object):
    top_score = 0 

    @staticmethod
    def show_help():
        print("主线任务:让僵尸走进房间")
    
    @classmethod
    def show_top_score(cls):
        print("游戏最高分是 %d" % cls.top_score)
    def __init__(self,plyer_name):
        self.player_name = plyer_name
    def start_game(self):
        print("[%s] 开始游戏..." %self.player_name)
        Game.top_score = 999

Game.show_help()
Game.show_top_score()

game = Game("小明")
game.start_game()
Game.show_top_score()
"""
输出
    主线任务:让僵尸走进房间
    游戏最高分是 0
    [小明] 开始游戏...
    游戏最高分是 999
"""