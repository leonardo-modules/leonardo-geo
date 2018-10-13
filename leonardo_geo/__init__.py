
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


default_app_config = 'leonardo_geo.Config'

class Default(object):

    optgroup = 'Geolocation'

    apps = [
        'leonardo_geo'
    ]

    js = {
        'js/leaflet.js',
        'js/mapbox.js',
        'js/mapbox-gl.js',
        'js/leaflet-mapbox-gl.js',
    }

    css = [
        'css/leaflet.css',
        'css/mapbox-gl.css',
    ]

    @property
    def widgets(self):
        return [
            'leonardo_geo.models.MapLocationWidget',
        ]

    config = {
        'GOOGLE_MAPS_API_KEY': ('','API key for Google Maps.'),
        'GOOGLE_MAPS_STYLES': ('','Styles for Google Maps.'),
        'LEAFLET_ACCESS_TOKEN': ('', 'Access token for Leaflet maps'),
        'LEAFLET_MAPBOX_STYLES': ('', 'Styles for Leaflet Maps - mapbox'),
    }
    


class Config(AppConfig, Default):
    name = 'leonardo_geo'
    verbose_name = _("Geolocation")

default = Default()
