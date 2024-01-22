class Twit:

    def __init__(self, twit_id: str, body: str, author: str):
        self.twit_id = twit_id
        self.body = body
        self.author = author


    def to_dict(self):
        return {
            'twit_id': self.twit_id,
            'body': self.body,
            'author': self.author
        }
