from .models import Domains

def get_hostname(request):
    return request.get_host().split(':')[0].lower()

def get_host_name(request):
    hostname = get_hostname(request)
    subdomains = hostname.split('.')[0]
    return Domains.objects.filter(subdomains=subdomains).first()