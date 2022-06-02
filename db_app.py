import dbcreds
import mariadb

conn = mariadb.connect(
                        user=dbcreds.user,
                        password=dbcreds.password,
                        host=dbcreds.host,
                        port=dbcreds.port,
                        database=dbcreds.database
                        )
cursor = conn.cursor()
supertest = 'super test'
print('db app connected')

def newPost(username):
    print(username)
    cursor.execute('SELECT * FROM blog_post')
    cursor.fetchall()
    id = cursor.rowcount +1    
    content = input('Please enter your post: ')
    cursor.execute("INSERT INTO blog_post(username, content, id) VALUES(?, ?, ?)",[username, content, id])
    
    if(cursor.rowcount == 1):
        conn.commit()
        print("Posted!")
    else: 
        print("Something went wrong")
        
def viewPosts():
    cursor.execute("SELECT * FROM blog_post")
    post_list = cursor.fetchall()
    for post in post_list:
        print(post[0] + ': ' + post[1])
     