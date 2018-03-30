# -*- coding: utf-8 -*-

from pkg_resources import get_distribution

__distribution__ = get_distribution(__package__)
__version__ = __distribution__.version
__title__ = __distribution__.project_name
