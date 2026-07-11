print("********** Quiz Game **********")

questions = [
    "What is the Capital of Pakistan? ",
    "What is 10 * 10? ",
    "Sun rises from? ",
    "What is 5 + 5? ",
    "What is 10 / 5? "
]

answers = [
    "islamabad",
    "100",
    "east",
    "10",
    "2"
]

score = 0

for i in range(len(questions)):
    user_answer = input(questions[i])

    if user_answer.lower() == answers[i]:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print("\n========== Result ==========")
print("Your Score:", score, "/", len(questions))