import flet as ft
from flet import AppBar, View
from flet.core.text import Text
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton


def main(page: ft.Page):
    page.title = "Exemplo Rotas"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/primeira",
                [
                    AppBar(title=Text("Primeira tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda"))
                ]
            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f"Bem vindo {input_nome.value}")
                    ]
                )
            )
        page.update()


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = gerenciar_rotas
    page.go(page.route)
    page.on_view_pop = voltar
    input_nome = ft.TextField(label="Nome", hint_text="digite seu nome")

ft.app(main)