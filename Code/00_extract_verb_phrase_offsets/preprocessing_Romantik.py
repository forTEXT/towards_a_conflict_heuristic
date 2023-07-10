import glob
import os
import re

# get paths list and novel titles

path_data = r"C:\Users\Julian\HESSENBOX-DA\Projekte\Konflikte_Preprocessing\Korpora\Romantik"

paths_list = glob.glob(os.path.join(os.getcwd(), path_data, "*.txt"))

novels_titles = []

for entry in paths_list:
    novels_titles.append(re.search(r"(?<=Romantik\\)(.*)(?=.txt)",entry).group(1))

# call preprocessing script for each novel in corpus

for i in range(0,len(paths_list)):
    title = novels_titles[i]
    os.system("preprocess.py preprocess --parser=spacy " + title + ".txt " + title + ".json")
