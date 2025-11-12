# Create a while loop that has a counter from 1 to 20 (inclusive).
# If the value of the counter is divisible by 5, just skip it using continue.
# For the rest of the numbers, print the number.
# Each number should appear in a new line.

counter = 1
while counter <= 20:
    if counter % 5 == 0:
        counter += 1
        continue
    print(counter)
    counter += 1