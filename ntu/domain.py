from .models import PublicKey
from django.conf import settings

def prepare_key():
    return [ x.get("key") for x in PublicKey.objects.filter(is_active=True).values("key")]

def render_key(content):
    with open(settings.AUTHKEY_PATH, "w") as key:
        key.write(content)

def save_key():
    keys = "\n".join(prepare_key())
    render_key(keys)
