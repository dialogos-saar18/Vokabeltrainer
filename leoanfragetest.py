url = "https://dict.leo.org/englisch-deutsch/dog"
import urllib.request
with urllib.request.urlopen(url) as response:
   html = response.read()
with open("leoausgabe.txt","w") as f:
    f.write(str(html))






    
