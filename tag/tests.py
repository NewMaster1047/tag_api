from django.test import TestCase
import re


def tag_creater(description):
    data = re.findall(r"#.[^#|\s+]*", description)
    serialized_d = []
    for i in data:
        if '#' in i:
            serialized_d.append(i)

    print(serialized_d)


tag_creater("adfads#asdfaf#123 #1313 #fdasfasf fasfsadffasf sadfa#dsfsdf")