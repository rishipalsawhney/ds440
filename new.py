import openai

# Set up your OpenAI API key
openai.api_key =

# Load the English sentences from the source file
with open("/Users/rishisawhney/PycharmProjects/pythonProject6/viet_sentences.txt", "r", encoding='utf8') as source_file:
    source_sentences = source_file.readlines()
#Initialize an empty list to store translated sentences
translations = []
for sentence in source_sentences :
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Translate the following text from Vietnamese to English:"},
            {"role": "user", "content": sentence},
        ],
        max_tokens=100,
        temperature=0.2,
        top_p=1,
        n=1,
        stop=None,
    )
    translation = response.choices[0].message["content"].strip()
    translations.append(translation)
    # Save the translated text to a file
    with open("viet-eng-no-shot.txt", "a") as file:
        # file.write(f"Original English: {sentence.strip()}\n")
        file.write(f"{translation}\n")




        # Iterate over each English sentence and translate it to Hindi using OpenAI API
# for sentence in source_sentences:
#     translation = openai.Completion.create(
#         engine="davinci-002",  # You can choose another engine if desired
#         prompt="Translate the following text from English to Hindi:\nEnglish: " + sentence.strip(),
#         max_tokens=60,  # Adjust as needed
#         temperature=0.7,  # Adjust as needed
#         top_p=1,
#         n=1,
#         stop=None
#     )
#
#
#     # Extract and append the translated sentence
#     translated_sentence = translation.choices[0].text.strip()
#     translated_sentences.append(translated_sentence)
#
#
# # Write the translated sentences to a separate file
# # with open("translated_hindi.txt", "w", encoding='utf8') as target_file:
# #     for sentence in translated_sentences:
# #         target_file.write(sentence + "\n")
# with open("translations.txt", "a") as file:
#     file.write(f"Original English: {sentence['translation']['en']}\n")
#     file.write(f"Translated Hindi: {translation}\n\n")


# for sentence in source_sentences:
#     translation = openai.Completion.create(
#         engine="davinci-002",  # You can choose another engine if desired
#         prompt="Translate the following text from English to Hindi:\nEnglish: " + sentence.strip(),
#         max_tokens=60,  # Adjust as needed
#         temperature=0.7,  # Adjust as needed
#         top_p=1,
#         n=1,
#         source_language="en",
#         target_language="hi"  # Set the target language to Hindi
#     )
#
#     # Extract and append the translated sentence
#     translated_sentence = translation.choices[0].text.strip()
#     translated_sentences.append(translated_sentence)



        # Extract and append the translated sentence
#         translated_sentence = translation.choices[0].text.strip()
#         translated_sentences.append(translated_sentence)
# # Write the original English sentences and their translations to a separate file
#
#
# with open("viettranslations.txt", "a", encoding='utf8') as file:
#     for original, translated in zip(source_sentences, translated_sentences):
#         file.write(f"Original English: {original.strip()}\n")
#         file.write(f"Translated Hindi: {translated}\n\n")
# print("Translation completed and saved to hinditranslations.txt")

# import openai
# # Set up your OpenAI API key
# openai.api_key =
# # Load the English sentences from the source file
# with open("test.en", "r", encoding='utf8') as source_file:
#     source_sentences = source_file.readlines()
# #Initialize an empty list to store translated sentences
# translations = []
# for sentence in source_sentences :
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "Translate the following text from English to Vietnamese:"},
#             {"role": "user", "content": sentence},
#         ],
#         max_tokens=100,
#         temperature=0.7,
#         top_p=1,
#         n=1,
#         stop=None,
#     )
#     translation = response.choices[0].message["content"].strip()
#     translations.append(translation)
#  # Save the translated text to a file
#     with open("translationtovietnamese2.txt", "a") as file:
#         file.write(f"Original English: {sentence.strip()}\n")
#         file.write(f"Translated Vietnamese: {translation}\n\n")
#
# bleu = BLEU()
# references = [example["translation"]["en"] for example in dataset]
# score = bleu.corpus_score(translations, [references])
# print(f"BLEU score: {score.score}")
#
# # Writing BLEU score to a file
# with open("bleu_scoreDE.txt", "w") as file:
#     file.write(f"BLEU score: {score.score}")