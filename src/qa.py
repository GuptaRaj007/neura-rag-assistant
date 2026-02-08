import subprocess
from retriever import retrieve
from prompts import PROMPT_V3   # use improved prompt

def call_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode("utf-8"),
        capture_output=True
    )
    return result.stdout.decode("utf-8", errors="ignore").strip()


def answer_question(question):
    docs = retrieve(question)
    context = "\n\n".join(docs)

    full_prompt = PROMPT_V3.format(
        context=context,
        question=question
    )

    return call_ollama(full_prompt)


if __name__ == "__main__":
    while True:
        q = input("Ask a policy question: ")
        print("\nAnswer:\n")
        print(answer_question(q))
