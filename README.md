# 🖥️ Cronômetro Pomodoro com Tkinter  

Um cronômetro interativo desenvolvido em **Python** com **Tkinter**, inspirado na técnica **Pomodoro**, que ajuda a melhorar o foco e a produtividade.  
O design simula um **monitor de computador animado**, exibindo efeitos de luz, mensagens motivacionais e sons ao fim de cada ciclo.  

---

## 📌 Funcionalidades  

- ⏱ **Cronômetro personalizado**: defina manualmente o tempo desejado.  
- 🍅 **Modo Pomodoro**: sessões de 25 minutos com pausas automáticas.  
- ☕ **Pausa curta**: intervalo de 5 minutos.  
- 🛑 **Pausa longa**: intervalo de 15 minutos após 4 ciclos de Pomodoro.  
- 🔊 **Notificação sonora**: alerta sonoro ao fim do ciclo (pode ser ativado/desativado).  
- ✨ **Animações visuais**:  
  - Efeito de **fade azul** no monitor durante a execução.  
  - **Pulsar no texto** do tempo restante.  
  - **Piscar em vermelho/branco** ao finalizar o cronômetro.  
- 💬 **Mensagens motivacionais aleatórias** durante a execução.  
- 🎨 **Interface estilizada**: imagem de fundo de um monitor + overlay translúcido.  

---

## 📂 Estrutura do Projeto  

```bash
cronometro_pomodoro/
│── assets/
│   └── monitor.png       # Imagem usada como fundo (monitor estilizado)
│── main.py               # Código principal do cronômetro
│── README.md             # Documentação do projeto
🚀 Como Executar
1️⃣ Pré-requisitos
Python 3.10+ (recomendado Python 3.12 ou 3.13)

Bibliotecas necessárias:

bash
Copiar código
pip install pillow
O Tkinter já vem incluso no Python em Windows e Linux.

2️⃣ Executar o projeto
No terminal, rode:

bash
Copiar código
python main.py
🎮 Controles
Enter → Inicia o cronômetro.

R → Reinicia com o valor atual digitado.

Botões na tela:

▶ Iniciar

⏸ Pausar

⟳ Reiniciar

Pomodoro (25m)

Pausa (5m)

Som ON/OFF

📸 Interface
O programa exibe um monitor estilizado com a contagem no centro, barra de progresso e mensagens dinâmicas.
O fundo (monitor) está no arquivo:

bash
Copiar código
assets/monitor.png
🔮 Melhorias Futuras
 Exportar estatísticas de ciclos (JSON/CSV).

 Histórico de sessões finalizadas.

 Customização de cores da tela.

 Versão com interface em PyQt.

 Suporte multiplataforma com sons customizados.

👨‍💻 Autor
Projeto desenvolvido por Higor Gabriel ✨
Estudante e entusiasta de Python, automação e desenvolvimento de aplicações interativas.
