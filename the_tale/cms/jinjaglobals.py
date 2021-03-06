# coding: utf-8
from dext.common.utils import jinja2

from the_tale.cms.models import Page
from the_tale.cms.conf import cms_settings

SECTIONS_DICT = dict( (section.id, section) for section in cms_settings.SECTIONS)

@jinja2.jinjaglobal
def get_cms_section_pages(section, *args, **kwargs):
    return Page.objects.filter(section=section, active=True).order_by('order')


@jinja2.jinjaglobal
def get_cms_section_info(section):
    return SECTIONS_DICT[section]
