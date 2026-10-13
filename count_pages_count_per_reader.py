from collections import defaultdict
import csv
#lines=[]
reader_points=defaultdict(int)
with open("/Users/hgunupur/Downloads/test_file.txt", "r",newline="",encoding="utf-8") as fr:
    # data=fr.read()
    # for line in data.split("\n"):
    #   word=[]
    #   for words in line.split(","):
    #     word.append(words)
    #   lines.append(word)
      lines=csv.reader(fr)
      for line in lines:
          reader_id=int(line[0])
          pages=int(line[3])
          reader_points[reader_id]+=50+pages

print(sorted(reader_points.items(),
        key=lambda x: x[1], reverse=True)[:5])
