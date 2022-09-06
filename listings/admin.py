from django.contrib import admin
from . models import Band, Listing, Siege, Users, EmailPassword


class BandAdmin(admin.ModelAdmin):
    """
    Class definissant la personalisation de notre
    interface admin.
    """

    list_display = (
        'id',
        'name',
        'year_formed',
        'genre',
        'biography',
        'official_homepage',
        'active',
        'siege',
    )  # liste les champs que nous voulons sur l'affichage de la liste.

    search_fields = (
        'id',
        'name',
    )  # Configuration du champ de recherche, donc on va chercher avec l'id et le nom

    ordering = (
        'id',
    )  # Tri par defaut du tableau

    # date_hierarchy = 'year_formed'  permet de filtrer par date de façon intuitive
    # Mais bien évidament, l'objet doit etre de type DateField ou DatetimeField

    list_filter = (
        'name',
        'active',
    )  # Liste des champs a partir desquels nous pourons filtrer les entrées


class ListingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'year',
        'type',
        'description',
        'sold',
        'band',
    )

    list_filter = (
        'title',
        'sold',
    )
    # date_hierarchy = 'year'
    ordering = (
        'id',
    )
    search_fields = (
        'id',
        'title',
    )


class SiegeAdmin(admin.ModelAdmin):

    """
    Cette class definit la liste des champs à afficher sur le site admin de Django
    """

    list_display = (
        'id',
        'name',
        'lieu',
        'Creation_Date',
        'genre',
        'number_scoiter',
    )

    date_hierarchy = 'Creation_Date'
    search_fields = (
        'id',
        'name',
    )
    ordering = (
        'id',
    )


class UsersAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'sexe',
        'contry',
        'borned',
        'nationality',
        'job',
        'picture',
    )
    search_fields = ('id',)
    ordering = ('id',)


class EmailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'Email',
        'Password',
        'proprio',
    )
    search_fields = (
        'id',
        'proprio',
    )
    ordering = ('id',)


admin.site.register(EmailPassword, EmailAdmin)
admin.site.register(Band, BandAdmin)    # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Listing, ListingAdmin)
admin.site.register(Siege, SiegeAdmin)
admin.site.register(Users, UsersAdmin)