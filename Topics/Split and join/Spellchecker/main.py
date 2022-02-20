dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence = input()
sentence_list = sentence.split()
all_correct = True

for word in sentence_list:
    if word not in dictionary:
        print(word)
        all_correct = False

if all_correct:
    print('OK')
