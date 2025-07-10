import reflex as rx

class RouterState(rx.State):
    current_path: str = "/"

    def on_load(self):
        self.current_path = "/"

    def set_path(self, path: str):
        self.current_path = path