import reflex as rx
from src.states.sidebar_state import SidebarState

def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                # 사이드바
                rx.cond(
                    SidebarState.show_sidebar,
                    rx.box(
                        rx.button(
                            rx.hstack(
                                rx.icon(tag="plus"),
                                rx.text("새 대화 시작"),
                            ),
                            width="100%",
                            height="48px",
                            on_click=SidebarState.new_chat,
                            color_scheme="blue",
                            variant="solid",
                        ),
                        width="180px",
                        height="80px",
                        padding="1rem",
                        bg={"light": "#f5f5f5", "dark": "gray.900"},
                        color={"light": "black", "dark": "white"}, 
                        transition="all 0.3s ease",
                    ),
                    rx.box(
                        width="0px",
                        height="80px",
                        transition="all 0.3s ease",
                        padding="1rem",
                    ),
                ),

                # 토글 버튼
                rx.box(
                    rx.button(
                        rx.icon(tag=rx.cond(SidebarState.show_sidebar, "chevrons-left", "chevrons-right")),
                        on_click=SidebarState.toggle_sidebar,
                        variant="ghost",
                        size="1",
                        height="48px",
                    ),
                    width="48px",
                    height="80px",
                    display="flex",
                ),
                align=rx.cond(SidebarState.show_sidebar, "center", "top"),
            ),
            rx.box(
                rx.text(
                    "test",
                    width="100%",
                    height="100%"
                ),
                padding="1rem",
            ),
            height="100vh",
        ),
        border_right="1px solid #e0e0e0",
        position="sticky",
        top="0",
        z_index="1000",
        bg={"light": "#f5f5f5", "dark": "gray.900"},
        color={"light": "black", "dark": "white"}, 
    )
