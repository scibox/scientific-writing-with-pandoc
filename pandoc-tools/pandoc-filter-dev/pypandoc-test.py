import pypandoc
import os

#read the intermediate json file -- generated by running pandoc with: -t json
file = open('test_out.json')
json_dat = file.read()

pypandoc.convert_text(json_dat,'rst',format='json',filters=[os.path.join('pandoc-tools','bib-filter.py')])

