import re
my_string=(input("Enter the desired sentence(sentence should endings with (.?!) ):"))
sentence_endings = r"[,-.?!]"
print(re.split(sentence_endings, my_string))