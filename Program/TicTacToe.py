class TicTacToe:
    def __init__(self):
        self.board = []
        self.cnt = 0
        for i in range(3):
            tmp = []
            for j in range(3):
                tmp.append('')
            self.board.append(tmp)

    def ShowTheBoard(self):    # 게임 생성 또는 게임 진행 시 판 현황 공개
        for i in range(3):
            for j in range(3):
                print(f'|_{self.board[i][j]}_|', end='')
            print()

    def Check1(self):    # 추후 알고리즘 수정 요망
        cnt1, cnt2 = 1, 1
        tmp1, tmp2 = self.board[0][0], self.board[0][2]

        if tmp1 != '':    # 대각선 비교
            for i in range(1, 3):
                if self.board[i][i] == tmp1:
                    cnt1 += 1
            if cnt1 == 3:
                return True

        if tmp2 != '':
            for i in range(1, 3):
                if self.board[i][2-i] == tmp2:
                    cnt2 += 1
            if cnt2 == 3:
                return True

        cnt1, cnt2 = 1, 1

        for i in range(3):
            tmp1, tmp2 = self.board[i][0], self.board[0][i]

            if tmp1 != '':
                for j in range(1, 3):
                    if self.board[i][j] == tmp1:
                        cnt1 += 1
                if cnt1 == 3:
                    return True

            if tmp2 != '':
                for j in range(1, 3):
                    if self.board[j][i] == tmp2:
                        cnt2 += 1
                if cnt2 == 3:
                    return True

        return False

    def Check2(self):    # 무승부 확인
        return (self.cnt == 9)

    def WhoseTurn(self):
        if self.cnt % 2 != 0:
            return True
        else:
            return False

    def IsGameOver(self):
        if self.Check1():
            if self.WhoseTurn():
                print('p1이 승리하였습니다.')
                return True
            else:
                print('p2가 승리하였습니다.')
                return True
        elif self.Check2():
            print('무승부입니다.')
            return True
        else:
            return False
        
    def PlayGame(self, a, b):    # 게임 진행, (a, b)에 표기
        if self.board[a][b] == '':
            if self.WhoseTurn():
                self.board[a][b] = 'O'
            else:
                self.board[a][b] = 'X'
            self.cnt += 1
            self.ShowTheBoard()
        else:
            print('이미 이전에 둔 적이 있습니다.')
            self.ShowTheBoard()
            return False
        return True