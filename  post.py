from datetime import datetime

class Content:
    def __init__(self):
        self.author = input("Enter nickname: ")  
        self.text = input("Write your post: ")   
        self.created_at = datetime.now()         

    
    def __str__(self):
        return f"{self.author} said at {self.created_at}: {self.text}"


class Post(Content):
    entries = []

    def __init__(self):
        super().__init__()                   
        self.id = len(Post.entries) + 1
        self.likes = 0                       
        self.dislikes = 0
        Post.entries.append(self)           

    def add_like(self):
        self.likes += 1

    def add_dislike(self):
        self.dislikes += 1

    def get_rating(self):
        return self.likes - self.dislikes

    @classmethod
    def sort_by_rating(cls):
        return sorted(cls.entries, key=lambda post: post.get_rating(), reverse=True)

    def __str__(self):
        return f"#{self.id} {self.author} said: {self.text}\nLikes: {self.likes} Dislikes: {self.dislikes}\nRating: {self.get_rating()}"

class Image:
    pass

class PostWithImage(Post, Image):
    pass

class Comment(Content):
    def __init__(self, post_id):
        super().__init__()         
        self.post_id = post_id     

    def __str__(self):
        return f"{self.author} commented on {self.post_id}: {self.text}" 

if __name__ == "__main__":
    post_with_image = PostWithImage()

    comment1 = Comment(1)
    comment2 = Comment(1)

    comment2.note = "some note"

    print(comment2)
    print(comment1)

