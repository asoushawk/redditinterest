import praw
from praw.models import MoreComments
from collections import Counter

reddit = praw.Reddit(
     client_id="A4pjgLj-HChYmA",
     client_secret="-SPf5aNyRtqnrCDxW9cEHULT9u0",
     user_agent="my user agent")

#1-pega nome de usuários
print("type subreddit")
sub = input()
fhandle = open("authors.txt", "w")
for submission in reddit.subreddit(sub).hot(limit=50):
	print(submission.title)
	for post in submission.comments.list():
		try:
			redditorname = post.author
			print(redditorname.name)
			fhandle.write(redditorname.name)
			fhandle.write(" ")
			print(a)
		except:
		  pass	



#2- remove nome de usuários repetidos:



fhandle = open("authors.txt", "r")
fhandle2 = open("authors1.txt", "w")

def remov_duplicates():
   global s
   st = fhandle.read() 
   st = st.split(" ")
   for i in range(0, len(st)):
      st[i] = "".join(st[i])
      dupli = Counter(st)
      s = " ".join(dupli.keys())
      
     


   
print ("removendo usuários duplicados...")      
remov_duplicates()
fhandle2.write(s)
fhandle2.write(" ")
fhandle.close()
fhandle2.close()
print("done")





#3 - coleta subreddits


fhandle = open("authors1.txt", "r")
f_read = fhandle.read()
stripped = f_read.split(" ")
a = 1
ahandle = open("subreddits1.txt", "w")

c = 0
b = 0



for _ in range(20000):
    a = a + 1
    b = 0
    print(a)
    added_subs = []
    try:
        for comment in reddit.redditor(stripped[a]).comments.new(limit=5):
        
            lastsub = open("lastsub.txt", "r")
            lastsub_r = lastsub.read()
            result = comment.subreddit
            user = comment.author

            result_s = str(result)
            user_s = str(user)

            print("LASTSUBR_R:", lastsub_r)
            print("result_s:", result_s)



            try:
                if lastsub_r != result_s and result_s not in added_subs:
                    added_subs.append(result_s)
                    print("subreddit não repetido")
                    ahandle.write(result_s)
                    ahandle.write(" ")	
                    ahandle.write("\n")
                    print("wrote it")



                else:
                   print("subreddit repetido")	



            except:
                pass


            print("added_subs", added_subs)
            print(user_s)

            lastsub.close()
            lastsub = open("lastsub.txt", "w")
            lastsub.write(result_s)

            print(a, "people")
            

    except Exception as e: print(e)    


#4 - conta ocorrências


fhandle = open("subreddits1.txt", "r")

fhandle_r = fhandle.read()

a = fhandle_r.replace("\n", " ")

b = a.split(" ")

counts = Counter(b)
print(counts)












