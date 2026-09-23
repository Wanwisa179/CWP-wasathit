def checkmate(board):
    try:
        rows = board.split('\n')
        rows = [r for r in rows if r]
        if not rows:
            return
        
        n = len(rows)
        king_pos = None
        valid_pieces = ['K', 'Q', 'R', 'B', 'P']
        
        for r in range(n):
            for c in range(len(rows[r])):
                if rows[r][c] == 'K':
                    king_pos = (r, c)
                    break
            if king_pos:
                break
                
        if not king_pos:
            return
            
        kr, kc = king_pos
        is_check = False
        
        straights = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dr, dc in straights:
            r, c = kr + dr, kc + dc
            while 0 <= r < n and 0 <= c < len(rows[r]):
                piece = rows[r][c]
                if piece in valid_pieces:
                    if piece in ['R', 'Q']:
                        is_check = True
                    break
                r += dr
                c += dc
                
        for dr, dc in diagonals:
            r, c = kr + dr, kc + dc
            distance = 1
            while 0 <= r < n and 0 <= c < len(rows[r]):
                piece = rows[r][c]
                if piece in valid_pieces:
                    if piece in ['B', 'Q']:
                        is_check = True
                    if piece == 'P' and distance == 1 and dr == 1:
                        is_check = True
                    break
                r += dr
                c += dc
                distance += 1
                
        if is_check:
            print("Success")
        else:
            print("Fail")
            
    except Exception:
        pass