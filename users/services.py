from DRFprogect.settings import STRIPE_API_KEY
import stripe

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product_name):
    """Функция создания продукта в Stripe."""
    product = stripe.Product.create(name=product_name)
    return product['id']


def create_stripe_price(amount, product_id):
    """Функция для создания цены в Stripe."""
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product=product_id
    )
    return stripe_price['id']


def create_stripe_session(price):
    """Функция для создания сессии на оплату в Stripe."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
