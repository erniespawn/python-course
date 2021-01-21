import requests

response = requests.get('https://www.mit.edu/~ecprice/wordlist.10000')
word_dict ={}
res = response.content.decode('utf-8')
for i in res.split('\n'):
    # print (i)
    if i:
        count = word_dict.get(i[0], 0)
        word_dict[i[0]] = count + 1
for alphabet, count in word_dict.items():
    print(f"Alphabet {alphabet} has count of {count}")
