import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']
play_again = 'Y'

while play_again.upper() == 'Y':
    results = random.choices(symbols, k=3)
    print(" | ".join(results))

    if results == ['7️⃣', '7️⃣', '7️⃣']:
        print("Jackpot! 💰")

    play_again = input("Do you want to keep playing? (Y/N): ")

print("Thanks for playing!")
