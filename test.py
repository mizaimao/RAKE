#!/usr/bin/env python3
import pandas as pd
import random
import rake

"""
The following codes read in a list of news saved in .txt format, and randomly choose 50 of them, then extract keywords from each of them.

Original text, along with 5 keywords with the highest score, are saved into a csv file.
"""
file_list = []
with open('../data/bbc_list') as file:
    for line in file:
        line = line.rstrip()
        file_list.append(line)

original_text = []
extracted_keywords = []
random.shuffle(file_list)
for txt in file_list[:50]:
    with open(txt) as myfile:
        content = myfile.read().replace('\n', '')
        rake_obj = rake.Rake("SmartStoplist.txt")
        keywords = rake_obj.run(content)

        l = min(len(keywords), 5)
        keywords = keywords[:l]

        original_text.append(content)
        extracted_keywords.append(','.join([str(x) for x in keywords]))

df = pd.DataFrame(data={'original text':original_text,'extracted keywords with top scores':extracted_keywords})
df.to_csv('results.csv', index=False, sep='\t')
