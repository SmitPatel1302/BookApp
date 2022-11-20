from django.shortcuts import render
from django.views import View

# Class to render index page of the Store app
class RenderStore(View):
    template_name = 'store/storeIndex.html'

    def get(self, request):
        return render(request, self.template_name)


# Class to render single product page of the item
class RenderSingleProduct(View):
    template_name = 'store/singleProduct.html'

    def get(self, request):
        return render(request, self.template_name)

# Class to render Checkout page
class RenderCheckout(View):
    template_name = 'store/checkout.html'

    def get(self, request):
        return render(request, self.template_name)