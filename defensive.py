#!/usr/bin/env python3
"""
Lab: Defensive debugging and validation.

Goal: compute average score from user-provided text.
Starter assumes ideal input and fails with non-numeric tokens.
"""


def parse_scores_csv(scores_text):
    """Parse comma-separated scores into a list of ints."""
    parts = scores_text.split(",")
    scores = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        try:
            scores.append(int(part))
        except ValueError:
            raise ValueError(f"Invalid input: '{part}' is not a valid integer.")
    return scores


def average_score(scores):
    """Return arithmetic mean of a non-empty score list."""
    if not scores:
        raise ValueError("Cannot compute average: scores list is empty.")
    return sum(scores) / len(scores)


def score_band(avg):
    """Classify average score into a textual band."""
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


def evaluate_scores(scores_text):
    """Return (average, band) from comma-separated score text."""
    scores = parse_scores_csv(scores_text)
    avg = round(average_score(scores), 2)
    return avg, score_band(avg)


def main():
    test_cases = [
        "90,85,95,100",        # Valid
        "90,85,invalid,100",   # Invalid integer
        ""                     # Empty input
    ]
    
    for case in test_cases:
        print(f"\\nEvaluating scores: '{case}'")
        try:
            avg, band = evaluate_scores(case)
            print("Average:", avg)
            print("Band:", band)
        except Exception as e:
            print(f"Error handling scores: {e}")


if __name__ == "__main__":
    main()
