import reflex as rx

class SidebarState(rx.State):
    show_sidebar: bool = True

    def toggle_sidebar(self):
        self.show_sidebar = not self.show_sidebar

    def new_chat(self):
        print("새 대화 시작")  # 서버 로그에 출력되며 UI에는 영향 없음