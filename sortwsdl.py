#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import logging
import os
from lxml import etree


def obtenerClaveOrdenacion(node, attr=None):
    """Devuelve la clave de ordenación de un nodo xml
    utilizando la etiqueta y los atributos
    """
    if attr is None:
        return '%s' % node.tag + ':'.join([node.get(attr)
                                        for attr in sorted(node.attrib)])
    if attr in node.attrib:
        return '%s:%s' % (node.tag, node.get(attr))
    return '%s' % node.tag


def ordenarNodosHijo(node, attr=None):
    """ Ordena a los hijos según la etiqueta y el atributo dado.
    Si attr es None, ordena a partir de todos los atributos"""
    if not isinstance(node.tag, str):  # PYTHON 2: Usar basestring en lugar de esto
        # No es un TAG, es un comentario o DATA, no necesita ordenación
        return
    # Ordenamos los hijos a partir de los atributos
    node[:] = sorted(node, key=lambda child: obtenerClaveOrdenacion(child, attr))
    # Y llamamos recursivamente
    for child in node:
        ordenarNodosHijo(child, attr)


def ordenarXML(xmlSinOrdenar, xmlOrdenado, attr=None):
    """Ordena uh xml y lo graba ordenado con el nombre recibido"""
    tree = etree.parse(xmlSinOrdenar)
    root = tree.getroot()
    ordenarNodosHijo(root, attr)

    sorted_unicode = etree.tostring(root,
                                    pretty_print=True,
                                    encoding='unicode')
    with open(xmlOrdenado, 'w') as output_fp:
        output_fp.write('%s' % sorted_unicode)
        logging.info('written sorted file %s', sorted_unicode)

for root, dirs, files in os.walk("."):
    for file in files:
        if (file.find(".wsdl")!=-1 and file.find(".sorted")==-1):
            print('Ordenando [' + root + '\\' + file + '] en [' + root + '\\' + file+'.sorted]')
            ordenarXML (root + '\\' + file, root + '\\' + file+'.sorted')
        
        
