# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from flask_app.views import insert_recipe,search_recipe,search_prices,home
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('flask_app.urls')),
    #path('', home_view, name='home'),
    path('', home, name='home'),  # Add this line

    path('insert_recipe/', insert_recipe, name='insert_recipe'),  # Add this line
    path('search/', search_recipe, name='search_recipe'),
    path('search/search_prices/<int:recipe_id>/', search_prices, name='search_prices'),    # Add this line

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)