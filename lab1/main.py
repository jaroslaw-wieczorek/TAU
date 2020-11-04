# -*- coding: utf-8 -*-
from googletrans import Translator
import csv
import time

from_language = "PL"
to_language = "EN"

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.pl',
      'translate.google.fr'
    ])


dev0 = {"in": './dev-0/in.tsv', "out": './lab1/dev-0/out.tsv'}
testA = {"in": './test-A/in.tsv', "out": './lab1/test-A/out.tsv'}

with open(testA['in']) as in_file:
    with open(testA['out'], 'w') as out_file:
        writer = csv.writer(out_file)
        for num, row in enumerate(csv.reader(in_file)):
            if row:
                if num % 100 == 0 and num != 0:
                    print('sleep 10s')
                    time.sleep(10)
                    print('start')
                sentence = ''.join(row)
                translation = translator.translate(text=sentence, dest=to_language, source=from_language)
                writer.writerow([translation.text])

