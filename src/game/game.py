"""
overall controller for game, entry point
"""

from src.game.engine import GameEngine


def main():
    game = GameEngine()
    game.start()

if __name__ == "__main__":
    main()
