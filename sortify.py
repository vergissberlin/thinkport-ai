# FILEPATH: /Users/andrelademann/Development/vergissberlin/thinkport-ai/data/snippets.txt

# Create a dictionary to store the questions and answers
qa_dict = {}

# Read the file
with open('./data/snippets.txt', 'r') as file:
    lines = file.readlines()

# Iterate through the lines and store questions and answers in the dictionary
for i, line in enumerate(lines):
    if line.startswith("Fragen:"):
        questions = []
        for j in range(i+1, len(lines)):
            if lines[j].startswith("Antworten:"):
                break
            questions.append(lines[j].strip())
        qa_dict["Fragen"] = questions
    elif line.startswith("Antworten:"):
        answers = []
        for j in range(i+1, len(lines)):
            answers.append(lines[j].strip())
        qa_dict["Antworten"] = answers

# Iterate through the questions and print each question followed by its corresponding answer
for i, question in enumerate(qa_dict["Fragen"]):
    print(f"Frage {i+1}: {question}")
    print(f"Antwort: {qa_dict['Antworten'][i]}")
    print()
