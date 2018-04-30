from django.shortcuts import render
from django.db.models import Q
from products.models import Product , parser
import re

# def product_LView(request):
#
#     queryset = Product.objects.all()
#     courseData = parser()
#     print('data is sent to views !!! ---->>>\n')
#
#     for x in range(1 , len(courseData["courses"]) ):     #len(courseData["courses"])
#         obj = Product.objects.get(pk=x)
#         original = obj.summary
#         obj.summary = re.sub(r'<.+?>', '', original)
#         obj.save()
#
#         # prodcut = Product()
#         # prodcut.category = courseData["courses"][x]["category"]
#         # prodcut.courseUrl = courseData["courses"][x]["courseUrl"]
#         # prodcut.duration = courseData["courses"][x]["duration"]
#         # prodcut.image = courseData["courses"][x]["image"]
#         # prodcut.name = courseData["courses"][x]["name"]
#         # prodcut.price = courseData["courses"][x]["price"]
#         # prodcut.promoMediaUrl = courseData["courses"][x]["promoMediaUrl"]
#         # prodcut.startDate = courseData["courses"][x]["startDate"]
#         # prodcut.summary = courseData["courses"][x]["summary"]
#         # prodcut.type = courseData["courses"][x]["type"]
#         # prodcut.instructorFullName = courseData["courses"][x]["creator"]["fullName"]
#         # prodcut.instructorImageUrl = courseData["courses"][x]["creator"]["imageUrl"]
#         # prodcut.instructorProfileUrl = courseData["courses"][x]["creator"]["profileUrl"]
#         #
#         # prodcut.save()
#     return render(request, "products/list.html" ,)

# '''
# my quey ---->>> SELECT *
#                 FROM "products_product"
#                 WHERE ("products_product"."name" LIKE %aaa% ESCAPE '\' OR "products_product"."category" LIKE %aaa% ESCAPE '\' OR "products_product"."summary" LIKE %aaa% ESCAPE '\' OR "products_product"."type" LIKE %aaa% ESCAPE '\' OR "products_product"."instructorFullName" LIKE %aaa% ESCAPE '\')
#
# '''
def search(request):
    query = request.GET.get('q')
    print(query + '\nsearch query***\n')
    results = Product.objects.filter(Q(name__icontains=query )
                                         | Q(category__icontains=query)
                                        | Q(summary__icontains=query)
                                        | Q(type__icontains=query)
                                        | Q(instructorFullName__icontains=query))
    # results = Product.objects.raw('SELECT * FROM products_product  WHERE ("products_product"."name" LIKE %sec%)   ')
    context = {
            'course':results
    }
    # print("my quey ---->>> "+ results.query.__str__() + "\n")
    return render(request ,'details.html' , context)

def product_list_view(request):
    # queryset = Product.objects.all()
    queryset = Product.objects.raw('SELECT * FROM products_product')
    context = {
        'course' : queryset
    }
    return render(request , 'details.html' , context)
