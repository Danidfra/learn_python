from func import func_105;


list_n = func_105.date_inputs()
dic_notas = (func_105.notas(list_n, sit=True)) if input('Gostaria de saber sobre a situação da turma? S/N ').lower().strip() in 's' else (func_105.notas(list_n, sit=False))


print(dic_notas)