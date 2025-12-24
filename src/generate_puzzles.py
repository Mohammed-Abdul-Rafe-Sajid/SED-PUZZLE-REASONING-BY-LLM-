import random
import json
import string

def random_token(min_len=2, max_len=4):
    length = random.randint(min_len, max_len)
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def generate_puzzle(problem_id, difficulty="easy"):
    transitions = []
    current_string = ""

    if difficulty == "easy":
        steps = random.randint(2, 3)
    elif difficulty == "medium":
        steps = random.randint(4, 6)
    else:  # hard
        steps = random.randint(6, 8)

    inserted_tokens = []

    for _ in range(steps):
        token = random_token()
        inserted_tokens.append(token)
        current_string += token
        transitions.append({
            "src": token,
            "tgt": ""
        })

    # ADD DISTRACTORS HERE
    transitions = add_distractors(transitions, inserted_tokens)

    # Shuffle transitions to make reasoning non-trivial
    random.shuffle(transitions)

    return {
        "problem_id": f"{problem_id:03d}",
        "initial_string": current_string,
        "transitions": transitions,
        "difficulty": difficulty
    }

def add_distractors(transitions, tokens):
    distractors = []
    for t in tokens:
        if len(t) > 2:
            distractors.append({
                "src": t[:2],
                "tgt": t[1:]
            })
    return transitions + distractors

def generate_dataset(n=100):
    dataset = []
    difficulties = ["easy", "medium", "hard"]

    for i in range(n):
        difficulty = random.choice(difficulties)
        puzzle = generate_puzzle(i, difficulty)
        dataset.append(puzzle)

    return dataset

if __name__ == "__main__":
    random.seed(42)

    puzzles = generate_dataset(100)

    with open("data/puzzles.json", "w") as f:
        json.dump(puzzles, f, indent=2)

    print("Generated 100 puzzles")
