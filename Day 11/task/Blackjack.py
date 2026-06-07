import random

def deal_card():
    """Return a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10 for J/Q/K, 11 for Ace
    return random.choice(cards)

def calculate_score(cards):
    """Calculate the score of the current hand."""
    # Blackjack check
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Adjust Ace value if needed
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def blackjack():
    print("Welcome to Blackjack!")
    user_cards = []
    computer_cards = []

    # Initial deal
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score == computer_score:
        print("Draw 🙃")
    elif computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
    elif user_score == 0:
        print("Win with a Blackjack 😎")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")

# Run the game
blackjack()
