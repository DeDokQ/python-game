class Stats():

    def __init__(self):
        """инициализация статистики"""
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Динамическая статистика"""
        self.player_health = 3
        self.score = 0
        self.waves = 0