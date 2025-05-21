from .models import Item

def pages_processor(request):
    #pages = MyPage.objects.all()  # Замените MyPage на имя вашей модели
    pages = Item.objects.exclude(item_nav_position=0).order_by('-item_nav_position') #Исключаем те у кого item_nav_position=0
    return {'pages': pages}