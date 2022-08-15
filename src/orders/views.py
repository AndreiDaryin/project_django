from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DeleteView, DetailView
from django.urls import reverse_lazy
from book.models import Book
from . models import Cart, BookInCart, Order

def get_cart(view):
    cart_id = view.request.session.get("cart")
    if not cart_id:
        if view.request.user.is_anonymous:
            customer = None
        else:
            customer = view.request.user
        cart = Cart.objects.create(
            customer = customer
        )
        view.request.session["cart"] = cart.pk
    else:
        cart = Cart.objects.get(pk=cart_id)
    return cart

class DeleteFromCart(DeleteView):
    template_name = "orders/delete-item.html"
    model = BookInCart
    success_url = reverse_lazy("orders:add-to-cart")

class UpdateCart(DetailView):
    template_name = "orders/cart.html"
    model = BookInCart
    def get_object(self, **kwargs):
        cart = get_cart(self)
        for good in self.request.GET.keys():
            if good[:5] == "good_":
                good_in_cart_pk = good.split("_")[1]
                book_in_cart = BookInCart.objects.get(pk=int(good_in_cart_pk))
                book_in_cart.quantity = int(self.request.GET.get(good))                
                book_in_cart.price = book_in_cart.book.price  * book_in_cart.quantity
                book_in_cart.save()
        action_type = self.request.GET.get('action_type')
        customer_name = self.request.GET.get('customer_name')
        customer_email = self.request.GET.get('customer_email')
        customer_adress = self.request.GET.get('customer_adress')
        customer_phone = self.request.GET.get('customer_phone')
        if action_type == 'Заказать':
            order = Order.objects.create(
                cart=book_in_cart.cart,
                name=customer_name,
                email=customer_email,
                adress=customer_adress,
                phone_number=customer_phone
            )
            self.request.session.delete('cart')
        return  cart

    def render_to_response(self, context, **response_kwargs):
        action_type = self.request.GET.get('action_type')
        if action_type == 'Заказать':
            return HttpResponseRedirect('/')
        return super().render_to_response(context, **response_kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddToCart(TemplateView):
    template_name = "orders/cart.html"
    def get_context_data(self, **kwargs):
        cart_id = self.request.session.get("cart")
        book_id = self.request.GET.get("book_id")
        cart = get_cart(self)
        if book_id:
            quantity = int(self.request.GET.get("quantity"))
            book = Book.objects.get(pk=book_id)
            price = book.price * quantity
            book_in_cart, created = BookInCart.objects.get_or_create(
                cart=cart,
                book=book,
                defaults = {
                    'quantity': quantity,
                    'price': price
            }
        )
            if not created:
                book_in_cart.quantity += quantity
                book_in_cart.price = book_in_cart.quantity *book.price
                book_in_cart.save()
        context = super().get_context_data(**kwargs)
        context['cart'] = cart
        return context