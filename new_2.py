import openai

# Set up your OpenAI API key
openai.api_key =

# Load the train dataset from a text file
with open("/Users/rishisawhney/PycharmProjects/pythonProject6/target_test.txt", "r", encoding='utf-8') as train_file:
    train_dataset = train_file.readlines()

# Load the test dataset from a text file
with open("/Users/rishisawhney/PycharmProjects/pythonProject6/source_test.txt", "r", encoding='utf-8') as test_file:
    test_dataset = test_file.readlines()

# Function to generate few-shot prompt
def generate_few_shot_prompt(train_examples, test_sentence):
    prompt = ""
    for example in train_examples:
        prompt += f"English: {example.strip()}\nHindi: <Translate to Hindi>\n\n"
    prompt += f"English: {test_sentence.strip()}\nHindi:"
    return prompt

# Function to perform few-shot translation
def few_shot_translation(num_shots):
    translations = []
    for test_sentence in test_dataset:
        # Select few-shot examples
        few_shot_examples = train_dataset[:num_shots]  # Use a subset of the train dataset
        prompt = generate_few_shot_prompt(few_shot_examples, test_sentence)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7,
            top_p=1,
            n=1,
        )
        translation = response.choices[0].message["content"].strip()
        translations.append(translation)

        # Save the translated text to a file
        with open(f"translations_{num_shots}_shots.txt", "a", encoding='utf-8') as file:
            file.write(f"Original English: {test_sentence.strip()}\n")
            file.write(f"Translated Hindi: {translation}\n\n")

# Perform few-shot translation for different shot numbers
for num_shots in [10, 50, 100]:
    few_shot_translation(num_shots)
