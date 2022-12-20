def solution(m, n, board):
    answer = 0

    # 4블록으로 사라지는 경우에 값을 변경해주어야 하는데 문자열은 인덱스 번호로 변경이 안 되므로 리스트로 변환해서 저장한다.
    board = [list(row) for row in board]

    # score는 board에서 사라지는 블록의 총 개수
    score = -1

    # score가 0이면 사라지는 블록이 없다는 뜻이므로 게임 종료
    while score != 0:

        # 사라지는 블록의 좌표값을 저장하는 집합으로 중복되는 블럭의 개수를 두번 세는걸 방지하기 위해 set으로 선언해준다.
        fourBlock = set([])

        # 4칸씩 살펴볼 때 (m-1)행 (n-1)열 까지만 살펴보면 된다.
        for row in range(m-1):
            for col in range(n-1):
                # "*"은 블럭이 없는 공백자리로 검사할 필요가 없다.
                if board[row][col] == "*": continue
                if len({board[row][col], board[row][col + 1], board[row + 1][col], board[row + 1][col + 1]}) == 1:
                    fourBlock.add((row, col))
                    fourBlock.add((row, col+1))
                    fourBlock.add((row+1, col))
                    fourBlock.add((row+1, col+1))

        score = len(fourBlock)
        answer += score

        # 사라지는 블록을 표시해준다.
        for deleteBlock in fourBlock:
            board[deleteBlock[0]][deleteBlock[1]] = "*"

        # 각 열의 맨 밑에서 부터 살펴보면서 "*"의 최초 위치(blank)를 탐색해준다.
        # 그 후에 최초 위치부터 위로 올라가면서 블럭이 있을 경우 서로의 자리를 바꿔준다. ("*" <-> block)
        # 블럭 교체 후에 최초 위치는 이제 빈칸이 아니므로 빈칸의 행 인덱스에 -1을 해준다.(블럭의 최초 위치가 한 칸 올라가게 됨)
        for _ in range(n):
            blank = -1
            for idx in range(m-1, -1, -1):
                if board[idx][_] == "*":
                    blank = idx
                    break

            for fillIdx in range(blank, -1, -1):
                if board[fillIdx][_] != "*":
                    board[blank][_], board[fillIdx][_] = board[fillIdx][_], board[blank][_]
                    blank -= 1

    return answer


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
