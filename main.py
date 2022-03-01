arquivo = open('produtos.txt','r')
total = 0
for i in arquivo:
    i = i.split(",")
    total = total + float(i[1].rstrip("\n"))
   
print(f'Total da compra foi de R$:{total}'.format(total))