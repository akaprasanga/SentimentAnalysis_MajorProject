import re

# text = "b'RT @: $BTC update \xf0\x80\x94 all hail the queen.  #nodip #BTCUSD #bitcoin #crypto #cryptos #cryptocurrencies #HODL #HODLgang #cryptom\xe2\x80\xa6'"
# m1 = re.sub(r"'","",text)
# m2 = re.findall(r"xf0",text)
# m3 = re.sub('\\xef','',text)
# print(text)
# print(m2)




import csv

csvFile = open('final_BTCTN_2017-7-31_2018_2_28.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)



data_file = csv.reader(open('BTCTN_2017-7-31_2018_2_28.csv', newline=''))
for row in data_file:
    [line] = row
    print(len(line))
    if len(line)>14:
        csvWriter.writerow([line])
    # refine_urls = re.sub(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+','',line)
    # refine_mentions = re.sub(r'@[A-Za-z0-9]+','',refine_urls)
    # refine_mentions = re.sub(r'"','',line)
    # refine_mentions = re.sub(r'@[A-Za-z0-9]+','',refine_urls)
    # m = re.sub(r'(?<=xf0)\w+','', line)
    
    # csvWriter.writerow([refine_mentions])

# refine_urls = """b'RTpjfadosinf  dnskjfnad b' ksdjnfk "b"" @llakf @90jafksn @PJ """

# refine_mentions = re.sub(r'""','',refine_urls)




# print(refine_mentions)


