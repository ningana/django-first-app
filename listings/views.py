import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from . models import Band, Listing, Siege, Users
from . forms import UserForm, ContactUsForm, BandForm, ListingForm, Emailpassword


def band_list(request):

    band = Band.objects.all()
    return render(request, "listings/band_list.html", {"band":band})


def band_detail(request, id):

    """
    On essaie, s'il ya d'erreur, on affiche l'ereur garce à Http404, que nous pouvons également personnalisé
    """
    try:
        band = Band.objects.get(id=id)
        return render(request, 'listings/band_details.html', {"band": band})
    except Band.DoesNotExist:
        raise Http404("this \"id\" doesn't exist in database ... Please, retry with a valid one")


def about_us(request):
    return render(request, "listings/about_us.html")


def email_sent(request):
    return render(request, "listings/email_sent.html")


def contact_us(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            """
            Si c'est valide, On envoie un mail"""
            print("Le formulaire est valide, felicitation")
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
                )
            """
            Nous recuperons les valeurs avec forms.Cleaned_data pour envoyer des mails
            ou faire des actions ...
            Ex : name = form.cleaned_data['name'] nous permetra de recuperer le nom"""
        return redirect('/Email_sent')     # rafraichissement de la page vers Email_sent, page de confirmation
        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        form = ContactUsForm()
    return render(request, "listings/contact.html", {'form':form})


def listings(request):
    List = Listing.objects.all()
    return render(request, "listings/listings.html", {"List":List})


def siege(request):

    """
    Cette fonction, cette vue, renvoi la liste de tous les sièges
    au gabarit, ou à la page html siege.html
    """
    sieg = Siege.objects.all()
    return render(request, "listings/siege.html", {"siege":sieg})


def band_create(request):

    """
    S'il s'agit d'une demande GET :
    Il doit s'agir de la première requête sur cette page et l'utilisateur s'attend à voir un formulaire vierge, prêt à
    être rempli. Nous créons donc une nouvelle instance vide du formulaire et nous la stockons dans une variable
    « form ».
    S'il s'agit d'une demande POST :
    Il ne s'agit pas de la première demande, mais d'une demande ultérieure à cette page, accompagnée de certaines
    valeurs de formulaire que l'utilisateur aura soumises. Nous créons donc une instance du formulaire et nous la
    remplissons avec les valeurs envoyées dans la requête POST. C’est stocké dans une variable « form ».
    Si la validation du formulaire se déroule avec succès :
    nous effectuons l'action, qu'il s'agisse d'envoyer un e-mail, de créer un objet ou de toute autre action.
    Nous redirigeons l'utilisateur vers une autre vue, peut-être une page de confirmation ou une autre page qui indique
    que l'action a réussi. Nous arrêtons d'exécuter cette fonction de vue à ce stade. Cependant...
    Si la validation du formulaire n'a PAS réussi :
    Le processus de validation a maintenant ajouté des messages d'erreur dans les champs concernés.
    Nous autorisons l'exécution de cette vue pour continuer à l'étape suivante ci-dessous.
    """
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid:
            band=form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, "listings/create_band.html", {'form':form})


def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/listings")
    else:
        form = ListingForm()
    return render(request, "listings/create_listing.html", {"form":form})


def listing_detail(request, id):
    """
    Cette class fournit un détail sur une annonce
    """
    try:
        listing = Listing.objects.get(id=id)
        return render(request, "listings/listing_detail.html", context={"listing":listing})
    except Listing.DoesNotExist:
        raise Http404("this \"id\" doesn't exist in database ... Please, retry with a valid one")


def connexion2(request):
    if request.method == 'POST':
        form = Emailpassword(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/Email_sent")
    else:
        form = Emailpassword()
    return render(request, "listings/create_user2.html", {"form":form})


def connexion(request):
    """
    Cette fonction definit et renvoie le formulaire d'enregistrement à un gabarit
    """
    save = False
    if request.method == 'POST':
        """
        SI c'est une requete POST, nous affichons un formulaire deja en cours de travail et
        botons le 2e parametre envoyer au constructeur, request.FILES, qui permet de au serveur de
        reconnaitre un fichier non textuel, car request.POST ne reconnait que des textes"""
        form = UserForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/connexion2')
    else:
        form = UserForm()
    return render(request, "listings/create_user.html", {"form":form})


def See_user(request):
    user = Users.objects.all()
    return render(request, "listings/see_user.html", {"user":user})


@login_required  # decorateur
def home(request):
    """
    Vue de la âge d'acceuil
    """
    jour = datetime.datetime.now()
    date = datetime.date.today()
    return render(request, "listings/home.html", {
        "jour":jour.strftime('%A'),
        "date":date,
        "heure":jour.time()
        })