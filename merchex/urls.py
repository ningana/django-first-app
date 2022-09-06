
import authentication.views
import listings.views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # Chemin vers le site d'administration de Django
    path('bands/', listings.views.band_list, name='band-list'),  # Chemin vers une vue non détaillée
    # Ici on precise un id pour passer  du bands/ au bands/id/ et le name est comme le nom de la vue
    path('bands/<int:id>/', listings.views.band_detail, name='band-detail'),
    path('bands/add/', listings.views.band_create, name="band-create"),
    path("about_us/", listings.views.about_us),
    path("formulaire/", listings.views.contact_us, name="contact"),
    path("listings/", listings.views.listings, name='listing'),
    path("listings/<int:id>/", listings.views.listing_detail, name="listing-detail"),
    path("listings/add/", listings.views.create_listing, name="create-listing"),
    path("Email_sent/", listings.views.email_sent),
    path("connexion/", listings.views.connexion, name="connexion"),
    path("connexion2/", listings.views.connexion2, name="connexion2"),
    # Ici, je difinit un chemin vide, cla sera la page d'acceil de mon sit
    path("home/", listings.views.home, name="home"),
    path("See_user/", listings.views.See_user),
    path('', authentication.views.login_page, name='login'),
    path("logout/", authentication.views.logout_page, name="logout"),
    path("signup/", authentication.views.signup, name="signup"),
    path("signuped/<str:username>/", authentication.views.signuped, name="signuped"),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)