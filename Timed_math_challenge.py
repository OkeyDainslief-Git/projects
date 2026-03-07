import random
import time

OPERATOR = ["+", "-", "*",]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("press enter to start!")
print("-----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            print("Correct!")
            break
        else:
            print("Wrong, try again.")
        wrong += 1

end_time = time.time()
elapsed_time = end_time - start_time

print("-----------------------")
print("Nice work! you finished in", elapsed_time, "seconds!" )

