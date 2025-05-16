import flet as ft
from flet import AppBar, View
from flet.core.text import Text
from flet.core.colors import Colors
from sqlalchemy import select
from models import *

def main(page: ft.Page):
    page.title = "Exercicio 1"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def salvar_info(e):
        if input_nome.value == "" or input_salario.value =="" or input_profissao.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
            print("Campos vazios")
        else:
            print("Campos preenchidos")
            obj_usuario = Usuario(
                nome=input_nome.value,
                profissao=input_profissao.value,
                salario=input_salario.value
            )

            obj_usuario.save()
            input_nome.value = ""
            input_profissao.value = ""
            input_salario.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
        page.update()


    def detalhes(nome, profissao, salario):
        txt_nome.value = nome
        txt_profissao.value = profissao
        txt_salario.value = salario

        page.go("/terceira")

    def exibir_lista(e):
        lv_exibir.controls.clear()
        sql_usuarios = select(Usuario)
        resultado_usuario = db_session.execute(sql_usuarios).scalars()

        for usuario in resultado_usuario:
            lv_exibir.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Nome: {usuario.nome}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Vizualizar detalhes", on_click=lambda _, u=usuario: detalhes(u.nome, u.profissao, u.salario)),
                        ]
                    )
                )
            )

        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastro de Usuario"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_profissao,
                    input_salario,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_info(e)
                    ),
                    ft.Button(
                        text="Exibir",
                        on_click=lambda _: page.go ("/segunda")
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
                        AppBar(title=Text("Usuarios Cadastrados"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_exibir,
                    ],
                )
            )

        if page.route == "/terceira":
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("Informações do Usuario"), bgcolor=Colors.SECONDARY_CONTAINER),
                        txt_nome,
                        txt_profissao,
                        txt_salario,
                    ]
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text('Dados salvos com sucesso!'),
        bgcolor=Colors.GREEN,
    )


    msg_erro = ft.SnackBar(
        content=ft.Text('Preencha os campos!'),
        bgcolor=Colors.RED,
    )

    input_nome = ft.TextField(label="Nome")
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salario")

    lv_exibir = ft.ListView(
        height=500
    )


    txt_nome = ft.Text()
    txt_profissao = ft.Text()
    txt_salario = ft.Text()


    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)


ft.app(main)
