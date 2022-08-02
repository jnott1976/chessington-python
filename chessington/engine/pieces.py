from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    target_square = 0
    target_square_2 = 0
    def get_available_moves(self, board) -> List[Square]:
        global target_square, target_square_2
        current_square = board.find_piece(self)
        if current_square == Square.at(1, 0) and self.player == Player.WHITE:
            target_square = Square.at(current_square.row+2,current_square.col)
        if current_square == Square.at(1, 1) and self.player == Player.WHITE:
            target_square = Square.at(current_square.row+2,current_square.col)
        if current_square == Square.at(1, 2) and self.player == Player.WHITE:
            target_square = Square.at(current_square.row+2,current_square.col)
        if current_square == Square.at(1, 3) and self.player == Player.WHITE:
            target_square = Square.at(current_square.row+2,current_square.col)
        if current_square == Square.at(1, 4) and self.player == Player.WHITE:
            target_square = Square.at(current_square.row+2,current_square.col)
        if current_square == Square.at(1, 5) and self.player == Player.WHITE:
            target_square = Square.at(current_square.row+2,current_square.col)
        if current_square == Square.at(1, 6) and self.player == Player.WHITE:
            target_square = Square.at(current_square.row+2,current_square.col)
        elif self.player == Player.WHITE:
            target_square_2 = Square.at(current_square.row+1,current_square.col)
        if current_square == Square.at(6, 0) and self.player == Player.BLACK:
            target_square = Square.at(current_square.row-2,current_square.col)
        if current_square == Square.at(6, 1) and self.player == Player.BLACK:
            target_square = Square.at(current_square.row-2,current_square.col)
        if current_square == Square.at(6, 2) and self.player == Player.BLACK:
            target_square = Square.at(current_square.row-2,current_square.col)
        if current_square == Square.at(6, 3) and self.player == Player.BLACK:
            target_square = Square.at(current_square.row-2,current_square.col)
        if current_square == Square.at(6, 4) and self.player == Player.BLACK:
            target_square = Square.at(current_square.row-2,current_square.col)
        if current_square == Square.at(6, 5) and self.player == Player.BLACK:
            target_square = Square.at(current_square.row-2,current_square.col)
        if current_square == Square.at(6, 6) and self.player == Player.BLACK:
            target_square = Square.at(current_square.row-2,current_square.col)
        elif self.player == Player.BLACK:
            target_square_2 = Square.at(current_square.row-1,current_square.col)
        return [target_square, target_square_2]


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []