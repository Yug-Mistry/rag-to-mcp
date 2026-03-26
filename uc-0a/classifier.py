"""
UC-0A — Complaint Classifier
classifier.py — Starter file

Build this using your AI coding tool:
1. Share agents.md, skills.md, and uc-0a/README.md
2. Ask the AI to implement this file
3. Run: python3 classifier.py --input ../data/city-test-files/test_pune.csv \
                               --output results_pune.csv
"""
import argparse
import csv

def classify_complaint(row: dict) -> dict:
    """
    Classify a single complaint row.
    Returns dict with: complaint_id, category, priority, reason, flag
    """
    raise NotImplementedError("Build this using your AI tool + agents.md")

def batch_classify(input_path: str, output_path: str):
    """Read input CSV, classify each row, write results CSV."""
    raise NotImplementedError("Build this using your AI tool + agents.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UC-0A Complaint Classifier")
    parser.add_argument("--input",  required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    batch_classify(args.input, args.output)
    print(f"Done. Results written to {args.output}")
