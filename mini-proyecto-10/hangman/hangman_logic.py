import random

WORDS = ['hormiga', 'babuino', 'tejon', 'murcielago', 'oso', 'castor', 'camello', 'gato', 'almeja', 'cobra', 'pantera', 'coyote', 'cuervo', 'ciervo', 'perro', 'burro', 'pato', 'aguila', 'huron', 'zorro', 'rana', 'cabra', 'ganso', 'halcon', 'leon', 'lagarto', 'llama', 'topo', 'mono', 'alce', 'raton', 'mula', 'salamandra', 'nutria', 'buho', 'panda', 'loro', 'paloma', 'piton', 'conejo', 'carnero', 'rata', 'cuervo', 'rinoceronte', 'salmon', 'foca', 'tiburon', 'oveja', 'mofeta', 'perezoso', 'serpiente', 'araña', 'cigüeña', 'cisne', 'tigre', 'sapo', 'trucha', 'pavo', 'tortuga', 'comadreja', 'ballena', 'lobo', 'wombat', 'cebra']

class HangmanGame:
    def __init__(self):
        self.word = random.choice(WORDS)
        self.guessed_letters = set()
        self.remaining_attempts = 6

    def guess(self, letter):
        if letter in self.guessed_letters:
            return False
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.remaining_attempts -= 1
        return True

    def get_word_state(self):
        return ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def is_game_over(self):
        return self.remaining_attempts == 0 or self.get_word_state() == self.word

    def has_won(self):
        return self.get_word_state() == self.word

    def get_game_state(self):
        return {
            'word_state': self.get_word_state(),
            'guessed_letters': list(self.guessed_letters),
            'remaining_attempts': self.remaining_attempts,
            'game_over': self.is_game_over(),
            'has_won': self.has_won()
        }