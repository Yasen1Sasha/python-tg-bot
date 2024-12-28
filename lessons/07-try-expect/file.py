print('Input N1:')
n1 = input()
print('Input N2:')
n2 = input()


try:
    #d = int(n1) / int(n2)
    print(d)
except ZeroDivisionError:
    print('ділення на нулік')
except TypeError:
    print('щО ЗА НЕРОЗУМНИЙ ПРОГРАМІСТ')

    d = int(n1) / int(n2)
    print('переведено в INT: ', d)
finally:
    print('блок винятків завершено')


print('програм працуєст')