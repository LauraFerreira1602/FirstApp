import flet as ft


def main(page: ft.Page):
    # Configuraçoes da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def adicao(e):
        numero1 = int(num1.value)
        numero2 = int(num2.value)
        txt_resultado.value =  f'{numero1} + {numero2} = {numero1 + numero2}'

        page.update()

    def subtracao(e):
        numero1 = int(num1.value)
        numero2 = int(num2.value)
        txt_resultado.value = f'{numero1} - {numero2} = {numero1 - numero2}'

        page.update()

    def multiplicacao(e):
        numero1 = int(num1.value)
        numero2 = int(num2.value)
        txt_resultado.value = f'{numero1} * {numero2} = {numero1 * numero2}'

        page.update()

    def divisao(e):
        numero1 = int(num1.value)
        numero2 = int(num2.value)
        txt_resultado.value = f'{numero1} / {numero2} = {numero1 / numero2}'

        page.update()

    num1 = ft.TextField(label="Numero 1", hint_text="Digite seu primeiro numero")
    num2 = ft.TextField(label="Numero 2", hint_text="Digite seu segundo numero")
    btn_adicao = ft.FilledButton(text="Adição",width=page.window.width,on_click= adicao)
    btn_subtracao = ft.FilledButton(text="Subtração",width=page.window.width,on_click= subtracao)
    btn_multiplicacao = ft.FilledButton(text="Multiplicação",width=page.window.width,on_click= multiplicacao)
    btn_divisao = ft.FilledButton(text="Divisão",width=page.window.width,on_click= divisao)

    txt_resultado = ft.Text(value="")

    page.add(
        ft.Column(
            [
                num1,
                num2,
                btn_adicao,
                btn_subtracao,
                btn_multiplicacao,
                btn_divisao,
                txt_resultado,
            ]
        )
    )


ft.app(main)