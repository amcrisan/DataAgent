class MessageContent:
    def __init__(self, text=None, image=None, tags=None,caption=None):
        self.text = text
        self.image = image
        self.tags = tags if tags is not None else []
        self.caption = caption

    def get_text(self):
        return self.text

    def get_image(self):
        return self.image

    def get_tags(self):
        return self.tags
    
    def get_caption(self):
        return self.caption

    def to_json(self):
        return {
            'text': self.text,
            'image': self.image if self.image else None,
            'tags': self.tags,
            'caption': self.caption
        }
