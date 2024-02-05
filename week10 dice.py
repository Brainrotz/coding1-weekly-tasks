import random

class DiceRoller:
    def __init__(self, sides, num_dice):
        self.sides = sides
        self.num_dice = num_dice

    def roll(self):
        return [random.randint(1, self.sides) for _ in range(self.num_dice)]

def main():
    try:
        sides, num_dice, num_rolls = map(int, input("Enter sides, number of dice, and number of rolls (comma-separated): ").split(','))
        if sides <= 0 or num_dice <= 0 or num_rolls <= 0:
            raise ValueError("All inputs must be positive integers.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    roller = DiceRoller(sides, num_dice)

    print(f"\nRolling {num_dice} {sides}-sided dice {num_rolls} times:")

    for roll_number in range(1, num_rolls + 1):
        result = roller.roll()
        print(f"Roll {roll_number}: {result}")

if __name__ == "__main__":
    main()
