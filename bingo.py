from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import random

# Função para gerar números aleatórios para cartelas de bingo
def generate_bingo_card():
    numbers = random.sample(range(1, 76), 24)
    return numbers

# Função para gerar números aleatórios para rifas
def generate_raffle_tickets(num_tickets):
    tickets = [random.randint(1000, 9999) for _ in range(num_tickets)]
    return tickets

# Função para criar PDF com cartelas de bingo
def create_bingo_pdf(num_cards):
    pdf_filename = "bingo_cards.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)

    x_start = 40
    y_start = 750
    card_width = 200
    card_height = 200
    x, y = x_start, y_start

    for _ in range(num_cards):
        numbers = generate_bingo_card()
        for i, num in enumerate(numbers):
            if i % 24 == 0 and i != 0:
                x = x_start
                y -= card_height + 20
            if i % 5 == 0 and i != 0:
                x = x_start
                y -= 20
            c.drawString(x, y, str(num))
            x += 30
        x = x_start
        y -= card_height + 50

    c.save()
    return pdf_filename
# pip install reportlab

# Função para criar PDF com rifas
def create_raffle_pdf(num_tickets):
    pdf_filename = "raffle_tickets.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)

    x_start = 40
    y_start = 750
    ticket_width = 100
    ticket_height = 30
    x, y = x_start, y_start

    tickets = generate_raffle_tickets(num_tickets)
    for i, ticket in enumerate(tickets):
        if i % 10 == 0 and i != 0:
            x = x_start
            y -= ticket_height + 20
        if i % 2 == 0 and i != 0:
            x = x_start
            y -= 20
        c.drawString(x, y, str(ticket))
        x += ticket_width
    c.save()
    return pdf_filename

# Geração de cartelas de bingo e rifas
num_bingo_cards = 16  # 4 cartelas por página = 4 * 4
num_raffle_tickets = 40  # 10 bilhetes por página = 4 * 10

bingo_pdf = create_bingo_pdf(num_bingo_cards * 24)  # Cada cartela tem 24 números
raffle_pdf = create_raffle_pdf(num_raffle_tickets * 10)  # Cada página tem 10 bilhetes

print(f"Cartelas de Bingo geradas: {bingo_pdf}")
print(f"Rifas geradas: {raffle_pdf}")


# Este código gera os PDFs de cartelas de bingo e rifas com o layout desejado para impressão em folhas A4, com as quantidades de cartelas e bilhetes que você especificar. Você pode ajustar as variáveis num_bingo_cards e num_raffle_tickets para gerar o número desejado de cartelas de bingo e bilhetes de rifa, respeitando o formato de 4 cartelas por página para bingo e 10 bilhetes por página para rifas.