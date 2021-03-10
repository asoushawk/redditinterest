
import praw
import random
from praw.models import MoreComments
from collections import Counter


reddit = praw.Reddit(
     client_id="A4pjgLj-HChYmA",
     client_secret="-SPf5aNyRtqnrCDxW9cEHULT9u0",
     user_agent="my user agent", check_for_async=False)

#limpador do console
def clear(): 
  
    import os
    os.system('cls' if os.name == 'nt' else 'clear')



#1-pega nome de usuários
print("type subreddit")
sub = input()
authors = list()

    


def getauthors():
  for submission in reddit.subreddit(sub).hot(limit=5):
    #print(submission.title)
    for post in submission.comments.list():
      try:
        redditorname = post.author
        #print(redditorname.name)
        yield str(redditorname)
      
      except:
        pass  

for author in getauthors():
  authors.append(author)


#2- remove nome de usuários repetidos:
fhandle2 = open("authors1.txt", "w")
def remov_duplicates():
   fhandle2 = open("authors1.txt", "w")
   st = authors
   for i in range(0, len(st)):
      st[i] = "".join(st[i])
      dupli = Counter(st)
      s = " ".join(dupli.keys())
      fhandle2.write(s)
      fhandle2.write(" ")
     
clear()
print ("removendo usuários duplicados...")      
remov_duplicates()
fhandle2.close()
print("done")



#3 - nomesdeusuario e os coloca em uma lista
lastsub = ['a']
fhandle = open("authors1.txt", "r")
f_read = fhandle.read()
stripped = f_read.split(" ")
items = list()


#função que retorna os autores
def getitem(stripped):
  for item in stripped:
    if item != "":  
      yield item


for itemm in getitem(stripped):
  items.append(itemm)

getitem(stripped)
random.shuffle(items)
ahandle = []

def work():
  a = -1 #index
  lastsub = ['a'] #ultimosub
  z = 500 #numero de usuarios a serem analisados
  for _ in range(z):
    a += 1 #incremento do loop
    added_subs = []
    try:
      for comment in reddit.redditor(items[a]).comments.new(limit=2):            
        result = comment.subreddit
        user = comment.author
        result_s = str(result)
        if result_s != sub:
          user_s = str(user)
          #print("LASTSUBR_R:", lastsub)
          #print("result_s:", result_s)
          try:
            if lastsub != result_s and result_s not in added_subs:
              added_subs.append(result_s)
              ahandle.append(result_s)
              yield result_s
            
              



          except:
            pass


          #print("added_subs", added_subs)
          #print(user_s)
          lastsub = []
          lastsub.append(result_s)

          
                          
          clear()
          #printa porcentagem do progresso
          print(int((a/z ) * 100), "%")
          
            
            
        
    except Exception as e: print(e)    

uf = 0
final = list()
for i in work():
  #print(final)
  if i not in final:
    uf = uf + 1
    #print(uf)
  final.append(i)
 
  
counts = Counter(final) #função count do python que conta a repetição de valores em uma lista


mostcommon = [mc for mc,cnt in counts.most_common(15)]
r = 1
clear()
for i in mostcommon:
  print(r, "-", i)
  r = r + 1

print("UF ", uf) #fator diversidade: número de subreddits únicos

