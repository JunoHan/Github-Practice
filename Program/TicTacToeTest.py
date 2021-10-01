from TicTacToe import TicTacToe

def PlayingTicTacToe():
    
    a = TicTacToe()
    
    print("TicTacToe 시작!")
    print()
    a.ShowTheBoard()
    
    while not a.IsGameOver():
        print()
        r, c = map(int, input('두고 싶은 곳을 입력해주세요: ' ).split())
        a.PlayGame(r, c)
        
    return True


PlayingTicTacToe()