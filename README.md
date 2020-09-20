# Тестовое задание
Реализован класс, который помогает дополнить запрос по префиксу слова.

# Описание задания
Программе даётся художественный текст. 
Она должна его обработать, сделав словарь, в котором для каждого слова хранится его частота встречаемости. 
После обработки текста должна быть возможность по префиксу строки находить слова, которые вероятнее всего будут напечатаны далее. 
В качестве критерия вероятности выступает частота упоминания в предложенном тексте. 

# Использование

```
from classes import Autocompletor

autocompletor = Autocompletor()
autocompletor.build_dictionary()

res = autocompletor.search_top_k_strings("th")
print(res) # ['the', 'that', 'this', 'thou', 'thy', 'thee', 'then', 'they', 'than', 'their']

res = autocompletor.search_top_k_strings("scan")
print(res) # ['scandal', 'scandalous', 'scant']

res = autocompletor.search_top_k_strings("q")
print(res) # ['queen', 'quarrel', 'quickly', 'quiet', 'quoth', 'quick', 'question', 'quite', 'quit', 'quench']

```

# Описание решения

