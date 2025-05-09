import flet as ft
from flet import AppBar, View
from flet.core.text import Text
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton

class Livro():
    def __init__(self, titulo, descricao, categoria, autor):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.autor = autor


def main(page: ft.Page):
    page.title = "Exercicio 2"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    lista = []

    def salvar_info(e):
        if input_titulo.value == "" or input_descricao.value == "" or input_categoria.value == "" or input_autor.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
            print("Campos vazios")
        else:
            print("Campos preenchidos")
            obj_livro = Livro(
                titulo=input_titulo.value,
                descricao=input_descricao.value,
                categoria=input_categoria.value,
                autor=input_autor.value
            )

            lista.append(obj_livro)
            input_titulo.value = ""
            input_descricao.value = ""
            input_categoria.value = ""
            input_autor.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_exibir.controls.clear()
        for livro in lista:
            lv_exibir.controls.append(
                ft.ListTile(
                    title=ft.Text(f"Titulo - {livro.titulo}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Vizualizar Detalhes", on_click=lambda _: page.go("/terceira"))
                        ],
                    )
                )
            )
        page.update()

    def Vizu_detalhes(e):
        lv_exibir.controls.clear()
        for livro in lista:
            lv_exibir.controls.append(
                ft.Text(value=f"{livro.titulo} - {livro.descricao} - {livro.categoria} - {livro.autor}"),
            )
        page.update()

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_info(e)
                    ),
                    ft.Button(
                        text="Exibir",
                        on_click=lambda _: page.go("/segunda")
                    )
                ],
            )
        )

        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Livros Cadastrados"), bgcolor=Colors.PRIMARY_CONTAINER),
                        lv_exibir,
                    ]
                )
            )
        page.update()

        if page.route == "/terceira":
            Vizu_detalhes(e)
            page.views.append(
                View(
                    "/Sobre o livro",
                    [
                    lv_exibir
                    ]
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    msg_sucesso = ft.SnackBar(
        content=ft.Text('Informaçoes salvas com sucesso!'),
        bgcolor=Colors.GREEN,
    )

    msg_erro = ft.SnackBar(
        content=ft.Text('Preencha os campos!'),
        bgcolor=Colors.RED,
    )

    input_titulo = ft.TextField(label="Titulo")
    input_descricao = ft.TextField(label="Descrição")
    input_categoria = ft.TextField(label="Categoria")
    input_autor = ft.TextField(label="Autor")

    lv_exibir = ft.ListView(
        height=500
    )

    page.on_route_change = gerenciar_rotas
    page.go(page.route)

    page.on_view_pop = voltar


ft.app(main)
