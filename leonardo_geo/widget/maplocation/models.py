# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.widgets.forms import WidgetUpdateForm

from leonardo.module.web.models import Widget


class MapLocationWidgetAdminForm(WidgetUpdateForm):

    def __init__(self, *args, **kwargs):
        super(MapLocationWidgetAdminForm, self).__init__(*args, **kwargs)
        self.fields['map'].widget.attrs.update({'class': 'item-maplocation'})

MAP_CHOICES = (
    ('roadmap', _("road map")),
    ('sattelite', _("satellite")),
    ('hybrid', _("hybrid")),
)


class MapLocationWidget(Widget):
    form = MapLocationWidgetAdminForm
    feincms_item_editor_form = MapLocationWidgetAdminForm

    feincms_item_editor_includes = {
        'head': ['admin/widget/maplocation/init_google.html'],
    }

    title = models.CharField(max_length=255, blank=True, verbose_name=_("title"))
    description = models.TextField(blank=True, verbose_name=_("description"))
    latitude = models.DecimalField(
        verbose_name=_("latitude"), max_digits=18, decimal_places=15)
    longitude = models.DecimalField(
        verbose_name=_("longitude"), max_digits=18, decimal_places=15)
    zoom = models.PositiveSmallIntegerField(max_length=255, verbose_name=_("zoom"), )
    map = models.CharField(
        max_length=255, verbose_name=_("map"), choices=MAP_CHOICES, default="map")

    class Meta:
        abstract = True
        verbose_name = _("map location")
        verbose_name_plural = _('map locations')