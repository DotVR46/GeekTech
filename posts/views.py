from django.http import HttpResponse
from django.shortcuts import render


# передача строк в ответ
def hello(request):
    return HttpResponse("GeekTech")

# передача списка
# def hello(request):
#     my_list = [1, 2, 3, 4, "String"]
#     return HttpResponse(my_list)

# передача html-кода
# def hello(request):
#     body = """
#     <h1>Привет</h1>
#     <p>Параграф</p>
#     """
#     return HttpResponse(body)

# передача словаря, приходит только ключ
# def hello(request):
#     my_dict = {"name": "Alex"}
#     return HttpResponse(my_dict)

# передача заголовков и статуса ответа
# def hello(request):
#     headers = {"name": "Chyngyz"}
#     return HttpResponse("GeekTech", status=200, headers=headers)
