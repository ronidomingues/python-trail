from fpdf import FPDF

project = input("Digite a descrição do projto: ")
estimated_hours = input("Digite o total de horas estimadas: ")
hourly_rate = input("Digite o valor da hora trabalhada: ")
term = input("Digite o prazo estimado para conclusão: ")

total_value = int(estimated_hours) * int(hourly_rate)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

#pdf.image("template.png", x=0, y=0)

pdf.text(115,145, project)
pdf.text(115, 160, estimated_hours)
pdf.text(115, 175, hourly_rate)
pdf.text(115, 190, term)
pdf.text(115, 205, str(total_value))

pdf.output("aula_01.pdf")

print("Orçamento gerado com sucesso!")
