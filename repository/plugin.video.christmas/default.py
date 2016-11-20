# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Christmas Addon by coldkeys
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

addonID = 'plugin.video.christmas'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PL152bjytsMC42yqZ2FV8CO7g2ngw54lCZ"
YOUTUBE_CHANNEL_ID_2 = "PL3cZQ6cMxQNgaCVxnDIGA72cekAHt71_0"
YOUTUBE_CHANNEL_ID_3 = "PL152bjytsMC4E9rcMWkAt9lwGDEF69O1K"
YOUTUBE_CHANNEL_ID_4 = "PLxvodScTx2Rst1LDYAZAE_7qBqBFXxhAA"
YOUTUBE_CHANNEL_ID_5 = "PL_34_m4eTlaNf6TSaM9IfLd13R1lKaoYd"
YOUTUBE_CHANNEL_ID_6 = "PLWN1djuBEKCnEDqRgvMKKs8qnmiIOck2L"
YOUTUBE_CHANNEL_ID_7 = "PLgj8F6OQTiK-aJXGXuxWYX9XGy7JaDcbU"
YOUTUBE_CHANNEL_ID_8 = "PLMATWUx3t7L8ko6w_qjgByofm8PQsCChp"
YOUTUBE_CHANNEL_ID_9 = "PL5A20A6534F2F8200"
YOUTUBE_CHANNEL_ID_10 = "PLCf3XRPFys5pa2urPKN3t7P4U_R2npMuA"
YOUTUBE_CHANNEL_ID_11 = "PL1wrsEJEvZjZmC0xYIeJxK_NYzN7mN-WD"
YOUTUBE_CHANNEL_ID_12 = "PLta2NUW1sQa9O9BRzJgFrlcj4WvNYz2uk"
YOUTUBE_CHANNEL_ID_13 = "PL36F3392C222A6A2D"
YOUTUBE_CHANNEL_ID_14 = "PL42rZ9F2TCkkz-zq24rRSFWaj-f0RXBWl"
YOUTUBE_CHANNEL_ID_15 = "PL4uUU2x5ZgR32hLWMaVhr7DwuEyjLQIeb"
YOUTUBE_CHANNEL_ID_16 = "PLfpeViGO0oEXyTleYuOwFxl7ic6_FX9dk"
YOUTUBE_CHANNEL_ID_17 = "PL7D8B9DE8F2B41BAD"
YOUTUBE_CHANNEL_ID_18 = "PL3cZQ6cMxQNgcTG6Yol_xo5jm0TUh2QnS"
YOUTUBE_CHANNEL_ID_19 = "PL8D4Iby0Bmm8OmcAYdZxiDl5igLVwFQ1J"
YOUTUBE_CHANNEL_ID_20 = "PL7F9HNhSDxR1-r-uHKSdc0NXh40hKa0ij"

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
        title="Christmas Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://i1.ytimg.com/vi/06zc5JllZC0/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christmas Jazz Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://i.ytimg.com/vi/Q8ecxOzSvh8/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CHRISTMAS Music Compilations (incl.Log Fires etc)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i.ytimg.com/vi/6oW44aeioio/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="VEVO Most Popular Christmas Hits This Week",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://i1.ytimg.com/vi/06zc5JllZC0/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NOW That's What I Call Christmas 2015",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.ytimg.com/vi/J4Hdky2bnB8/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ultimate Christmas Playlist",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://i.ytimg.com/vi/Ooc5eJc5SHA/hqdefault.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Christmas RnB Soul and Contemporary Songs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.ytimg.com/vi/Aj2huwHjj-k/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Motown Christmas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://i.ytimg.com/vi/-EaUlaz1jSM/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ella Fitzgerald A Swinging Christmas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://i.ytimg.com/vi/oaFKnf69IH4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Glee - The Christmas Album",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://i.ytimg.com/vi/kHUv4cDaCh8/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kids Christmas Songs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://i1.ytimg.com/vi/hega-GxyW6o/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="London Symphony Orchestra - Christmas Classics",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://i.ytimg.com/vi/POVjeuef0RY/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christmas Carols by King's College Cambridge",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://i.ytimg.com/vi/wZLqzxxxnDc/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Christmas Music (40's- 60's).",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://i.ytimg.com/vi/iunknhlxRf4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Country Christmas Songs 2016",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://i.ytimg.com/vi/H7eW561EGQc/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christmas Instrumental",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="http://i.ytimg.com/vi/6PtKPSZ73JQ/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Reggae Christmas Songs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://i.ytimg.com/vi/-laDVEbCaNo/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christmas Party Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://i.ytimg.com/vi/QT03SvRpwWU/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christmas Time, Karaoke and Wine",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://i.ytimg.com/vi/x_7r5yfR-84/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christmas Themed Cakes, Cupcakes and Treats",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://i1.ytimg.com/vi/YdySDf1u1NI/hqdefault.jpg",
        folder=True )
run()
