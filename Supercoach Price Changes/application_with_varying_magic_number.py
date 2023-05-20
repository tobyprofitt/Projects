import math

def calculate_new_price(current_price, last_three_scores, base_magic_number):
    # Divide the current price into fourths. Keep three fourths.
    three_fourths_price = current_price * 3 / 4

    # Take the average of the player's last three scores
    score_average = sum(last_three_scores) / 3

    # Multiply that by the base Magic number
    magic_number_product = score_average * base_magic_number

    # Divide by 4
    magic_number_product /= 4

    # Add that to the three fourths you saved
    new_price = three_fourths_price + magic_number_product

    # Round that to the nearest $100
    new_price = math.floor(new_price / 100) * 100

    # Calculate the change in price
    price_change = new_price - current_price

    # Round the change in price to the nearest $100
    price_change = round(price_change / 100) * 100

    return new_price, price_change

def interpolate_magic_number(round_number):
    magic_number_by_round = {
        0: 5506,
        3: 5150,
        7: 5100,
        10: 5050,
        14: 5000
    }

    # Get rounds less and greater than the input round
    less_than = {k: v for k, v in magic_number_by_round.items() if k <= round_number}
    greater_than = {k: v for k, v in magic_number_by_round.items() if k > round_number}

    if less_than:
        round_less = max(less_than.keys())
    else:
        round_less = min(magic_number_by_round.keys())

    if greater_than:
        round_greater = min(greater_than.keys())
    else:
        round_greater = max(magic_number_by_round.keys())

    magic_number = magic_number_by_round[round_less] + (magic_number_by_round[round_greater] - magic_number_by_round[round_less]) * (round_number - round_less) / (round_greater - round_less)
    return magic_number

def main():
    while True:
        try:
            current_price = float(input("Enter the player's current price: ").strip())
            scores = input("Enter the player's last three scores, separated by commas: ").strip()
            last_three_scores = [float(score) for score in scores.split(',')]
            if len(last_three_scores) != 3:
                raise ValueError("Please provide exactly three scores.")
            
            round_number = int(input("Enter the current round number: ").strip())
            base_magic_number = interpolate_magic_number(round_number)

            new_price, price_change = calculate_new_price(current_price, last_three_scores, base_magic_number)
            print(f"The player's new price is: ${format(new_price, ',')}")
            print(f"The change in price is: ${format(price_change, ',')}")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue


if __name__ == "__main__":
    main()

