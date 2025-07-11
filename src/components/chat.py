import reflex as rx

class ChatState(rx.State):
    has_started: bool = False

    def start_chat(self):
        self.has_started = True

def chat_main() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                # 타이틀 (채팅 시작 전만 보여짐)
                rx.cond(
                    rx.Var.create(ChatState.has_started) == False,
                    rx.vstack(
                        rx.heading("ChatGPT Prototype", size="7", align="center"),
                        rx.text("Ask me anything...", size="4", color="gray", align="center"),
                        spacing="2",
                    ),
                ),
                # 채팅 입력창
                rx.input(
                    placeholder="Type your message...",
                    width="100%",
                    border_radius="xl",
                    padding="1rem",
                    box_shadow="sm",
                    on_blur=ChatState.start_chat,
                ),
                rx.button(
                    "Send",
                    width="100%",
                    border_radius="xl",
                    margin_top="1rem",
                    color_scheme="blue",
                    size="3",
                ),
                # 초기 버튼 3개
                rx.cond(
                    rx.Var.create(ChatState.has_started) == False,
                    rx.hstack(
                        rx.button("Example 1", size="4", flex="1", border_radius="xl", variant="soft"),
                        rx.button("Example 2", size="4", flex="1", border_radius="xl", variant="soft"),
                        rx.button("Example 3", size="4", flex="1", border_radius="xl", variant="soft"),
                        spacing="4",
                        margin_top="2rem",
                    ),
                ),
                spacing="4",
                align="stretch",
            ),
            padding="3rem",
            width="100%",
            max_width="600px",
            min_height="100vh",
        ),
    )
