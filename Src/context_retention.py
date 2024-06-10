class ContextManager:
    def __init__(self):
        self.context = {}

    def update_context(self, user_input):
        # Update context based on user input (this is a simple example)
        self.context['last_input'] = user_input
        return self.context

