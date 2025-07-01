import random
from art import logo

def create_deck():
    return [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21 and ((1 in cards) or (11 in cards)):
        return 0

    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1

    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "🙃 It's a draw!"
    elif dealer_score == 0:
        return "😱 You lose, dealer has Blackjack!"
    elif user_score == 0:
        return "🎉 You win with a Blackjack!"
    elif user_score > 21:
        return "💥 You went over. You lose!"
    elif dealer_score > 21:
        return "🔥 Dealer went over. You win!"
    elif user_score > dealer_score:
        return "😎 You win!"
    else:
        return "🤖 Dealer wins."


def play_game():
    print(logo)
    deck = create_deck()
    random.shuffle(deck)

    user_cards = [deal_card(deck), deal_card(deck)]
    dealer_cards = [deal_card(deck), deal_card(deck)]

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"🧍‍♀️ Your cards: {user_cards}, current score: {user_score}")
        print(f"🤖 Dealer's first card: [{dealer_cards[0]}, ?]")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            next_card = input("🃏 Type 'y' to get another card, 'n' to pass: ")
            if next_card == "y":
                user_cards.append(deal_card(deck))
            else:
                is_game_over = True

    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card(deck))

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    print("\n=== 🧾 Final Results ===")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))
    print("========================\n")

play_game()

while input("🃓 Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()