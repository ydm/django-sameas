# -*- coding: utf-8-unix -*-

#
# This file is part of Django-SameAs.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2013 by 4web.bg
#

from __future__ import unicode_literals
from django.template import (Context, Template,)
from django.template.loader import render_to_string
from django.test import TestCase


class SameAsTagTest(TestCase):
    def _render_to_str(self, template_string, context_dict=None):
        tpl = Template(template_string)
        return tpl.render(Context(context_dict or {}))

    def test_flat(self):
        """
        """
        inp = '{% load sameastags %}'\
              '{% block test1 %}value1{% endblock %} '\
              '{% block test2 %}value2{% endblock %} '\
              '{% block test3 %}value3{% endblock %} '\
              '{% sameas test3 %} '\
              '{% sameas test2 %} '\
              '{% sameas test1 %}'
        exp = "value1 value2 value3 value3 value2 value1"
        act = self._render_to_str(inp)
        self.assertEqual(exp, act)

    def test_flat_vars(self):
        inp = '{% load sameastags %}'\
              '{% block test1 %}{{ key1 }}{% endblock %} '\
              '{% block test2 %}{{ key2 }}{% endblock %} '\
              '{% block test3 %}{{ key3 }}{% endblock %} '\
              '{% sameas test3 %} '\
              '{% sameas test2 %} '\
              '{% sameas test1 %}'
        ctx = {'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}
        exp = "value1 value2 value3 value3 value2 value1"
        act = self._render_to_str(inp, ctx)
        self.assertEqual(exp, act)

    def test_inheritance(self):
        exp = '\n'.join(['derived, base'] * 2)
        act = render_to_string('sameas/test/derived.html').strip()
        self.assertEqual(exp, act)
