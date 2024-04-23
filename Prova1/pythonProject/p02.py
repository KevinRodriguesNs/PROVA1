pop_A = 80000
pop_B = 200000
anos = 0
taxa_cre_A = 3
taxa_cre_B = 1.5

while pop_A <= pop_B:
    pop_A = pop_A * (1 + taxa_cre_A / 100)
    pop_B = pop_B * (1 + taxa_cre_B / 100)
    anos = anos + 1

print(f"Sera necessário {anos} anos para que o pais A ultrapasse o pais B.")