import re

scanner=re.Scanner([
    (r"[\d]+(\w\w)?",     lambda scanner,token:(token)),
    (r"[A-Za-z]+",     lambda scanner,token:(token)),
    (r"[,.]+",     None),
    (r"\s+", None),
])

text="""also, we just checked in today. 
he took attendence and then chatted with us.
Our next presentation is the following Friday, the 27th of October."""

results, remainder=scanner.scan(text)
#print(results)

#basic word remover
rem_text = ["is", "an", "in", "and", "then", "the", "with", "just", "of",]

pattern = re.compile(r'\b{}\b'.format('|'.join(rem_text)))

filtered_token = [word for word in results if not pattern.search(word)]
print(filtered_token)