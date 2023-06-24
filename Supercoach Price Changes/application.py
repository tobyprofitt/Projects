

# Author: Toby Profitt 20/05/2023
# With help from Father Dougal
# https://supercoachtalk.com/how-supercoach-pricing-works-2020/


def calculate_new_price(current_price, last_three_scores, base_magic_number, deflation_factor, should_round=True):
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

    # Apply the deflation factor
    new_price *= deflation_factor

    # Round that to the nearest $100 if should_round is True
    if should_round:
        new_price = round(new_price / 100) * 100

    # Calculate the change in price
    price_change = new_price - current_price

    # Round the change in price to the nearest $100
    price_change = round(price_change / 100) * 100

    return new_price, price_change



def calculate_deflation_factor(starting_price, past_3_scores, actual_new_price, base_magic_number):
    estimated_new_price, _ = calculate_new_price(starting_price, past_3_scores, base_magic_number, deflation_factor=1, should_round=False)
    deflation_factor = actual_new_price / estimated_new_price
    return deflation_factor



def main():
    DEFAULT_MAGIC_NUMBER = 5505.74
    DEFAULT_DEFLATION_FACTOR = 0.9859509020999704

    while True:
        try:
            calculate_deflation = input("Do you need to calculate the deflation factor? (yes/no): ").strip().lower()
            if calculate_deflation == "yes":
                starting_price = float(input("Enter the sample player's starting price: ").strip())
                scores = input("Enter the sample player's past three scores, separated by commas: ").strip()
                past_3_scores = [float(score) for score in scores.split(',')]
                if len(past_3_scores) != 3:
                    raise ValueError("Please provide exactly three scores.")
                actual_new_price = float(input("Enter the sample player's actual new price: ").strip())
                base_magic_number_input = input(f"Enter the base magic number (leave empty for default {DEFAULT_MAGIC_NUMBER}): ").strip()
                base_magic_number = DEFAULT_MAGIC_NUMBER if base_magic_number_input == "" else float(base_magic_number_input)
                deflation_factor = calculate_deflation_factor(starting_price, past_3_scores, actual_new_price, base_magic_number)
                print(f"The estimated deflation factor is: {deflation_factor}")
            elif calculate_deflation == "no":
                deflation_factor = DEFAULT_DEFLATION_FACTOR
                base_magic_number = DEFAULT_MAGIC_NUMBER
            else:
                raise ValueError("Please enter either 'yes' or 'no'.")

            current_price = float(input("Enter the player's current price: ").strip())
            scores = input("Enter the player's last three scores, separated by commas: ").strip()
            last_3_scores = [float(score) for score in scores.split(',')]
            if len(last_3_scores) != 3:
                raise ValueError("Please provide exactly three scores.")

            new_price, price_change = calculate_new_price(current_price, last_3_scores, base_magic_number, deflation_factor)
            print(f"The player's new price is: ${new_price:,d}")
            print(f"The change in price is: ${price_change:,d}")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue

if __name__ == "__main__":
    main()
