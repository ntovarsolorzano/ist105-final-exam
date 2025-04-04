#!/usr/bin/env python3

import cgi
import html

# Party items and their corresponding values
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

    form = cgi.FieldStorage()
    indices = form.getfirst("items", "")

    html_output = "<html><head><title>Party Planner Result</title></head><body>"
    html_output += "<h1>Party Planner Result</h1>"

    if not indices:
        html_output += "<p style='color:red;'>No items selected.</p></body></html>"
        print(html_output)
        return

    try:
        selected_indices = [int(i.strip()) for i in indices.split(",") if i.strip().isdigit()]
    except ValueError:
        html_output += "<p style='color:red;'>Invalid input. Please enter comma-separated indices.</p></body></html>"
        print(html_output)
        return

    selected_items = []
    values = []

    for idx in selected_indices:
        if 0 <= idx < len(party_items):
            item, value = party_items[idx]
            selected_items.append(item)
            values.append(value)

    if not values:
        html_output += "<p style='color:red;'>No valid items selected.</p></body></html>"
        print(html_output)
        return

    base_code = values[0]
    for val in values[1:]:
        base_code &= val

    # Store original base_code for display
    original_base_code = base_code

    # Apply modification rules
    if base_code == 0:
        base_code += 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        base_code -= 2
        message = "Let's keep it classy!"
    else:
        message = "Chill vibes only!"

    html_output += f"<p><strong>Selected Items:</strong> {', '.join(selected_items)}</p>"
    html_output += f"<p><strong>Base Party Code:</strong> {' & '.join(str(v) for v in values)} = {original_base_code}</p>"
    html_output += f"<p><strong>Adjusted Party Code:</strong> {base_code}</p>"
    html_output += f"<p><strong>Message:</strong> {html.escape(message)}</p>"
    html_output += "</body></html>"

    print(html_output)

if __name__ == "__main__":
    main()
