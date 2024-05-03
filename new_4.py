import openai

# Set up your OpenAI API key
openai.api_key =


with open("/Users/rishisawhney/PycharmProjects/pythonProject6/test.en", "r", encoding='utf-8') as train_file:
    english_sentences = train_file.readlines()

# Load the Vietnamese translations from a text file
with open("/Users/rishisawhney/PycharmProjects/pythonProject6/test.vi", "r", encoding='utf-8') as test_file:
    vietnamese_translations = test_file.readlines()

# Ensure both files are aligned and have the same number of lines
assert len(english_sentences) == len(vietnamese_translations), "Mismatch in sentence counts!"

# Function to generate few-shot prompt
def generate_few_shot_prompt(pairs, test_sentence):
    prompt = ""
    for eng, viet in pairs:
        prompt += f"English: {eng.strip()}\nVietnamese: {viet.strip()}\n\n"
    prompt += f"English: {test_sentence.strip()}\nVietnamese:"
    return prompt

# Function to perform few-shot translation
def few_shot_translation(num_shots):
    translations = []
    for i, test_sentence in enumerate(english_sentences):
        # Select few-shot examples
        few_shot_examples = list(zip(english_sentences, vietnamese_translations))[:num_shots]  # Use a subset of the paired dataset
        prompt = generate_few_shot_prompt(few_shot_examples, test_sentence)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use a model that supports Vietnamese
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
        with open(f"viet_translations_{num_shots}_shots.txt", "a", encoding='utf-8') as file:
            file.write(f"{translation}\n")

# Perform few-shot translation for different shot numbers
for num_shots in [50]:  # example: using 10 training examples
    few_shot_translation(num_shots)

    # Load the train dataset from a text file
    # with open("test.en", "r", encoding='utf-8') as train_file:
    #     train_dataset = train_file.readlines()
    #
    # # Load the test dataset from a text file
    # with open("test.vi", "r", encoding='utf-8') as test_file:
    #     test_dataset = test_file.readlines()
    #
    # # Function to generate few-shot prompt
    # def generate_few_shot_prompt(train_examples, test_sentence):
    #     prompt = ""
    #     for example in train_examples:
    #         prompt += f"English: {example.strip()}\nVietnamese: <Translate to Vietnamese>\n\n"
    #     prompt += f"English: {test_sentence.strip()}\nVietnamese:"
    #     return prompt
    #
    # # Function to perform few-shot translation
    # def few_shot_translation(num_shots):
    #     translations = []
    #     for test_sentence in test_dataset:
    #         # Select few-shot examples
    #         few_shot_examples = train_dataset[:num_shots]  # Use a subset of the train dataset
    #         prompt = generate_few_shot_prompt(few_shot_examples, test_sentence)
    #
    #         response = openai.ChatCompletion.create(
    #             model="gpt-4",  # Use a model that supports Vietnamese
    #             messages=[
    #                 {"role": "system", "content": prompt},
    #             ],
    #             max_tokens=150,
    #             temperature=0.7,
    #             top_p=1,
    #             n=1,
    #         )
    #         translation = response.choices[0].message["content"].strip()
    #         translations.append(translation)
    #
    #         # Save the translated text to a file
    #         with open(f"eng_viet_translations_{num_shots}_shots.txt", "a", encoding='utf-8') as file:
    #             file.write(f"{translation}\n")
    #
    # # Perform few-shot translation for different shot numbers
    # for num_shots in [10]:
    #     few_shot_translation(num_shots)