from .models import Category


# ----------------Writing a template context processor function to pass arguemnts to the base.html file-------------------------
def blog_Api_Context_Processor(request):
    context = {}
    ur = '/home/'
    if request.path.endswith(ur) or request.path.startswith(ur+'updatePost/')  :
        querySet = Category.objects.all()
        categories = [obj.name for obj in querySet]
        context['categ'] = categories
    return context
