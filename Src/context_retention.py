class ContextManager:
    def __init__(self):
        self.context = []

    def update_context(self, user_input):
        self.context.append(user_input)
        if len(self.context) > 5:
            self.context.pop(0)
        return self.context

    def get_context(self):
        return " ".join(self.context)

