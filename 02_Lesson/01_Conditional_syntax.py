
""" 1. Синтаксис условной инструкции
------------------------------------
Все ранее рассматриваемые программы имели линейную структуру: все инструкции выполнялись
последовательно одна за одной, каждая записанная инструкция обязательно выполняется.

Допустим мы хотим по данному числу x определить его абсолютную величину (модуль).
Программа должна напечатать значение переменной x, если x>0 или же величину -x
в противном случае. Линейная структура программы нарушается: в зависимости
от справедливости условия x>0 должна быть выведена одна или другая величина.
Соответствующий фрагмент программы на Питоне имеет вид: """

x = int(input())
if x > 0:
    print(x)
else:
    print(-x)

""" В этой программе используется условная инструкция if (если).
После слова if указывается проверяемое условие (x > 0), завершающееся двоеточием.
После этого идет блок (последовательность) инструкций, который будет выполнен, если 
условие истинно, в нашем примере это вывод на экран величины x. 
Затем идет слово else (иначе), также завершающееся двоеточием, и блок инструкций,
который будет выполнен, если проверяемое условие неверно, в данном случае будет 
выведено значение -x.

Итак, условная инструкция в Питоне имеет следующий синтаксис:

    ++++++++++++++++++++++

    if Условие:
        Блок инструкций 1
    else:
        Блок инструкций 2

    ++++++++++++++++++++++

Блок инструкций 1 будет выполнен, если Условие истинно. 
Если Условие ложно, будет выполнен Блок инструкций 2.

В условной инструкции может отсутствовать слово else и последующий блок.
Такая инструкция называется неполным ветвлением. Например, если дано число x и мы хотим 
заменить его на абсолютную величину x, то это можно сделать следующим образом: """

x = int(input())
if x < 0:
    x = -x
print(x)

""" В этом примере переменной x будет присвоено значение -x, но только в том случае,
когда x<0. А вот инструкция print(x) будет выполнена всегда, независимо от проверяемого
условия.

Для выделения блока инструкций, относящихся к инструкции if или else в языке Питон 
используются отступы. Все инструкции, которые относятся к одному блоку, должны иметь равную
величину отступа, то есть одинаковое число пробелов в начале строки.
Рекомендуется использовать отступ в 4 пробела и не рекомедуется использовать в качестве
отступа символ табуляции. """