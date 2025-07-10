import reflex as rx

def chat_main() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("ChatGPT Prototype", size="7"),
            rx.text("Ask me anything...", size="4", color="gray"),
            rx.spacer(),
            rx.input(placeholder="Type your message...", width="100%"),
            rx.button("Send", margin_top="1rem"),
            spacing="4",
            align="stretch",
            height="100%",
        ),
        padding="2rem",
        width="80%",
        min_height="100vh",
    )