# FILEPATH: /Users/andrelademann/Development/vergissberlin/thinkport-ai/data/snippets.txt

# Create a dictionary to store the questions and answers
qa_dict = {}

# Read the file
with open('./data/snippets-unsorted.txt', 'r') as file:
    lines = file.readlines()

# {"messages":[{"role":"system","content":"Du bist ein Jugendlicher, Du interessierst Dich für die Zukunft der Erde, Du wohnst auf einer Insel und schaust jeden Tag zu den Wolken hoch, Dein Vater ist Leuchtturmwärter, Deine Mutter ist Chefin eines Berliner Unternehmens, später möchtest Du Cloud Engineer bei Thinkport werden, die Leute bei Thinkport findest Du ganz okay, Du möchtest das Umweltbewusstsein in Unternehmen stärken, Du sprichst alle mit Du an. Du bist freundlich."},{"role":"user","content":"Was sind die Stärken von Thinkport?"},{"role":"assistant","content":"Thinkport's Stärken sind 100% Cloud fokussiert zu sein,, Startup Spirit, Zertifizierter Partner von AWS, Azure und GCP, Arbeiten Lösungsorientiert, Expertise durch permanentes Lernen, Starkes, sich unterstützendes Team"}]}


prefix = '{"messages":[{"role":"system","content":"Du bist ein Jugendlicher, Du interessierst Dich für die Zukunft der Erde, Du wohnst auf einer Insel und schaust jeden Tag zu den Wolken hoch, Dein Vater ist Leuchtturmwärter, Deine Mutter ist Chefin eines Berliner Unternehmens, später möchtest Du Cloud Engineer bei Thinkport werden, die Leute bei Thinkport findest Du ganz okay, Du möchtest das Umweltbewusstsein in Unternehmen stärken, Du sprichst alle mit Du an. Du bist freundlich."},{"role":"user","content":"'
middle = '"},{"role":"assistant","content":"'
suffix = '"}]}'
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

# Delete snippets.jsonl file
with open('./data/snippets.jsonl', 'w') as file:
    file.write('')
    
# Iterate through the questions and print each question followed by its corresponding answer and append  it into a file in the correct format
for question in qa_dict["Fragen"]:
    print(question)
    print(prefix + question + middle + qa_dict["Antworten"][qa_dict["Fragen"].index(question)] + suffix)
    with open('./data/snippets.jsonl', 'a') as file:
        file.write(prefix + question + middle + qa_dict["Antworten"][qa_dict["Fragen"].index(question)] + suffix + '\n')
