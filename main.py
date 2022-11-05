from game import Game


def main() -> None:
    game = Game()
    game.key_listener()
    game.game_loop()
    game.mainloop()


if __name__ == "__main__":
    main()