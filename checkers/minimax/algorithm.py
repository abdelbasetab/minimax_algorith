from copy import deepcopy
import pygame
from checkers.constants import RED, WHITE




def minimax(position, depth, max_player,game):

    if depth == 0 or position.winner() != None:

        return position.evaluate(), position
    
    if max_player:
        maxEvalition = float('-inf') # - infinity
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0] # recursiv call evaluation to run ELSE (false) part 
            maxEvalition = max(maxEvalition, evaluation)
            if maxEvalition == evaluation:
                best_move = move
        return maxEvalition, best_move
    else :
        minEvalition = float('inf') # - infinity
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0] # recursiv call evaluation
            minEvalition = min(minEvalition, evaluation)
            if minEvalition == evaluation:
                best_move = move
        return minEvalition, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece,move[0],move[1])
    if skip:
        board.remove(skip)
    
    return board




def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # to see the future methode
            draw_moves(game,board,piece) # see how minimax work 

            temp_board = deepcopy(board) # deep copy == copy just the content not the referrence also 
            tem_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(tem_piece, move, temp_board, game, skip)
            moves.append((new_board))
    return moves



def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win,(0,255,0),(piece.x,piece.y),50,5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
   # pygame.time.delay(100) 
