# Проект 1. Анализ резюме из HeadHunter

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[3. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[4. Результат](.README.md#Результат)    
[5. Выводы](.README.md#Выводы) 

### Описание проекта    
Проект заключается в подготовке данных для дальнейшей работы с данными над задачей прогнозирования желаемого уровня ЗП соискателя. 
Исходный датасет можно скачать [здесь](https://drive.google.com/file/d/1hapbVzJLaBLHQHOf8FkRZzIH2ltevrw6/view?usp=sharing)  

:arrow_up:[к оглавлению](_)

### Краткая информация о данных
[Датасет](https://drive.google.com/file/d/1hapbVzJLaBLHQHOf8FkRZzIH2ltevrw6/view?usp=sharing) представляет собой базу данных резюме, выгруженную с сайта hh.ru и содержит следующую информацию:
Пол, возраст	
ЗП	
Ищет работу на должность:	
Город, переезд, командировки	
Занятость	
График	
Опыт работы	
Последнее/нынешнее место работы	
Последняя/нынешняя должность	
Образование и ВУЗ	
Обновление резюме	
Авто

Перед запускам датасет нужно сохранить в папку data\
  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  
1. Базовый анализ структуры данных
2. Преобразование данных
3. Разведывательный анализ
4. Очистка данных

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
В результате преобразования и очистки данных получили базу без пропусков, выраженных анамолий и выбросов, создали несколько дополнительных признаков, с которым можно работать, выявили зависимости между рядом признаков и желаемой ЗП.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
Прослеживается зависимость уровня желаемой ЗП от пола, возраста, образования, города соискателя, а также готовности к командировкам и переезду. Эти признаки являются важными при построении модели прогнозирования желаемого уровня ЗП.

:arrow_up:[к оглавлению](.README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами