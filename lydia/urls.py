"""lydia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('partner/', include('partner.urls')),
    path('product-category/', include('product_category.urls')),
    path('product/', include('product.urls')),
    path('purchase/', include('purchase.urls')),
    path('partner-type/', include('partner_type.urls')),
    path('purchase-opportunity/', include('purchase_opportunity.urls')),
    path('payment/', include('payment.urls')),
    path('payment-mode/', include('payment_mode.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
