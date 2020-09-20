# Тестовое задание
Реализован класс, который помогает дополнить запрос по префиксу слова. 

# Использование

```
from classes import Autocompletor
...
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
