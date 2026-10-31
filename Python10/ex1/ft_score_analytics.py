import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    i = 1
    total = 0
    scores = []
    while i < len(sys.argv):
        try:
            scores.append(int(sys.argv[i]))
            total += int(sys.argv[i])
        except ValueError:
            ...
        i += 1
    if len(scores) == 0:
        i = 1
        while i < len(sys.argv):
            try:
                int(sys.argv[i])
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
            i += 1
        print("No scores provided. Usage: python3"
              " ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total}")
        print(f"Average score: {total / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {int(max(scores)) - int(min(scores))}")
