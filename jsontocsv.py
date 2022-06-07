import json
import csv

result=''

with open('D:/GT-VIRT-DATA-PT-03-2022-U-LOL/Project-2/Resources/result.json','r') as f:
        for line in f.read():
            result+=line

result=json.loads(result)

print(type(resuly[0]))




