import chess

piece_values = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

pawn_table_white = [
    0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5,  5, 10, 25, 25, 10,  5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5, -5,-10,  0,  0,-10, -5,  5,
    5, 10, 10,-20,-20, 10, 10,  5,
    0,  0,  0,  0,  0,  0,  0,  0
]
pawn_table_black = list(reversed(pawn_table_white))

def eval_piece(piece: chess.Piece, square: chess.Square) -> int:
    mapping = []
    if piece.piece_type == chess.PAWN:
        mapping = pawn_table_white if piece.color == chess.WHITE else pawn_table_black
    else:
        return 0
    return mapping[square]


def eval_board(board: chess.Board) -> float:
    print(board)
    total = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        value = piece_values[piece.piece_type] + eval_piece(piece, square)
        total += value if piece.color == chess.WHITE else -value
    return total

print(eval_board(chess.Board()))