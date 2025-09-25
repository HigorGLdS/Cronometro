import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import random
import winsound

# ==== Variáveis globais ====
restante = 0
rodando = False
modo = "Livre"  # Livre | Pomodoro | Pausa
fade_step = 0
fade_direcao = 1
ciclo_pomo = 1
sons_ativos = True

mensagens = [
    "Bora, você tá mandando bem! 🚀",
    "Mais um minuto de foco = mais progresso!",
    "Não desiste agora! 💪",
    "Cada segundo conta 💻",
    "Foco hoje, resultado amanhã!",
]

# ==== Funções visuais ====

def animar_monitor():
    """Anima a tela do monitor com um fade suave de cor azul."""
    global fade_step, fade_direcao
    if not rodando:
        return

    fade_step += fade_direcao * 5
    if fade_step >= 100:
        fade_direcao = -1
    elif fade_step <= 0:
        fade_direcao = 1

    cor = f"#%02x%02x%02x" % (200 - fade_step, 230, 255)
    canvas.itemconfig(overlay_rect, fill=cor)
    root.after(150, animar_monitor)


def flash_monitor(cor1="red", cor2="white", vezes=8, delay=150):
    """Pisca a tela do monitor no fim do tempo."""
    def alternar(n):
        if n <= 0:
            canvas.itemconfig(overlay_rect, fill="white")
            return
        canvas.itemconfig(overlay_rect, fill=cor1 if n % 2 == 0 else cor2)
        root.after(delay, lambda: alternar(n - 1))
    alternar(vezes)


def pulso_label(label, base_size=28, step=1, growing=True):
    """Efeito de pulsar (aumentar/diminuir o texto suavemente)."""
    size = int(label.cget("font").split()[1]) if " " in label.cget("font") else base_size
    if growing:
        size += step
        if size >= base_size + 4:
            growing = False
    else:
        size -= step
        if size <= base_size - 2:
            growing = True
    label.config(font=("Consolas", size))
    root.after(100, lambda: pulso_label(label, base_size, step, growing))


# ==== Funções do cronômetro ====

def iniciar():
    """Inicia o cronômetro"""
    global restante, rodando, modo
    if not rodando:
        try:
            restante = int(entry_tempo.get())
            if restante <= 0:
                messagebox.showerror("Erro", "Digite um número maior que zero")
                return
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido")
            return
        rodando = True
        label_status.config(text=f"Iniciado ({modo})", fg="green")
        animar_monitor()
        pulso_label(label_tempo)  # anima tempo
        atualizar()


def pausar():
    """Pausa o cronômetro"""
    global rodando
    rodando = False
    label_status.config(text="⏸ Pausado", fg="orange")


def reiniciar():
    """Reinicia o cronômetro"""
    global rodando, restante
    rodando = False
    try:
        restante = int(entry_tempo.get())
        label_tempo.config(text=f"{restante} s", fg="black")
        barra["value"] = 0
        label_status.config(text="Reiniciado", fg="blue")
        canvas.itemconfig(overlay_rect, fill="white")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido")


def atualizar():
    """Atualiza a contagem regressiva"""
    global restante, rodando, ciclo_pomo

    if rodando and restante > 0:
        label_tempo.config(text=f"{restante} s")

        # cor do tempo
        if restante > 10:
            label_tempo.config(fg="green")
        elif restante > 5:
            label_tempo.config(fg="orange")
        else:
            label_tempo.config(fg="red")

        # barra de progresso
        try:
            total = int(entry_tempo.get())
            barra["value"] = ((total - restante) / total) * 100
        except:
            pass

        # mensagens motivacionais aleatórias no meio
        if restante % 30 == 0 and restante != 0:
            label_status.config(text=random.choice(mensagens), fg="purple")

        restante -= 1
        root.after(1000, atualizar)

    elif restante <= 0 and rodando:
        rodando = False
        if sons_ativos:
            winsound.Beep(1200, 700)

        flash_monitor()
        label_status.config(text=random.choice(mensagens), fg="purple")
        messagebox.showinfo("Fim", "Tempo esgotado!")

        # ciclo pomodoro automático
        if modo == "Pomodoro":
            ciclo_pomo += 1
            if ciclo_pomo % 4 == 0:
                pausa_longa()
            else:
                pausa_curta()


# ==== Modos Pomodoro ====

def pomodoro():
    global modo
    modo = "Pomodoro"
    entry_tempo.delete(0, tk.END)
    entry_tempo.insert(0, "1500")  # 25 min


def pausa_curta():
    global modo
    modo = "Pausa"
    entry_tempo.delete(0, tk.END)
    entry_tempo.insert(0, "300")  # 5 min


def pausa_longa():
    global modo
    modo = "Pausa"
    entry_tempo.delete(0, tk.END)
    entry_tempo.insert(0, "900")  # 15 min


def toggle_sons():
    global sons_ativos
    sons_ativos = not sons_ativos
    botao_som.config(text="🔊 Som: ON" if sons_ativos else "🔇 Som: OFF")


# ==== Interface ====

root = tk.Tk()
root.title("Cronômetro Computador")
root.geometry("500x420")
root.resizable(False, False)

# ==== Fundo ====
imagem = Image.open("assets/monitor.png")
imagem = imagem.resize((500, 400))
bg_image = ImageTk.PhotoImage(imagem)

canvas = tk.Canvas(root, width=500, height=400, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg_image)

# Overlay escuro translúcido só na tela do monitor
overlay_rect = canvas.create_rectangle(90, 55, 410, 230, fill="#000000", outline="")
canvas.itemconfig(overlay_rect, stipple="gray25")  # cria efeito de transparência

# ==== Widgets ====
entry_tempo = tk.Entry(root, font=("Consolas", 14), justify="center")
canvas.create_window(250, 70, window=entry_tempo)

botao_iniciar = tk.Button(root, text="▶ Iniciar", command=iniciar, font=("Helvetica", 12), bg="green", fg="white")
canvas.create_window(150, 110, window=botao_iniciar)

botao_pausar = tk.Button(root, text="⏸ Pausar", command=pausar, font=("Helvetica", 12), bg="orange", fg="white")
canvas.create_window(250, 110, window=botao_pausar)

botao_reiniciar = tk.Button(root, text="⟳ Reiniciar", command=reiniciar, font=("Helvetica", 12), bg="blue", fg="white")
canvas.create_window(350, 110, window=botao_reiniciar)

botao_pomo = tk.Button(root, text="Pomodoro (25m)", command=pomodoro, font=("Helvetica", 10))
canvas.create_window(150, 150, window=botao_pomo)

botao_pausa = tk.Button(root, text="Pausa (5m)", command=pausa_curta, font=("Helvetica", 10))
canvas.create_window(350, 150, window=botao_pausa)

botao_som = tk.Button(root, text="🔊 Som: ON", command=toggle_sons, font=("Helvetica", 10))
canvas.create_window(255, 150, window=botao_som)

label_tempo = tk.Label(root, text="0 s", font=("Consolas", 28), bg="white")
canvas.create_window(255, 200, window=label_tempo)

barra = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
canvas.create_window(250, 290, window=barra)

label_status = tk.Label(root, text="", font=("Helvetica", 12), bg="white")
canvas.create_window(250, 325, window=label_status)

# ==== Atalhos ====
root.bind("<Return>", lambda e: iniciar())
root.bind("r", lambda e: reiniciar())

root.mainloop()
