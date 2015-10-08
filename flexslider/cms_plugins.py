from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from flexslider import models
from django.utils.translation import ugettext as _


class FlexSlider(CMSPluginBase):
    model = CMSPlugin  # Model where data about this plugin is saved
    module = _("FlexSlider")
    name = _("FlexSlider Plugin")  # Name of the plugin
    render_template = "flexslider/flexslider.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        context['slides'] = models.Slide.objects.all
        return context

plugin_pool.register_plugin(FlexSlider)  # register the plugin

