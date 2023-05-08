# **Генератор паролей**
### **Описание**

Генерирует пароли разной сложности учитывая его длинну, верхний регистр, цифры и испец. символов.

### **Стек**
![python version](https://img.shields.io/badge/Python-3.10.2-green)
![django version](https://img.shields.io/badge/Django-4.1.5-green)

### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему windows и утилиту git bash.<br/>
Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
https://github.com/artyom-vah/password-generator.git
```


2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

### *Генерация паролей любой сложности*:

1. С учетом длинны пароля от 4 до 50 символов;
2. С учетом верхнего регистра: "*ABCDEFGHIJKLMNOPQRSTUVWXYZ*";
3. С учетом цифр "*0123456789*" ;
4. С учетом спец. символов "*!@#$%^&*()";
5.  По умолчанию генерация происходит в нижнем регистре "*abcdefghijklmnopqrstuvwxyz*".

### *Пример готового проекта*
##### 1й скрин:
![Screenshot_1](https://github.com/artyom-vah/password-generator/blob/main/screens/Screenshot_1.jpg)

##### 2й скрин:
![Screenshot_2](https://github.com/artyom-vah/password-generator/blob/main/screens/Screenshot_2.jpg)

##### 3й скрин:
![Screenshot_3](https://github.com/artyom-vah/password-generator/blob/main/screens/Screenshot_3.jpg)
