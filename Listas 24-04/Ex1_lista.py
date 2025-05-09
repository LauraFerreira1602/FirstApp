import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

class User():
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

def main(page: ft.Page):
    # Configurações
    page.title = "Exercicio 1"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []
    def salvar_info(e):
        if input_nome.value == "" or input_salario.value =="" or input_cargo.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
        else:
            obj_user = User(
                nome=input_nome.value,
                cargo=input_cargo.value,
                salario=input_salario.value
            )

            lista.append(obj_user)
            input_nome.value = ""
            input_cargo.value = ""
            input_salario.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()


    def verificar_campos(e):
        salario = input_salario.value

        if not salario.isnumeric():
            input_salario.error = True
            input_salario.error_text = "Digite somente numeros"
            page.update()
            return


    def exibir_lista(e):
        lv_exibir.controls.clear()
        for user in lista:
            lv_exibir.controls.append(
                ft.Text(value=f"{user.nome} - {user.cargo} - {user.salario}")
            )
        page.update()


    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_cargo,
                    input_salario,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_info(e)
                    ),
                    ft.Button(
                        text="Exibir lista",
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
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_exibir,
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text('Informaçoes salvas com sucesso!'),
        bgcolor=Colors.GREEN,
    )


    msg_erro = ft.SnackBar(
        content=ft.Text('Preencha os campos!'),
        bgcolor=Colors.RED,
    )

    input_nome = ft.TextField(label="Nome")
    input_cargo = ft.TextField(label="Cargo")
    input_salario = ft.TextField(label="Salario",
                                 on_change=verificar_campos)

    lv_exibir = ft.ListView(
        height=500
    )


    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
