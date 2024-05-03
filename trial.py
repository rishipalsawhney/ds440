# from datasets import load_dataset
# dataset = load_dataset("cfilt/iitb-english-hindi")
#
# dataset
#
# source_train_file = open("source_train.txt", "w+", encoding='utf8')
# target_train_file = open("target_train.txt", "w+", encoding='utf8')
# for translation_pair in dataset["train"]["translation"]:
#   source_sentence = translation_pair["en"]
#   target_sentence = translation_pair["hi"]
#   source_train_file.write(source_sentence.strip("\n") + "\n")
#   target_train_file.write(target_sentence.strip("\n") + "\n")
# source_train_file.close()
# target_train_file.close()
#
# source_valid_file = open("source_valid.txt", "w+", encoding='utf8')
# target_valid_file = open("target_valid.txt", "w+", encoding='utf8')
# for translation_pair in dataset["validation"]["translation"]:
#   source_sentence = translation_pair["en"]
#   target_sentence = translation_pair["hi"]
#   source_valid_file.write(source_sentence.strip("\n") + "\n")
#   target_valid_file.write(target_sentence.strip("\n") + "\n")
# source_valid_file.close()
# target_valid_file.close()
#
# source_test_file = open("source_test.txt", "w+", encoding='utf8')
# target_test_file = open("target_test.txt", "w+", encoding='utf8')
# for translation_pair in dataset["test"]["translation"]:
#   source_sentence = translation_pair["en"]
#   target_sentence = translation_pair["hi"]
#   source_test_file.write(source_sentence.strip("\n") + "\n")
#   target_test_file.write(target_sentence.strip("\n") + "\n")
# source_test_file.close()
# target_test_file.close()
import xlsxwriter as xlsxwriter
from sacrebleu.metrics import BLEU
# import sacrebleu
#
# # Load reference translations from the text file
# with open('test.vi', 'r', encoding='utf-8') as ref_file:
#     references = [line.strip() for line in ref_file]
#
# # Load translations from another text file
# with open('eng-viet-50-shot.txt', 'r', encoding='utf-8') as trans_file:
#     translations = [line.strip() for line in trans_file]
#
# # Calculate BLEU score
# bleu = sacrebleu.corpus_bleu(translations, [references])
# print(f"BLEU score: {bleu.score}")
#
# with open("eng-viet-50-shot-bleu-score.txt", "w") as file:
#     file.write(f"BLEU score: {bleu.score}")
import bert_score

# Load reference translations from the text file
with open('test.vi', 'r', encoding='utf-8') as ref_file:
    references = [line.strip() for line in ref_file]

# Load translations from another text file
with open('eng-viet-50-shot.txt', 'r', encoding='utf-8') as trans_file:
    translations = [line.strip() for line in trans_file]

# Calculate BERTScore
P, R, F1 = bert_score.score(translations, references, lang="en")
print(f"BERTScore: {F1.mean()}")

with open("eng-viet-50-shot-bert-score.txt", "w") as file:
    file.write(f"BERTScore: {F1.mean()}")
import bert_score
#
# # Load reference translations from the text file
# with open('test.vi', 'r', encoding='utf-8') as ref_file:
#     references = [line.strip() for line in ref_file]
#
# # Load translations from another text file
# with open('viet_sentences.txt', 'r', encoding='utf-8') as trans_file:
#     translations = [line.strip() for line in trans_file]
#
# # Calculate BERTScore
# P, R, F1 = bert_score.score(translations, references, lang="en")
# print(f"BERTScore: {F1.mean()}")
#
# with open("bert_eng_viet_score.txt", "w") as file:
#     file.write(f"BERTScore: {F1.mean()}")

