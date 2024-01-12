import random

class Bot:
    def __init__(self):
        self.board = [[0 for x in range(4)] for y in range(4)]
        self.score = 0
        self.move_count = 0

    def move(self):
        possible_moves = self.get_possible_moves()
        if possible_moves:
            move = random.choice(possible_moves)
            self.make_move(move)

    def get_possible_moves(self):
        possible_moves = []
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == 0:
                    possible_moves.append((row, col))
        return possible_moves

    def make_move(self, move):
        row, col = move
        self.board[row][col] = self.board[row-1][col-1] + 1
        self.board[row-1][col-1] = 0
        self.score += self.board[row][col]
        self.move_count += 1

    def __str__(self):
        output = ""
        for row in range(4):
            for col in range(4):
                output += str(self.board[row][col]) + " "
            output += "\n"
        return output

if __name__ == "__main__":
    bot = Bot()
    while True:
        bot.move()
        print(bot)
        if bot.score >= 2048:
            print("You won!")
            break