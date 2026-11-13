# Copyright © 2026 Christopher Snow
# Four invented events, not random draws. No real-world outcomes were measured.
events = [
    [1, 1, 0],
    [1, 0, 0],
    [1, 1, 1],
    [0, 1, 1],
]
seats = 2
overflow_count = 0

print("INVENTED examples: 1 attends, 0 is absent.")
for guests in events:
    attendance = sum(guests)
    print("Guests:", guests, "Attendees:", attendance,
          "Overflows:", attendance > seats)
    if attendance > seats:
        overflow_count += 1

fraction = overflow_count / len(events)
print("Overflow examples:", overflow_count, "of", len(events))
print("Illustrative fraction:", fraction, "=", 100 * fraction, "%")
print("This is a counting demonstration, not an estimated model probability.")
