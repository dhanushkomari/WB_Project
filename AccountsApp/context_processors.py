from App.models import Restaurant,Bot   
from AccountsApp.models import CustomUser as User


def rest_details(request):
    try:
        cp_bots = Bot.objects.filter(rest = request.user.rest)
    except:
        cp_bots = []
    return {'cp_bots': cp_bots}