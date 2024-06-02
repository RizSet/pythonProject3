import codecs
import json
import os

json_path = os.path.dirname(os.path.realpath(__file__)) + "\\"
json_file = "24tvarticles.json"
json_data = []
if not os.path.exists(json_path + "sas_ready_txt"):
    os.makedirs(json_path + "sas_ready_txt")
with open(json_path +  "\\..\\" + json_file , 'r', encoding='utf-8') as json_fileopen:
    json_data = json.load(json_fileopen)
for article in json_data:
    article_text = article['article_title'][0] + "\n\n"

    for article_text_str in article['article_text']:
        article_text = article_text + " " + article_text_str.replace(" ", " ")

    article_uuid = article['article_uuid']

    with codecs.open(json_path + "sas_ready_txt/" + article_uuid + ".txt", "w", "utf-8-sig") as temp:
        temp.write(article_text)