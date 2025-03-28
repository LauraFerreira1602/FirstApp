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
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ElevatedButton(text="Enviar", on_click=lambda _: page.go("/segunda"))
                ]
            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value=f"Titulo: {input_titulo.value}"),
                        Text(value=f"Descrição: {input_descricao.value}"),
                        Text(value=f"Categoria: {input_categoria.value}"),
                        Text(value=f"Autor: {input_autor.value}")
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
    input_titulo = ft.TextField(label="Titulo", hint_text="titulo do livro")
    input_descricao = ft.TextField(label="Descrição", hint_text="descrição do livro")
    input_categoria = ft.TextField(label="Categoria", hint_text="categoria do livro")
    input_autor = ft.TextField(label="Autor", hint_text="nome do autor")


ft.app(main)