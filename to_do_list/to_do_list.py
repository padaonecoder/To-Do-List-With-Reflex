import reflex as rx

class State(rx.State):
    task: str = ""
    tasks: list[dict] = []

    def set_task(self, value: str):
        self.task = value

    def add_task(self):
        if self.task.strip():
            self.tasks.append({"text": self.task.strip(), "done": False})
            self.task = ""

    def toggle_task(self, index: int):
        self.tasks[index]["done"] = ~self.tasks[index]["done"]

    def delete_task(self, index: int):
        del self.tasks[index]

def index():
    return rx.box(
        rx.flex(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.spacer(),
                        rx.color_mode.button(),
                        width="100%",
                    ),
                    rx.heading("📝 To-Do List", size="8"),
                    rx.form(
                        rx.vstack(
                            rx.input(
                                placeholder="Write a task...",
                                value=State.task,
                                on_change=State.set_task,
                                width="100%",
                            ),
                            rx.button("Add task"),
                            spacing="2",
                        ),
                        on_submit=State.add_task,
                        width="100%",
                    ),
                    rx.divider(),
                    rx.foreach(
                        State.tasks,
                        lambda t, i: rx.hstack(
                            rx.box(
                                width="20px",
                                height="20px",
                                border="2px solid gray",
                                border_radius="4px",
                                background_color=rx.cond(
                                    t["done"], "green", "transparent"
                                ),
                                cursor="pointer",
                                on_click=lambda: State.toggle_task(i),
                            ),
                            rx.text(
                                t["text"],
                                text_decoration=rx.cond(t["done"], "line-through", "none"),
                                color=rx.cond(
                                    t["done"],
                                    "gray",
                                    rx.color_mode_cond("black", "white")
                                ),
                                font_weight="bold",
                                
                                flex="1",
                            ),
                            rx.text(
                                "❌",
                                color="red",
                                cursor="pointer",
                                on_click=lambda: State.delete_task(i),
                            ),
                            spacing="3",
                            align="center",
                            width="100%",
                        )
                    ),
                    spacing="4",
                    width="100%",
                ),
                border="4px solid #ccc",
                border_radius="12px",
                box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
                padding="32px",
                style=rx.color_mode_cond(
                    {"background": "linear-gradient(#669bbc, #003049, #fdf0d5, #c1121f, #780000)"},  # modo claro
                    {"background": "#1a1a1a"}  # modo oscuro
                ),
                width="100%",
                max_width="500px",
            ),
            justify="center",
            align="center",
            height="100vh",
        ),
        padding="16px",
        background=rx.color_mode_cond(
            "linear-gradient(#780000, #c1121f, #fdf0d5, #003049, #669bbc)",  # modo claro
            "#121212"  # modo oscuro
        ),
    )

app = rx.App()
app.add_page(index)