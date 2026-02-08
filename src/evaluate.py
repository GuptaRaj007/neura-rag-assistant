from qa import answer_question

EVAL_SET = [
    ("Can I get a refund after 10 days?", "Not allowed, only within 7 days"),
    ("Can I cancel after shipping?", "Not allowed once shipped"),
    ("How long does international shipping take?", "10–15 business days"),
    ("Do you offer free express delivery?", "Not mentioned"),
    ("Can I cancel my subscription mid-cycle?", "No refund for partial period"),
    ("What is your office address?", "Not mentioned"),
]

def evaluate():
    print("\nEvaluation Results:\n")
    for q, expected in EVAL_SET:
        ans = answer_question(q)
        print(f"Q: {q}")
        print(f"Expected: {expected}")
        print(f"Model Answer:\n{ans}\n")
        print("-" * 50)

if __name__ == "__main__":
    evaluate()
