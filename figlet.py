import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    try:
        # Verifica se foram passados 0 ou 2 argumentos
        if len(sys.argv) == 1:
            # Nenhum argumento, usar fonte aleatória
            font = random.choice(figlet.getFonts())
        elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            # Verifica se o nome da fonte é válido
            if sys.argv[2] in figlet.getFonts():
                font = sys.argv[2]
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")

        # Define a fonte escolhida
        figlet.setFont(font=font)

        # Solicita o texto ao usuário
        text = input("Input: ")

        # Exibe o texto em ASCII art
        print(figlet.renderText(text))

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
