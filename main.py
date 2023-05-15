# Nome: Bruno Fukumori
# RM: 99486

# Nome: Erick Gruber
# RM: 99584

# Nome: João Cantalice
# RM: 550177

# Nome: Ricardo Hernandez
# RM: 99167

# Nome: Wesley Ninaja
# RM: 98115

print("\nInsira as toneladas colhidas por mês:\n")

total_harvest = 0
total_manual_loss = 0
total_machine_loss = 0

for month in range(1, 13, 1):
    harvest = float(input(f"\nMês {month}....: "))
    manual_loss = harvest * 0.05
    machine_loss = harvest * 0.15

    total_harvest += harvest
    total_manual_loss += manual_loss
    total_machine_loss += machine_loss

    print(f"\n\tPerda manual.......: {manual_loss:.2f}")
    print(f"\n\tPerda com máquina..: {machine_loss:.2f}")

print(
    "\n\nRELATÓRIO CONSOLIDADO:\n",
    f"Colheita do ano........: {total_harvest:.2f} Toneladas",
    f"Projeção de desperdício:",
    f"\tManual.................: {total_manual_loss:.2f}",
    f"\tCom máquina............: {total_machine_loss:.2f}",
    sep="\n\n",
)
