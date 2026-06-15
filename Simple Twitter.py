users = {}
posts = []
post_id = 1


def create_user():
    username = input("Enter a username: ")
    bio = input("Enter a bio: ")

    users[username] = {
        "bio": bio,
    }

    print("User created!")


def write_post():
    global post_id

    username = input("Who is posting? ")

    if username not in users:
        print("That user does not exist.")
        return

    text = input("What do you want to say? ")

    post = {
        "id": post_id,
        "user": username,
        "text": text,
        "likes": 0
    }

    posts.append(post)
    post_id += 1

    print("Post created!")


def view_feed():
    if len(posts) == 0:
        print("No posts yet.")
        return
        
    print("----- FEED -----")
    for post in posts:
        print("ID: " + str(post['id']))
        print("User: " + str(post['user']))
        print("Post: " + str(post['text']))
        print("Likes: " + str(post['likes']))
        print("----------------")
    print()


def like_post():
    try:
        wanted_id = int(input("Enter post ID to like: "))
    except ValueError:
        print("Please enter a number.")
        return

    for post in posts:
        if post["id"] == wanted_id:
            post["likes"] += 1
            print("Post liked!")
            return

    print("Post not found.")


# Extension: Show most liked post
def most_liked_post():
    if len(posts) == 0:
        print("No posts available.")
        return

    best_post = posts[0]

    for post in posts:
        if post["likes"] > best_post["likes"]:
            best_post = post

    print("Most Liked Post")
    print("ID: " + str(best_post['id']))
    print("User: " + str(best_post['user']))
    print("Post: " + str(best_post['text']))
    print("Likes: " + str(best_post['likes']))


while True:
    print("1. Create a user")
    print("2. Write a post")
    print("3. View the feed")
    print("4. Like a post")
    print("5. Show most liked post")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_user()

    elif choice == "2":
        write_post()

    elif choice == "3":
        view_feed()

    elif choice == "4":
        like_post()

    elif choice == "5":
        most_liked_post()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
