# The task: a public URL contains a large web-server log file made up of URLs. Write Python code that takes the public
# URL as input, fetches the data, processes it, counts URL occurrences, and returns the top N most popular URLs. For
# example, N=5 means the top five URLs; N=100 means the top 100.
# Original problem statement (condensed from interviewer explanation)
# “Write Python code that takes this public URL as the input, fetch the data from this URL, process the data inside it,
# and tell us what are the top and most popular URLs.”

from urllib.request import urlopen
import csv
from collections import defaultdict
count=defaultdict(int)
url="https://public.karat.io/content/urls2.txt"
with urlopen(url) as response:
    lines = (line.decode("utf-8") for line in response)
    data=csv.reader(lines)
    for line in data:
        url=line[0]
        count[url]+=1

print(sorted(count.items(),
        key=lambda x: x[1],
        reverse=True)[:5])
