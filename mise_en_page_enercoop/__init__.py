# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Mise_en_page_Enercoop
                                 A QGIS plugin
 Un plugin permettant de faire des sorties de mise en page automatique
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-04-26
        copyright            : (C) 2023 by Jumeau-Mousset Lucas
        email                : lucas.jumeau-mousset@enercoop.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Jumeau-Mousset Lucas'
__date__ = '2023-04-26'
__copyright__ = '(C) 2023 by Jumeau-Mousset Lucas'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Mise_en_page_Enercoop class from file Mise_en_page_Enercoop.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Mise_en_page_Enercoop import Mise_en_page_EnercoopPlugin
    return Mise_en_page_EnercoopPlugin()
