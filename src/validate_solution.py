def apply_transition(s, src, tgt):
    return s.replace(src, tgt)

def solve(puzzle):
    s = puzzle["initial_string"]
    for t in puzzle["transitions"]:
        s = apply_transition(s, t["src"], t["tgt"])
    return s == ""

if __name__ == "__main__":
    import json
    puzzles = json.load(open("data/puzzles.json"))

    valid = sum(solve(p) for p in puzzles)
    print(f"Valid puzzles: {valid}/{len(puzzles)}")
