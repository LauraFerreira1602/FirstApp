import flet as ft


def main(page: ft.Page):
    # Configuraçoes da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções

    def par_impar(e):
        numero = int(input_numero.value)
        resultado = numero % 2
        if resultado == 0:
            txt_resultado.value = f"Par"
        else:
            txt_resultado.value = f"Impar"

        page.update()


    input_numero = ft.TextField(label="Numero", hint_text="Digite seu numero")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=par_impar
    )
    txt_resultado = ft.Text(value="")

    # Construir layout
    page.add(
        ft.Column(
            [
                input_numero,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)
