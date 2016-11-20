# -*- coding: utf-8 -*-
#------------------------------------------------------------
# ChuckleVision Addon by coldkeys
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: coldkeys
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.chucklevision'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLe4z01xQs9YvbMPo-td5Z53HKQW8UFCmn"
YOUTUBE_CHANNEL_ID_2 = "PLNJZf85okxOC4JxP0mKuYIt2PepD_UyKK"
YOUTUBE_CHANNEL_ID_3 = "PLNJZf85okxODYAuFq_OFhvWedRkZA68Wg"
YOUTUBE_CHANNEL_ID_4 = "PLlGFVAkUT61aLJ2_j_LsuP7V9WMpg1s9R"
YOUTUBE_CHANNEL_ID_5 = "PLlGFVAkUT61aOuckao78gYhEDNCYrI79B"
YOUTUBE_CHANNEL_ID_6 = "PLlGFVAkUT61bABMJY9N-xieh1bfrDos7N"
YOUTUBE_CHANNEL_ID_7 = "PL4DCC69EDFFADE18C"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="All Episodes of ChuckleVision",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://i.ytimg.com/vi/v3thQ3xv10s/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ChuckleVision Series 1 (1987)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.ytimg.com/vi/VyCcxNXY_tY/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ChuckleVision Series 2 (1988-1989)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://i1.ytimg.com/vi/dqMQKtzqw_Y/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ChuckleVision Series 3-10",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://i.ytimg.com/vi/a0veX8yKi5A/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ChuckleVision Series 11-19",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.ytimg.com/vi/LGZSW8wZCeM/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ChuckleVision Series 20-21",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://i1.ytimg.com/vi/aIJ2S9UxxOs/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ChuckleVision: The Ultimate Soundtrack",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.ytimg.com/vi/CpQO_PDLPug/hqdefault.jpg",
        folder=True )
run()
