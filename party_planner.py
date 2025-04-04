#!/usr/bin/env python3

import sys
import html

party_items = [
    ("Cake", 20),
    ("Balloons", 21),
    ("Music System", 10),
    ("Lights", 5),
    ("Catering Service", 8),
    ("DJ", 3),
    ("Photo Booth", 15),
    ("Tables", 7),
    ("Chairs", 12),
    ("Drinks", 6),
    ("Party Hats", 9),
    ("Streamers", 18),
    ("Invitation Cards", 4),
    ("Party Games", 2),
    ("Cleaning Service", 11),
]

def main():
    print("Content-Type: text/html\n")

    if len(sys.argv) < 2:
        print("<p style='color:red;'>No input provided.</p>")
        return

    indices_str = sys.argv[1]
    try:
        selected_indices = [int(i) for i in indices_str.split(",") if i.strip().isdigit()]
    except ValueError:
        print("<p style='color:red;'>Invalid input format.</p>")
        return

    selected_items = []
    values = []

    for idx in selected_indices:
        if 0 <= idx < len(party_items):
            item, value = party_items[idx]
            selected_items.append(item)
            values.append(value)

    if not values:
        print("<p style='color:red;'>No valid items selected.</p>")
        return

    base_code = values[0]
    for val in values[1:]:
        base_code &= val

    original_base_code = base_code

    if base_code == 0:
        base_code += 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        base_code -= 2
        message = "Let's keep it classy!"
    else:
        message = "Chill vibes only!"

    print("<html><head><title>Party Code</title></head><body>")
    print(f"<h1>Selected Items:</h1><p>{', '.join(selected_items)}</p>")
    print(f"<p><strong>Base Party Code:</strong> {' & '.join(map(str, values))} = {original_base_code}</p>")
    print(f"<p><strong>Adjusted Party Code:</strong> {base_code}</p>")
    print(f"<p><strong>Message:</strong> {html.escape(message)}</p>")
    print("</body></html>")

if __name__ == "__main__":
    main()

# Python code