# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Fishing videos on YouTube by coldkeys
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

addonID = 'plugin.video.fishingtube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PL152bjytsMC5IAot7hLowOewo2Dioib5k"
YOUTUBE_CHANNEL_ID_2 = "PL152bjytsMC64BKWyBXMrPZEXKD_vtJos"
YOUTUBE_CHANNEL_ID_3 = "PL152bjytsMC5sDSspMKm3xT99gzw79oSo"
YOUTUBE_CHANNEL_ID_4 = "PL152bjytsMC5QMDCc-unKiA6KS4BSA_Np"
YOUTUBE_CHANNEL_ID_5 = "PL152bjytsMC5qVKp6tSl8y34FYh_jjBPG"
YOUTUBE_CHANNEL_ID_6 = "PL152bjytsMC6KqgV0ZPmtC80paIWBVamO"
YOUTUBE_CHANNEL_ID_7 = "UCtElDjbNvNG9UkhC-T54HJA"
YOUTUBE_CHANNEL_ID_8 = "PL152bjytsMC67WcR2MUh2uwpAv2CXWOQi"
YOUTUBE_CHANNEL_ID_9 = "PL152bjytsMC7hs0a9cA-dbPclJtcnKqQY"
YOUTUBE_CHANNEL_ID_10 = "UCBDT-Kl4nHgEvpwYfLb315w"
YOUTUBE_CHANNEL_ID_11 = "PL152bjytsMC4ZTchUbULfLu_lyN_kMfXx"
YOUTUBE_CHANNEL_ID_12 = "PL152bjytsMC5JDSOCLE2mx7bykXARhO4f"
YOUTUBE_CHANNEL_ID_13 = "PL152bjytsMC4DhX_loiwTvit3nTd1138I"
YOUTUBE_CHANNEL_ID_14 = "PL152bjytsMC4JXAqLdA4L-6jROXdVVuin"
YOUTUBE_CHANNEL_ID_15 = "PL152bjytsMC442b8eCTm2SC-EZyNNtJCo"
YOUTUBE_CHANNEL_ID_16 = "PL152bjytsMC5OT7Lae50JQxYGlAPxFNWz"
YOUTUBE_CHANNEL_ID_17 = "PL152bjytsMC7iBdA896I_cpbNBKRJVvUg"
YOUTUBE_CHANNEL_ID_18 = "UC16NCfnoaG7rm60e9pl89fw"
YOUTUBE_CHANNEL_ID_19 = "PL152bjytsMC5Wg7vcSqJy6MvH9LQnok7C"
YOUTUBE_CHANNEL_ID_20 = "PL152bjytsMC7tU7WCuHcn9ZzlDpsY3IsP"
YOUTUBE_CHANNEL_ID_21 = "PL152bjytsMC5MRutIMrbBCFcc5EGAre0t"
YOUTUBE_CHANNEL_ID_22 = "UC8oBI0G2b4ooFWhI2LcHwLA"
YOUTUBE_CHANNEL_ID_23 = "UCaULe1cc4jCQ6ZzUrDY81Sg"
YOUTUBE_CHANNEL_ID_24 = "UCGrzmEwDXba2-x-YUPPpPVw"
YOUTUBE_CHANNEL_ID_25 = "UCt6iqDb8Pcza_A_UW5XMFyg"
YOUTUBE_CHANNEL_ID_26 = "UC2Jn89il6-leUA3NygCgnfg"
YOUTUBE_CHANNEL_ID_27 = "UCQUFq9cNM0Zm6boX0dRhuLQ"
YOUTUBE_CHANNEL_ID_28 = "UCHsVmxfbTN79r80FC9qeOYQ"
YOUTUBE_CHANNEL_ID_29 = "UCE0nF0ay4EP5jXIOiFaPy2Q"
YOUTUBE_CHANNEL_ID_30 = "PL152bjytsMC4QUQR3YuuLT2ctnHK61BaQ"
YOUTUBE_CHANNEL_ID_31 = "UCk2DJldSE7hhQTU8rjNHeYw"
YOUTUBE_CHANNEL_ID_32 = "PL152bjytsMC5IK0pAmAosCCBczD2RaCm7"
YOUTUBE_CHANNEL_ID_33 = "PL152bjytsMC6d20kipk9bNnoq1d3tzfBU"
YOUTUBE_CHANNEL_ID_34 = "PL152bjytsMC72aLxD2li9Fh57ajyJMXzp"
YOUTUBE_CHANNEL_ID_35 = "UCq0lLWU77ZPGbbmIIxW5mdw"
YOUTUBE_CHANNEL_ID_36 = "UC7r0G7BAZrsmkZGEuUGDzSA"
YOUTUBE_CHANNEL_ID_37 = "UCFhnnIKuj0qP4NtVXmoZ5gw"
YOUTUBE_CHANNEL_ID_38 = "PL152bjytsMC7O4En1nsgWVNzzXvHZZcd2"
YOUTUBE_CHANNEL_ID_39 = "UCzTfnC661R3LXu_mS9aRFKA"
YOUTUBE_CHANNEL_ID_40 = "UCUUU29AwqBBdItwah3CfbDQ"
YOUTUBE_CHANNEL_ID_41 = "PL152bjytsMC6aHC2Nday_WqMNR8le3MId"
YOUTUBE_CHANNEL_ID_42 = "UCS_HiqBbUxpOV_8G6vaBgrA"
YOUTUBE_CHANNEL_ID_43 = "UCjHltD9bKOFQ3kI3B32yfWA"
YOUTUBE_CHANNEL_ID_44 = "PL152bjytsMC7_0wJRpUjK1uDs7ysRG0Ss"
YOUTUBE_CHANNEL_ID_45 = "PL152bjytsMC6UZhJsq1Erq9gKuxQfix51"
YOUTUBE_CHANNEL_ID_46 = "PL152bjytsMC5EMB-yTZVeqnGESxtyT1g6"
YOUTUBE_CHANNEL_ID_47 = "PL152bjytsMC5U0Azyvz9CLp_4Cx-xmCuh"
YOUTUBE_CHANNEL_ID_48 = "PL152bjytsMC66c6QZETlkRREvsbZhYKdO"
YOUTUBE_CHANNEL_ID_49 = "PL152bjytsMC7UF5NuryOkRpUMRsoa8rFy"
YOUTUBE_CHANNEL_ID_50 = "PL152bjytsMC4DAdWPEQHLWvnk1INCySKc"


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
        title="*John Wilson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/johnwilson.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Total Fishing S1-3",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/51MCkYkfyML.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Matt Hayes and Mick Brown",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/hayesnbrown.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Go Fishing Online - Tips etc",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-6Fc7i9sNJX8/AAAAAAAAAAI/AAAAAAAAAAA/OZdHvuSC5dw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Carp Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/carp.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Perch, Pike and Zander Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/pike.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Totally Awesome Fishing Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-P2USlMtGNXo/AAAAAAAAAAI/AAAAAAAAAAA/sDV3FPYrotM/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="*Fishing Series",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/fishingseries.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Match Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/matchfishing.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Uncut Angling",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-8Rt7LjDZrtU/AAAAAAAAAAI/AAAAAAAAAAA/-0-9PLOJWXM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Bob Nudd",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/bobnudd.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="*Coarse Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/coarsefishing.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="*Fly Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/flyfishing.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="*Salmon and Trout Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/salmon.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="*Catfish Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/catfish.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*My Life in Angling",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/gonefishing.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Sea Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/seafishing.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fly and Fly Tying (check playlist)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/fly.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Kayak Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/kayak.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Angling Schools and Tools",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/school.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="*Rex Hunt, Robson Green and more",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/rexhunt.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fishing TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-wndEWxwcAL0/AAAAAAAAAAI/AAAAAAAAAAA/wlieH4UtZK0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nash TV Carp Fishing",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/-fGfdBM-7Geg/AAAAAAAAAAI/AAAAAAAAAAA/Nuz-b_Uyn14/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Carp Catcher",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/-hxTxGpsBNv4/AAAAAAAAAAI/AAAAAAAAAAA/5uH4K1tjFmY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lake Fork Guy Fishing TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/-iC53i460Jmc/AAAAAAAAAAI/AAAAAAAAAAA/sl4CD_VhExU/s100-c-k-no-mo/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wired2Fish",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/-WspSpZO5FuY/AAAAAAAAAAI/AAAAAAAAAAA/Kwnz5IDnzoA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Big Bass Master 1",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-J3xORXh6Z00/AAAAAAAAAAI/AAAAAAAAAAA/cFa0xxXu33Y/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Handmade Fisherman",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/-pvK8xiOLKVM/AAAAAAAAAAI/AAAAAAAAAAA/AokqC76ixIo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tackle Fanatics TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://yt3.ggpht.com/-0loPtDk8oSs/AAAAAAAAAAI/AAAAAAAAAAA/a8aAbq1IZ80/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Fishing Britain",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/fishbrit.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The New Fly Fisher TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-_pUgT4JkOG4/AAAAAAAAAAI/AAAAAAAAAAA/GYhMzXNXeWk/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="*Hobie Outdoor Adventures Season 1-4",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://yt3.ggpht.com/-_eGXE9gSO7U/AAAAAAAAAAI/AAAAAAAAAAA/Og6DEhVnDok/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="*Reel Time Florida Sportsman TV Season 1-3",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-DNGLO85zSxU/AAAAAAAAAAI/AAAAAAAAAAA/KVOmq16kPAc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Into the Blue Fishing Season 4-7",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/-EoAfVi8JLtk/AAAAAAAAAAI/AAAAAAAAAAA/NJx4v0Y-ZTM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Addictive Fishing",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/-GVYwA_JBBFg/AAAAAAAAAAI/AAAAAAAAAAA/P3WyjL4FlNU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kayak Fish'n TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-tFqfmM3cJTU/AAAAAAAAAAI/AAAAAAAAAAA/hy9fAGSkXEQ/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Carp Headbangers",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/-L4kFZ8oXJtA/AAAAAAAAAAI/AAAAAAAAAAA/c4E9u7FYLmg/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="*Korda TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-SqfvY_RfBJ8/AAAAAAAAAAI/AAAAAAAAAAA/GsAynsc1PYY/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Ultimate Fishing",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/-QBOAOmaV38E/AAAAAAAAAAI/AAAAAAAAAAA/O5Cfua1lMPg/s100-c-k-no/photo.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Big Fish Channel - YouFish TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-MIFrLQjGvrU/AAAAAAAAAAI/AAAAAAAAAAA/QpgK9gf3MtE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*iFish TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/-XcKIhchIFh0/AAAAAAAAAAI/AAAAAAAAAAA/V0-DBNo_yJU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mark Erdwin's Fishing for Memories",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/-BlRPcSli9AQ/AAAAAAAAAAI/AAAAAAAAAAA/a-0bJMYY38g/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Back of the Landing Net Carp Fishing",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/-61FRiyr8xCc/AAAAAAAAAAI/AAAAAAAAAAA/dlxl5ioLi1k/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Carp Series",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://yt3.ggpht.com/-XPiGjAUyxAs/AAAAAAAAAAI/AAAAAAAAAAA/pN7-DRduPSs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Jet Ski Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/jetski.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="*Fishing the World",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/world.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*A Big Catch",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://yt3.ggpht.com/-x5DsKWR408Q/AAAAAAAAAAI/AAAAAAAAAAA/rBKd0sxiemU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Ice Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/ice.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Spear Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/spear.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*More Fishing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="special://home/addons/plugin.video.fishingtube/resources/morefishing.jpg",
        folder=True )
run()
