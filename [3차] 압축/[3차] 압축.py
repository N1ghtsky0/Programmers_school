def solution(msg):
    answer = []
    
    # 알파벳 A ~ Z를 담은 사전(book)을 정의
    book = {chr(i):idx for idx, i in enumerate(range(65, 91), 1)}
    
    # 사전에 새로 추가될 단어의 번호
    new_book_idx = 27
    
    # w_idx : 현재 입력의 시작 인덱스
    # c_idx : 다음 글자의 인덱스
    w_idx, c_idx = 0, 1
    
    while True:
        word = msg[w_idx:c_idx]
        if word not in book:
            answer.append(book[word[:-1]])
            book[word] = new_book_idx
            w_idx = c_idx - 1
            new_book_idx += 1
        else:
            c_idx += 1
        
        if c_idx > len(msg):
            answer.append(book[word])
            break
            
    return answer
