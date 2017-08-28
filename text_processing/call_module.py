import sys
sys.path.insert(0,"/home/cians/text_processing/modules")

import diction_extractor as de

caller=de.Give_txt_file_get_list()

print(caller.extract("a_300.txt"))
