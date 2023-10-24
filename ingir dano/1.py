with open("D:/documents/desktop/putan/1/text_1_var_56") as file:
    text = file.readlines()
chastota = {}
prepinanie = [".", ",", "!", "?",":",";"]
for line in text:
    for s in prepinanie:
        line = line.replace(s," ")
    line = line.split()
    for e in line:
        if e in chastota:
            chastota[e] += 1
        else:
            chastota[e] = 1
chastota = sorted(chastota.items(), key=lambda item: item[1], reverse=True)
with open('D:/documents/desktop/putan/1/result_1.txt', 'w') as file:
    for key, value in chastota:
        file.write(f'{key}:{value}\n')
