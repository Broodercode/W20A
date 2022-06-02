import db_app
db_app

cursor = db_app.cursor

username = input("Please type your name: ")

print('Hello ' + username)

def userChoice():
    
    choice = input('Please press 1 for new post, 2 to view all posts, or 3 to exit: ')

    if(choice == '1'):
        db_app.newPost(username)
    elif(choice == '2'):
        db_app.viewPosts()
    elif(choice == '3'):
        return
    else:
       print("invalid selection")
       userChoice()
        
userChoice()