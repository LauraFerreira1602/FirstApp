import flet as ft

import datetime
from datetime import datetime


def main(page: ft.Page):
    # Configuraçoes da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    def verificar_idade(e):
        data_nascimento = datetime.strptime(str(input_data_nasc.value), "%d-%m-%Y")
        conta = 2025 - data_nascimento.year
        idade = int(conta)
        mes = datetime.today().month
        dia = datetime.today().day

        try:
            if mes < data_nascimento.month:
                idade = idade - 1

            elif mes == data_nascimento.month:
                if dia < data_nascimento.day:
                    idade = idade - 1

            if idade <= 17:
                txt_resultado.value =  f'Esta pessoa tem {idade} anos, ela é menor de idade'

            elif idade >= 18 and idade <= 120:
                txt_resultado.value =  f'Esta pessoa tem {idade} anos, ela é maior de idade'

            else:
                txt_resultado.value = f'Esta pessoa faleceu'

        except ValueError:
            txt_resultado.value = 'Data Invalida'

        page.update()

    input_data_nasc = ft.TextField(label="Data de Nascimento", hint_text="Digite a data do seu nascimento")
    btn_enviar = ft.FilledButton(text="Enviar", width=page.window.width, on_click=verificar_idade)
    txt_resultado = ft.Text(value="")

    page.add(
        ft.Column(
            [
                input_data_nasc,
                btn_enviar,
                txt_resultado
            ]
        )
    )


ft.app(main)