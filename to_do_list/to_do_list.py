import reflex as rx

class State(rx.State):
    task: str = ""
    tasks: list[dict] = []

    def add_task(self):
        if self.task.strip():
            self.tasks.append({"text": self.task.strip(), "done": False})
            self.task = ""

    def toggle_task(self, index: int):
        self.tasks[index]["done"] = ~self.tasks[index]["done"]

    def delete_task(self, index: int):
        del self.tasks[index]

def index():
    return rx.center(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            rx.heading("📝 Lista de tareas", size="8"),
            rx.input(
                placeholder="Escribe una tarea...",
                value=State.task,
                on_change=lambda e: State.set_task(e),
                width="100%",
            ),
            rx.button("Añadir tarea", on_click=State.add_task),
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
                            t["done"],
                            "green",
                            "transparent"
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
            width="500px",
        ),
        padding="6",
        height="100vh",
    )

app = rx.App()
app.add_page(index)