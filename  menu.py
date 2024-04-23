from datetime import datetime

class Content:
    def __init__(self):
        self.author = input("Enter nickname: ")  
        self.text = input("Write your post: ")   
        self.created_at = datetime.now()         

    
    def __str__(self):
        return f"{self.author} said at {self.created_at}: {self.text}"


class Post(Content):
    def __init__(self):
        super().__init__()                   
        self.id = None
        self.likes = 0
        self.dislikes = 0

    def add_like(self):
        self.likes += 1

    def add_dislike(self):
        self.dislikes += 1

    def get_rating(self):
        return self.likes - self.dislikes

    def __str__(self):
        return f"{self.author} said: {self.text}\nLikes: {self.likes} Dislikes: {self.dislikes}\nRating: {self.get_rating()}"

class Comment(Content):
    def __init__(self, post_id):
        super().__init__()         
        self.post_id = post_id  
        self.note = None

    def __str__(self):
        return f"{self.author} commented on post #{self.post_id}: {self.text} Note: {self.note}" 

if __name__ == "__main__":
    post = Post()
    comment1 = Comment(1)
    comment2 = Comment(1)
    comment2.note = "some note"
    print(comment2)
    print(comment1)
