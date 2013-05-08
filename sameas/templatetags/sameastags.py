# -*- coding: utf-8-unix -*-

from __future__ import unicode_literals
from django import template
from django.template.loader_tags import (BlockNode, do_block)


register = template.Library()


_block_key = lambda b: '__sameas_{}__'.format(b)


class SameNode(template.Node):
    def __init__(self, block_name):
        self.block_name = block_name

    def render(self, context):
        return context[_block_key(self.block_name)]


@register.tag('sameas')
def do_sameas(parser, token):
    try:
        tag, block = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "{} tag requires a single argument" .format(
                token.split_contents()[0]
            )
        )
    else:
        return(SameNode(block))


# ydm: I have to override the default `block` tag handler since
# there's no other way (as far as I know) to access block's rendered
# content
class BlockNodeProxy(BlockNode):
    def __init__(self, name, nodelist, parent=None):
        super(BlockNodeProxy, self).__init__(name, nodelist)

    def render(self, context):
        result = super(BlockNodeProxy, self).render(context)
        context[_block_key(self.name)] = result
        return result


@register.tag('block')
def modified_do_block(parser, token):
    node = do_block(parser, token)
    return BlockNodeProxy(node.name, node.nodelist)
