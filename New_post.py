from datetime import datetime

class Content:
    def __init__(self):
        self.author = input("Введіть псевдонім: ")
        self.text = input("Напишіть свій допис: ")
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.author} сказав(-ла) о {self.created_at}: {self.text}"

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

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.get_rating() == other.get_rating()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Post):
            return self.get_rating() < other.get_rating()
        return False

    def __gt__(self, other):
        if isinstance(other, Post):
            return self.get_rating() > other.get_rating()
        return False

    def __le__(self, other):
        if isinstance(other, Post):
            return self.get_rating() <= other.get_rating()
        return False

    def __ge__(self, other):
        if isinstance(other, Post):
            return self.get_rating() >= other.get_rating()
        return False

    def __str__(self):
        return (f"#{self.id} {self.author} сказав(-ла): {self.text}\n"
                f"Лайків: {self.likes} Дизлайків: {self.dislikes}\n"
                f"Рейтинг: {self.get_rating()}")

class Image:

    pass

class PostWithImage(Post, Image):
    def __init__(self):
        super().__init__()
        

class Comment(Content):
    def __init__(self, post_id):
        super().__init__()
        self.post_id = post_id

    def __str__(self):
        return f"{self.author} прокоментував(-ла) допис #{self.post_id}: {self.text}"

if __name__ == "__main__":
    post_with_image = PostWithImage()

    comment1 = Comment(1)
    comment2 = Comment(1)

    
    comment2.note = "якась нотатка"

    print(comment2)
    print(comment1)

