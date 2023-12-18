class ReversiGame:
    BOARD_SIZE = 8

    def __init__(self):
        self.board = [[' ' for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.board[3][3] = self.board[4][4] = 'O'
        self.board[3][4] = self.board[4][3] = 'X'
        self.current_player = 'X'
        self.scores = {'X': 2, 'O': 2}

    def get_score(self, player):
        return self.scores.get(player, 0)

    def is_valid_move(self, row, col):
        if not (0 <= row < self.BOARD_SIZE) or not (0 <= col < self.BOARD_SIZE) or self.board[row][col] != ' ':
            return False
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            if self._is_valid_direction(row, col, dr, dc):
                return True
        return False

    def _is_valid_direction(self, row, col, dr, dc):
        opponent = 'O' if self.current_player == 'X' else 'X'
        r, c = row + dr, col + dc
        if not (0 <= r < self.BOARD_SIZE) or not (0 <= c < self.BOARD_SIZE) or self.board[r][c] != opponent:
            return False
        r += dr
        c += dc
        while 0 <= r < self.BOARD_SIZE and 0 <= c < self.BOARD_SIZE:
            if self.board[r][c] == ' ':
                return False
            elif self.board[r][c] == self.current_player:
                return True
            r += dr
            c += dc
        return False

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self._flip_tiles(row, col)
            self._update_scores()
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Negalimas ėjimas")

    def _flip_tiles(self, row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            if self._is_valid_direction(row, col, dr, dc):
                self._flip_direction(row, col, dr, dc)

    def _flip_direction(self, row, col, dr, dc):
        opponent = 'O' if self.current_player == 'X' else 'X'
        r, c = row + dr, col + dc
        while self.board[r][c] == opponent:
            self.board[r][c] = self.current_player
            r += dr
            c += dc

    def _update_scores(self):
        self.scores = {'X': 0, 'O': 0}
        for i in range(8):
            for j in range(8):
                player = self.board[i][j]
                if player in self.scores:
                    self.scores[player] += 1

    def is_game_over(self):
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.board[i][j] == ' ' and self.is_valid_move(i, j):
                    return False
        return True

    def get_winner(self):
        if self.scores['X'] > self.scores['O']:
            return 'X'
        elif self.scores['O'] > self.scores['X']:
            return 'O'
        else:
            return 'Lygiosios'