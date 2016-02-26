# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Rock Music on YouTube Addon by coldkeys
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

addonID = 'plugin.video.ytrock'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLhxCqteIQdB9ifVNBEv_7_BpdiZr_sBSf"
YOUTUBE_CHANNEL_ID_2 = "PLhxCqteIQdB-dbcKmg1rBrvlDtkhvIEsw"
YOUTUBE_CHANNEL_ID_3 = "PLhxCqteIQdB-RuLmvoOp0RCMbVZStvxe2"
YOUTUBE_CHANNEL_ID_4 = "PLhxCqteIQdB_PZaAmHjGwNrsWLWgTjn5j"
YOUTUBE_CHANNEL_ID_5 = "PLhxCqteIQdB9WhOEIK2lw6bAjgMbhfALZ"
YOUTUBE_CHANNEL_ID_6 = "PLhxCqteIQdB_vS3ZiOHsygGMzR-wXNjd4"
YOUTUBE_CHANNEL_ID_7 = "PLhxCqteIQdB9VG5fNGSbgm_c5OIsI6stn"
YOUTUBE_CHANNEL_ID_8 = "PLhxCqteIQdB_uV_fLanB0DbgH3GJM1qtU"
YOUTUBE_CHANNEL_ID_9 = "PLhxCqteIQdB_qxYts7TpOuMsnRH3gzcak"
YOUTUBE_CHANNEL_ID_10 = "PLhxCqteIQdB9jC6eOSEKFW0hNC1E__aft"

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
        title="Greatest rock concerts ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.ytimg.com/vi/3AL73LYo64A/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Rock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.ytimg.com/vi/MN0_Dd4KWJk/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Progressive Rock ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i.ytimg.com/vi/iFWtsT5zRKo/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="David Gilmour",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.ytimg.com/vi/3tZCJeHR800/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Emerson, Lake & Palmer ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.ytimg.com/vi/fLS0Med0s6E/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Led Zeppelin ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.ytimg.com/vi/eQx0mLiiNxI/default.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Pink Floyd",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.ytimg.com/vi/heJT5hMFEs8/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Yes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://i.ytimg.com/vi/GHiVc4IFG7E/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Deep Purple ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://i.ytimg.com/vi/3EOW5HXEGqw/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Moody Blues",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://i.ytimg.com/vi/WwJpYoClb3I/default.jpg",
        folder=True )
run()
