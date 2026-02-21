# apps/site_settings/apps.py
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SiteSettingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.site_settings"           # ← খুব জরুরি! পুরো dotted path দিতে হবে

    verbose_name = _("Site Settings")                 # ← শুধু একটা স্পেস → হেডার অদৃশ্য/খালি হবে
    # অথবা verbose_name = ""             # পুরো খালি
    # অথবা verbose_name = _("Site Settings")  # যদি চাও এই নাম দেখাক (সুন্দর করে)