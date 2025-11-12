# Write a function, until_stop, that gets a list of strings as the parameter.
# In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original list until it reaches the string “STOP”.
# The new list should not contain the string “STOP”.
# Note: the word STOP doesn’t have to appear in the list.
# If the word “STOP” did not appear in the list, the returned list should be a copy of the original one.
# For example, running until_stop(["hey", "joe", "meow", "STOP", "Hello"]) should return the list ["hey", "joe", "meow"].

def until_stop(words):
    result = []
    index = 0

    while index < len(words):
        if words[index] == "STOP":
            break
        result.append(words[index])
        index += 1
    return result

print(until_stop(["joe", "sam", "hari", "manu", "STOP", "leena"]))
print(until_stop(["STOP", "sam", "bob", "dick", "sara", "doris", "rainer"]))