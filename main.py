# from datasets import load_dataset
#
# dataset = load_dataset("cfilt/iitb-english-hindi")
# dataset = dataset["test"]  # Assuming you want to use the training set
#
# import openai
#
# openai.api_key =
# translations = []
# for example in dataset:
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=example["translation"]["en"],
#         max_tokens=60,
#         temperature=0.7,
#         top_p=1,
#         n=1,
#         stop=None,
#     )
#     translation = response.choices[0].text.strip()
#     translations.append(translation)
#
# # Printing translations
# for original_en, translation_hi in zip(dataset["translation"]["en"], translations):
#     print(f"English: {original_en}")
#     print(f"Hindi Translation: {translation_hi}")

