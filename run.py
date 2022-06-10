#!/usr/bin/env python

import os

import Game


def main():
    menu = Game.Menu()
    score_board = Game.ScoreBoard()

    # play = Game.Play("#", "*")
    play = Game.Play("█", "░")

    while 1:
        menu.start

        if menu.selected_item == 0:
            # Volta pro menu se a tela for redimencionada
            try:
                play.start
            except:
                pass

            score_board.add_score(play.score[:])

        elif menu.selected_item == 1:
            score_board.start

        else:
            break


if __name__ == "__main__":
    os.environ["TERM"]="linux"
    os.environ["TERMINFO"]="/etc/terminfo"
    main()
