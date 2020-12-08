from .models import SocialNetwork

def ctx_dict(request):

    redes_sociales = SocialNetwork.objects.all()

    ctx = {'redes_sociales':redes_sociales}

    return ctx