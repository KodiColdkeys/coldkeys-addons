# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Most Haunted Addon by coldkeys
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

addonID = 'plugin.video.mosthaunted'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLZE_drxHBVHrzRh96m-1pe8GrRYfcGS6w"
YOUTUBE_CHANNEL_ID_2 = "PLZE_drxHBVHrNiwfDIB_GmdsxLb5O97d_"
YOUTUBE_CHANNEL_ID_3 = "PLZE_drxHBVHoMkk9pZiPtdj3gJQHN1Dzf"
YOUTUBE_CHANNEL_ID_4 = "PLZE_drxHBVHrt_1wf3F1r9sQitzndjboN"
YOUTUBE_CHANNEL_ID_5 = "PLq-ap_BfvXn8UcrNKkrpCfCuNvrfMaJE1"
YOUTUBE_CHANNEL_ID_6 = "PLq-ap_BfvXn8cvRqg9xTOEwminXpZLa0O"
YOUTUBE_CHANNEL_ID_7 = "PLq-ap_BfvXn-bfXXWQZxrEoVtMR1cRDRT"
YOUTUBE_CHANNEL_ID_8 = "PLq-ap_BfvXn_Xt_53bn9dKoRhxNDycY6y"
YOUTUBE_CHANNEL_ID_9 = "PL67gu3YR5V8VySnFWcNxukylY57AmI_zh"
YOUTUBE_CHANNEL_ID_10 = "PL9PCUr0Stw6-EOhDeUvvj-6nH6ouPdYJl"
YOUTUBE_CHANNEL_ID_11 = "PLWEJFP6S9CF2c3F3-Ne3lo4fMVIav5LJP"
YOUTUBE_CHANNEL_ID_12 = "PL9PCUr0Stw6-EOhDeUvvj-6nH6ouPdYJl"
YOUTUBE_CHANNEL_ID_13 = "PLurs-HetJcxlfdOVEfoEYt9FhUEqFrolk"
YOUTUBE_CHANNEL_ID_14 = "PL3CD837F7930EF545"
YOUTUBE_CHANNEL_ID_15 = "PLxdHf9vy34LkaY7xrmvGviMkH4bLoDwh-"
YOUTUBE_CHANNEL_ID_16 = "UCLl5DuQifCYReW0b5IomM5w"

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
        title="Seasons 1 -3",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Seasons 4 - 6",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Seasons 7 - 9",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Seasons 10 - 12",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Season 13",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Season 14",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Season 15 - The Live Series",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="special://home/addons/plugin.video.mosthaunted/resources/live.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Season 16",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Season 17",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Most Haunted Live",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="special://home/addons/plugin.video.mosthaunted/resources/live.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Most Haunted Unseen",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="special://home/addons/plugin.video.mosthaunted/resources/unseen.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Best of Most Haunted Live",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="special://home/addons/plugin.video.mosthaunted/resources/live.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Most Haunted Live The Search for Evil 2009",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="special://home/addons/plugin.video.mosthaunted/resources/live.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Most Haunted Live - USA - Gettysburg",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="special://home/addons/plugin.video.mosthaunted/resources/live.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="NEW Most Haunted S1 2014",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="special://home/addons/plugin.video.mosthaunted/resources/Most_Haunted.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Most Haunted Videos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="special://home/addons/plugin.video.mosthaunted/resources/Most_Haunted.jpg",
        folder=True )
run()
