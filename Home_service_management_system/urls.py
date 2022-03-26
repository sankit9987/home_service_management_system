"""Home_service_management_system URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from HSMS import views,serviceviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('login', views.user_login,name="user_login"),
    path('logout', views.user_logout,name="user_logout"),
    path('about-us', views.about_us,name="about_us"),
    path('change-location', views.change_location,name="change_location"),
    path('contact-us', views.contact_us,name="contact_us"),
    path('faq', views.faq,name="faq"),
    path('privacy', views.privacy,name="privacy"),
    path('register', views.register,name="register"),
    path('service-categories', views.service_categories,name="service_categories"),
    path('service-details/<int:id>', views.service_details,name="service_details"),
    path('service-by-category', views.service_by_category,name="service_by_category"),
    path('terms-of-use', views.terms_of_use,name="terms_of_use"),
    path('product/<int:id>', views.product,name="product"),
    path('edit', views.edit,name="edit"),
    path('change-password', views.change_password,name="change_password"),
    path('booking', views.booking,name="booking"),
    path('my-booking', views.my_booking,name="my_booking"),
    path('search', views.search,name="search"),





    path('dashboard', serviceviews.dashboard,name="dashboard"),
    path('view-service', serviceviews.view_service,name="view_service"),
    path('add-service', serviceviews.add_service,name="add_service"),
    path('order', serviceviews.order,name="order"),
    path('delete/<int:id>', serviceviews.service_delete,name="service_delete"),
    path('service/<int:id>', serviceviews.service_view,name="service_view"),
    path('view-order/<int:id>', serviceviews.view_order,name="view_order"),
    path('add-service-provider', serviceviews.add_service_provider,name="add_service_provider"),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
