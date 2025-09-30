#a = 5
#b = 6
#result = 5 == 6  #сохраняем результат операции в переменную
#print(result)   # False - 5 не равно 6
#print(a != b)   # True
#print(a > b)    # False - 5 меньше 6
#print(a < b)    # True
from django.db.models.expressions import result
from django.templatetags.i18n import language

#bool1 = True
#bool2 = False
#print(bool1 == bool2)   # False - bool1 не равно bool2

#x and y

#age = 22
#weight = 58
#result = age > 21 and weight == 58
#print(result)   # True

#result = 4 and "w"
#print(result)   #w, так как 4 равно True, возравращает

#result = 0 and "w"
#print(result)   # 0, так как 0 эквалентно False

#x or y

#age = 22
#isMarried = False
#result = age > 21 or isMarried
#print(result)   # True, так как выражения age > 32 равно True

#значения in набор_значений

#message = "hello world!"
#hello = "hello"
#print(hello is message) # False

#gold = "gold"
#print(gold not in message)  # True

#message = "hello world"
#hello = "hello"
#print(hello not in message)    # False

#gold = "gold"
#print(gold not in message)     # True

#language = "english"
#if language == "english":
    #print("Hello")
#print("End")

#language = "english"
#if language == "english":
    #print("hello")
    #print("end")

#language = "russian"
#if language == "english":
    #print("hello")
    #print("World")
#else:
    #print("Привет")
    #print("мир")

#language = "german"
#if language == "english":
    #print("Hello")
    #print("World")
#elif language == "german":
    #print("Hello")
    #print("World")
#else:
    #print("Привет")
    #print("мир")

#language = "german"
#if language == "english":
    #print("Hello")
    #print("World")
#elif language == "german":
    #print("Hello")
    #print("Welt")
#else:
    #print("Привет")
    #print("мир")

#language = "german"
#if language == "english":
    #print("Hello")
#elif language == "german":
    #print("Hallo")
#elif language == "french":
    #print("Salut")
#else:
    #print("Привет")

#language = "english"
#daytime = "morning"
#if language == "english":
    #print("English")
    #if daytime == "morning":
        #print("Godd morning")
    #else:
        #print ("Good evening")

#language = "english"
#daytime = "morning"
#if language == "english":
    #print("English")
#if daytime == "morning":
    #print("Good morning")
#else:
    #print("Good evening")

#language = "russian"
#daytime = "morning"
#if language == "english":
#    if daytime == "morning":
#        print("Good evening")
#else:
#    if daytime == "morning":
#        print("доброе утро")
#    else:
#        print("Добрый вечер")




