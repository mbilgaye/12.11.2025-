nums = [1, 3, 5]
try:
    nums.get()
except:
    pass
    program_survived = True

# The function average may raise an unhandled exception.
# Change the main function, so that you are protected from unexpected termination.
# If the function has raised an error, print “Error!” to the screen.

def average(numbers):
    return sum(numbers) / len(numbers)

def main():
    try:
        print(average([23, 45, 67, 89, 91, 43, 76]))
        print(average([]))
    except ZeroDivisionError:
        print("Error, You can't divide by zero")

if __name__ == '__main__':
    main()