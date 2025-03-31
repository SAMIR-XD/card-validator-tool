import re

def luhn_check(card_number):
    """Luhn Algorithm ব্যবহার করে কার্ড নম্বর চেক করা"""
    card_number = card_number[::-1]
    total = 0
    for i, digit in enumerate(card_number):
        num = int(digit)
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
        total += num
    return total % 10 == 0

def check_cards(file_name):
    """কার্ড ফাইল থেকে পড়ে লাইভ এবং ডেড কার্ড আলাদা করা"""
    with open(file_name, 'r') as f:
        cards = f.readlines()

    live_cards = []
    dead_cards = []

    for line in cards:
        match = re.match(r"(\d{16})\|\d{2}\|\d{4}\|\d{3}", line.strip())
        if match:
            card_number = match.group(1)
            if luhn_check(card_number):
                live_cards.append(line.strip())
            else:
                dead_cards.append(line.strip())

    # ফলাফল সংরক্ষণ
    with open("live_cards.txt", "w") as f:
        f.write("\n".join(live_cards))

    with open("dead_cards.txt", "w") as f:
        f.write("\n".join(dead_cards))

    print(f"Total Checked: {len(cards)}")
    print(f"Live Cards: {len(live_cards)}")
    print(f"Dead Cards: {len(dead_cards)}")
    print("Results saved in live_cards.txt & dead_cards.txt")

# ইউজার ইনপুট নিয়ে রান করানো
file_name = input("Enter the file name containing card details: ")
check_cards(file_name)