"""
实现orm字段
"""


class Field:
    def __init__(self, name=None, unique=False, max_length=None, primary_key=False, null=False, blank=False,
                 default=None, increment=False, index=False, choices=None, comments=None):
        self.name = name
        self.unique = unique
        self.max_length = max_length
        self.primary_key = primary_key
        self.null = null
        self.increment = increment
        self.index = index
        self.blank = blank
        self.default = default
        self.choices = choices
        self.comments = comments

    def __str__(self):
        return f"{self.name}"


class VarChar(Field):
    def __init__(self):
        super().__init__()