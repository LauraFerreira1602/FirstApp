import flet as ft
from flet import AppBar, View
from flet.core.text import Text
from flet.core.colors import Colors
from sqlalchemy import select
from models import *

def main(page: ft.Page):
    page.title = "Exercicio 2"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

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

            obj_livro.save()
            input_titulo.value = ""
            input_descricao.value = ""
            input_categoria.value = ""
            input_autor.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()


    def detalhes(titulo, descricao, categoria, autor):
        txt_titulo.value = titulo
        txt_descricao.value = descricao
        txt_categoria.value = categoria
        txt_autor .value = autor

        page.go("/terceira")


    def exibir_lista(e):
        lv_exibir.controls.clear()
        sql_livros = select(Livro)
        resultado_livro = db_session.execute(sql_livros).scalars()

        for livro in resultado_livro:
            lv_exibir.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Titulo: {livro.titulo}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Ver Sobre", on_click=lambda _, l=livro: detalhes(l.titulo, l.descricao, l.categoria, l.autor)),
                        ]
                    )
                )
            )


    def gerenciar_rotas(e):
        # page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro de Livros"), bgcolor=Colors.PRIMARY_CONTAINER),
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

        if page.route == "/terceira":
            page.views.append(
                View(
                    "/terceira",
                    [
                    AppBar(title=Text("Informações do Livro"), bgcolor=Colors.SECONDARY_CONTAINER),
                    txt_titulo,
                    txt_descricao,
                    txt_categoria,
                    txt_autor
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


    txt_titulo = ft.Text()
    txt_descricao = ft.Text()
    txt_categoria = ft.Text()
    txt_autor = ft.Text()


    page.on_route_change = gerenciar_rotas
    page.go(page.route)

    page.on_view_pop = voltar


ft.app(main)
