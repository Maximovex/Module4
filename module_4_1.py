from fake_math import divide as fakediv
from true_math import divide as truediv

print('Деление на ноль как в школе: ',fakediv(5,0))
print('Верное деление на ноль: ', truediv(7,0))