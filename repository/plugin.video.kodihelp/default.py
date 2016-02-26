# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Kodi Help Addon by coldkeys
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

addonID = 'plugin.video.kodihelp'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCb5DkdbEOBNoOY7RGkGN4pg"
YOUTUBE_CHANNEL_ID_2 = "UCoMOQDEEBECQ81CdojuEqfg"
YOUTUBE_CHANNEL_ID_3 = "UCZuZ4D4WGmyCLlWkgXvqqEg"
YOUTUBE_CHANNEL_ID_4 = "UCuSdObYHdjize3ziP951org"
YOUTUBE_CHANNEL_ID_5 = "UCkuxO4LKCwGUYlWohaL0pyA"
YOUTUBE_CHANNEL_ID_6 = "UC0XB4eRTTYxYeLMpVcIClSQ"
YOUTUBE_CHANNEL_ID_7 = "UC8Vs1m9YmDBQHGMicqzg9OA"
YOUTUBE_CHANNEL_ID_8 = "UCJHVVRzymRUP3hLiCv1ynvg"
YOUTUBE_CHANNEL_ID_9 = "UCWM6C2mZAhTAOVUi3tDWeCw"
YOUTUBE_CHANNEL_ID_10 = "UCJsK7OWTPV5Te0g_mRkllcQ"
YOUTUBE_CHANNEL_ID_11 = "UCr_wSx5sZh5ydPzf7jOS7ZQ"
YOUTUBE_CHANNEL_ID_12 = "UCTcmpCCEk6q0ovCrHANZoUw"
YOUTUBE_CHANNEL_ID_13 = "UCOQVoYzsSlRnDNIBWe2dY4g"
YOUTUBE_CHANNEL_ID_14 = "UCUY5BYXIaZoa4-HclwnNWDA"
YOUTUBE_CHANNEL_ID_15 = "UClL8FITZIKeSf1YzGOMMd-g"
YOUTUBE_CHANNEL_ID_16 = "UC8IdNL6nD0UVJ82RzfMwjWQ"
YOUTUBE_CHANNEL_ID_17 = "UCgRxR05Lmy_KVVW5I0PcTDA"
YOUTUBE_CHANNEL_ID_18 = "UC5tUi0nhIWLJvO_oWxuzekw"
YOUTUBE_CHANNEL_ID_19 = "UCfM9Y0sFwEJWP8sKUHceFTg"
YOUTUBE_CHANNEL_ID_20 = "UC-jBkGiRokRd-B2ylx1VqJQ"

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
        title="Husham Memar",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-7MqMXmT3DR8/AAAAAAAAAAI/AAAAAAAAAAA/bfs3l0wg6u4/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tech Timeruuu",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-xrpSGZutUms/AAAAAAAAAAI/AAAAAAAAAAA/WoCkFC1pt8Q/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JoeNobody010101",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-yyi7bfBAFdM/AAAAAAAAAAI/AAAAAAAAAAA/YZtjGJ9XsYo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Solo Man",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-YUHW44PfRLU/AAAAAAAAAAI/AAAAAAAAAAA/TMK9xizbGJU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SpoonFed Productions",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-AEmubMpBV6I/AAAAAAAAAAI/AAAAAAAAAAA/bzycEE8Y5qA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="XBMC - KODI Help",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-6mLNnnG4sKE/AAAAAAAAAAI/AAAAAAAAAAA/78_ra-ZQpnI/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Acosta XBMC",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-r8WbLIryyAU/AAAAAAAAAAI/AAAAAAAAAAA/0KWNwqjB8yM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="OneTechGenius XBMC HELPER",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-gz5CkSVvQW0/AAAAAAAAAAI/AAAAAAAAAAA/5tL5WmC4U4w/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="XBMConnect",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-op-ozll4OWI/AAAAAAAAAAI/AAAAAAAAAAA/Hoq_od6Z9MY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="naresh lal",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-Kb9zJh_02NI/AAAAAAAAAAI/AAAAAAAAAAA/QuwbM3wc9vI/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Simply Caz",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-swGWsXGqbbA/AAAAAAAAAAI/AAAAAAAAAAA/GnwcHOLcYfo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="KRAZ inabox",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-cRThFqx7f4s/AAAAAAAAAAI/AAAAAAAAAAA/gEQAOW5hXPQ/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Newtech Evolution",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-Rn4z3ys8mIs/AAAAAAAAAAI/AAAAAAAAAAA/yPQtOUwwQKw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dimitrology",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-gc8RvvduE-E/AAAAAAAAAAI/AAAAAAAAAAA/7YIGzK1cPME/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Daz B Tutorials",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-bAbB2J-DS0s/AAAAAAAAAAI/AAAAAAAAAAA/f6Wgc535wA4/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Soulless Builds",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-T5R891izvqc/AAAAAAAAAAI/AAAAAAAAAAA/yj2lp7_d1rs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Touchtone",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-PZf6tIaQqC4/AAAAAAAAAAI/AAAAAAAAAAA/LWrigWjcmcE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="All Things Tech",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-FWrRH5t7WTQ/AAAAAAAAAAI/AAAAAAAAAAA/YKGxO8Ay_Rk/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="KodiMaster",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-2QIT9by2lOc/AAAAAAAAAAI/AAAAAAAAAAA/VYh0VnvwnzA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DaButcher Builds",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-Rq5_cE4Bab0/AAAAAAAAAAI/AAAAAAAAAAA/58sCN8EcKcA/s100-c-k-no/photo.jpg",
        folder=True )
run()
