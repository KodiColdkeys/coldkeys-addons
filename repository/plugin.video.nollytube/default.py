# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Nollywood videos on YouTube by coldkeys
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

addonID = 'plugin.video.nollytube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLD0Gh4WFSWRVlTonp_9Xd_W3CWQIw5nvh"
YOUTUBE_CHANNEL_ID_2 = "PLD0Gh4WFSWRX5gZ8C_TMZfAgvrSTw_0JA"
YOUTUBE_CHANNEL_ID_3 = "PLD0Gh4WFSWRXv_QKt1b8T-K0xLJoSe2Zi"
YOUTUBE_CHANNEL_ID_4 = "PL2gJz0Y33jNylRulhObO9Ebxivc8A0AjN"
YOUTUBE_CHANNEL_ID_5 = "PLD0Gh4WFSWRX5gZ8C_TMZfAgvrSTw_0JA"
YOUTUBE_CHANNEL_ID_6 = "PL2gJz0Y33jNw7fxltv09j2AWrjdFSbWIR"
YOUTUBE_CHANNEL_ID_7 = "PL2gJz0Y33jNw6i2wOS0IpnNUc2vCtqcmN"
YOUTUBE_CHANNEL_ID_8 = "PL2gJz0Y33jNzVGVTouWsyRvmJmMRraW-C"
YOUTUBE_CHANNEL_ID_9 = "PL2gJz0Y33jNwoCMh8oq2f4j0EJP6BJNwd"
YOUTUBE_CHANNEL_ID_10 = "PL2gJz0Y33jNwJ7suyOIzt4dwSOTQ_dBEF"
YOUTUBE_CHANNEL_ID_11 = "PLIS2cJG94zffCtXlOqHjPLjHFei1p6U-S"
YOUTUBE_CHANNEL_ID_12 = "UCm6NRZvIcYwpj79CIa1Lj9g"
YOUTUBE_CHANNEL_ID_13 = "PLbjbnNeI30wgPXUiN7PErRZQsGqqJbOIl"
YOUTUBE_CHANNEL_ID_14 = "PLbjbnNeI30wik0Ov2IfORTHek4Em_bWQ5"
YOUTUBE_CHANNEL_ID_15 = "PLbjbnNeI30wh_1BuDkMluXW9RYpDDtiOm"
YOUTUBE_CHANNEL_ID_16 = "PLbjbnNeI30wieyIthYDFduOKTxyG_gpQ2"
YOUTUBE_CHANNEL_ID_17 = "PL3yqRRVpedzWzYa_2wiGrxTG3QCfoWpiJ"
YOUTUBE_CHANNEL_ID_18 = "PL3yqRRVpedzWUsD5EFS1_gljtUoIXCNgo"
YOUTUBE_CHANNEL_ID_19 = "PL3yqRRVpedzWXcyyUoEwRqLPNyOvxD05E"
YOUTUBE_CHANNEL_ID_20 = "PL3yqRRVpedzVrC36vqunF_KKOSTWNiirH"
YOUTUBE_CHANNEL_ID_21 = "PL3yqRRVpedzWQrXGO7UNrwqTWTy9qPB4u"
YOUTUBE_CHANNEL_ID_22 = "PL3yqRRVpedzWdHH3oONLqLiourFkBRTuP"
YOUTUBE_CHANNEL_ID_23 = "PL3yqRRVpedzVhq0woasscvxA4DumOloau"
YOUTUBE_CHANNEL_ID_24 = "PLpyD34pHIy8kxlDxSnPpG59X_R-QWFN7i"
YOUTUBE_CHANNEL_ID_25 = "PLpyD34pHIy8mn2kONMZPNiOqvkL0GK1Uk"
YOUTUBE_CHANNEL_ID_26 = "PLjip-PCXtl0X5KNLPqggxtA7AOpu8v69L"
YOUTUBE_CHANNEL_ID_27 = "PLjip-PCXtl0VL01oWCB7pOV2nbWXa_l5e"
YOUTUBE_CHANNEL_ID_28 = "PLjip-PCXtl0UEigfNJbRI7RZSpqyuG4mo"
YOUTUBE_CHANNEL_ID_29 = "PL7C5FD4AF14CAFA73"
YOUTUBE_CHANNEL_ID_30 = "PLjip-PCXtl0V6aOVyEoArxHiSK_VgXs8y"
YOUTUBE_CHANNEL_ID_31 = "PLjip-PCXtl0VouLK2OmGoVrZZgZpPW5sr"
YOUTUBE_CHANNEL_ID_32 = "PLjip-PCXtl0V1yjx0InnyCkMPZW6PhS3U"
YOUTUBE_CHANNEL_ID_33 = "PLjip-PCXtl0Uu8s0vhhupV5c8w2uYZE7z"
YOUTUBE_CHANNEL_ID_34 = "PLe1FlWw9yfSID4ppIbsZ_sFrLa0oyfmj1"
YOUTUBE_CHANNEL_ID_35 = "PLe1FlWw9yfSJrA_5bb4UVgmvQX2EzWZzf"
YOUTUBE_CHANNEL_ID_36 = "PLe1FlWw9yfSLI6W0lOtXy0rSS0t-TS038"
YOUTUBE_CHANNEL_ID_37 = "PLe1FlWw9yfSKMZPJLM9TXZNeS5BWLxis_"
YOUTUBE_CHANNEL_ID_38 = "PLe1FlWw9yfSIz-nRu9K_3pEC-o4ge0CG_"
YOUTUBE_CHANNEL_ID_39 = "UCOThq4XOYOPjZNOdbaAELAA"
YOUTUBE_CHANNEL_ID_40 = "PLe1FlWw9yfSKrrBb395nssf8iay9gLRgq"
YOUTUBE_CHANNEL_ID_41 = "PLe1FlWw9yfSJom9cZtQ2vMIqO-afk5OUy"
YOUTUBE_CHANNEL_ID_42 = "PLe1FlWw9yfSKJ5z8gjpo_9-Sy0FMrKMoW"
YOUTUBE_CHANNEL_ID_43 = "PLe1FlWw9yfSLgmR2O5ayRbHH72Tuq2Wjf"
YOUTUBE_CHANNEL_ID_44 = "PLe1FlWw9yfSLJygbbZkfvq5gsvcBilOES"
YOUTUBE_CHANNEL_ID_45 = "PL8jHYBHzSNEIPSQXWy41L2VMKXnRWVVwp"
YOUTUBE_CHANNEL_ID_46 = "PL8jHYBHzSNEK6Ppp2fsOS6V3mZTGPbmlB"
YOUTUBE_CHANNEL_ID_47 = "PL8jHYBHzSNEJ1Tq9DQ2WdzO19fyIecbBb"
YOUTUBE_CHANNEL_ID_48 = "PL8jHYBHzSNEJMWD72s7cGoBL26BJrYJ5_"
YOUTUBE_CHANNEL_ID_49 = "PL2gJz0Y33jNzesZ5jsfKAV4cs08xsqjfb"
YOUTUBE_CHANNEL_ID_50 = "PL2gJz0Y33jNzBrTDWfCAUE2sSUGCavZZ4"
YOUTUBE_CHANNEL_ID_51 = "UCSH4tR3T3HhpkEL2aBqIy1g"
YOUTUBE_CHANNEL_ID_52 = "UCRpVhC2Mv9B-CIhYXGb0IdA"
YOUTUBE_CHANNEL_ID_53 = "UCoMmHHH65XqnS-nFcGjjbIg"
YOUTUBE_CHANNEL_ID_54 = "UCOU1T_xHxlLe3XGmXNh4PZw"
YOUTUBE_CHANNEL_ID_55 = "UCVS0KpEqeBaPKfwMwLodScQ"
YOUTUBE_CHANNEL_ID_56 = "UCi8vPG6uMxIjoZMhLLX2BkQ"
YOUTUBE_CHANNEL_ID_57 = "UCeW1_lWZFIiMCMqKdSB2Zzw"
YOUTUBE_CHANNEL_ID_58 = "UC-CIIGOdqDf_uAUk50CC_vQ"
YOUTUBE_CHANNEL_ID_59 = "UCBDhfNtm0XVf-nTsJjjecag"
YOUTUBE_CHANNEL_ID_60 = "UC0kUosmFwu4oGu-Q2PxKjsQ"


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
        title="Very Interesting Family Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-__2sZEukV10/AAAAAAAAAAI/AAAAAAAAAAA/-x3ba3IKpBo/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Family Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-__2sZEukV10/AAAAAAAAAAI/AAAAAAAAAAA/-x3ba3IKpBo/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Drama",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-__2sZEukV10/AAAAAAAAAAI/AAAAAAAAAAA/-x3ba3IKpBo/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Family Recommended Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-ZKe79blip5M/AAAAAAAAAAI/AAAAAAAAAAA/oEGDoiVa46M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Family Channel",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-__2sZEukV10/AAAAAAAAAAI/AAAAAAAAAAA/-x3ba3IKpBo/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Romanctic Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-ZKe79blip5M/AAAAAAAAAAI/AAAAAAAAAAA/oEGDoiVa46M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Epic Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-ZKe79blip5M/AAAAAAAAAAI/AAAAAAAAAAA/oEGDoiVa46M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Comedy Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-ZKe79blip5M/AAAAAAAAAAI/AAAAAAAAAAA/oEGDoiVa46M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-ZKe79blip5M/AAAAAAAAAAI/AAAAAAAAAAA/oEGDoiVa46M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ikoro TV Chosen Ones (includes 18+ movies)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-ZKe79blip5M/AAAAAAAAAAI/AAAAAAAAAAA/oEGDoiVa46M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sylvester Madu's Week",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-LYcjnrFg5Tc/AAAAAAAAAAI/AAAAAAAAAAA/TuNQzUVyMZc/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="iBakaTV-Nollywood (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-LYcjnrFg5Tc/AAAAAAAAAAI/AAAAAAAAAAA/TuNQzUVyMZc/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Epic-Rural Movies African BoxOffice TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-8s7Gs0SJtJE/AAAAAAAAAAI/AAAAAAAAAAA/U_pozttsLqg/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Family Movies African BoxOffice TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-8s7Gs0SJtJE/AAAAAAAAAAI/AAAAAAAAAAA/U_pozttsLqg/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Royal Movies African BoxOffice TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-8s7Gs0SJtJE/AAAAAAAAAAI/AAAAAAAAAAA/U_pozttsLqg/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Comedy Movies African BoxOffice TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-8s7Gs0SJtJE/AAAAAAAAAAI/AAAAAAAAAAA/U_pozttsLqg/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Family Movies King of Nollywood",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-jl4C-jWAUEc/AAAAAAAAAAI/AAAAAAAAAAA/a1rIGHNNB5w/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sex and Romantic Movies King of Nollywood",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-jl4C-jWAUEc/AAAAAAAAAAI/AAAAAAAAAAA/a1rIGHNNB5w/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christian Movies King of Nollywood",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-jl4C-jWAUEc/AAAAAAAAAAI/AAAAAAAAAAA/a1rIGHNNB5w/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Latest Epic Movies King of Nollywood",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-jl4C-jWAUEc/AAAAAAAAAAI/AAAAAAAAAAA/a1rIGHNNB5w/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Movies of the Week - King of Nollywood",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-jl4C-jWAUEc/AAAAAAAAAAI/AAAAAAAAAAA/a1rIGHNNB5w/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Movies of the Month - King of Nollywood",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-jl4C-jWAUEc/AAAAAAAAAAI/AAAAAAAAAAA/a1rIGHNNB5w/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Trending Movies - King of Nollywood",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/-jl4C-jWAUEc/AAAAAAAAAAI/AAAAAAAAAAA/a1rIGHNNB5w/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="2016 Latest Nigerian Nollywood Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/-HajcYG3iAhk/AAAAAAAAAAI/AAAAAAAAAAA/zb98UE-sYmM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="2015 Latest Nigerian Nollywood Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/-HajcYG3iAhk/AAAAAAAAAAI/AAAAAAAAAAA/zb98UE-sYmM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best of Nollywood 5 Star",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/-n6A595gwrdY/AAAAAAAAAAI/AAAAAAAAAAA/ov5lQz69FmY/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Family Movies On Nollywood 5 Star",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-n6A595gwrdY/AAAAAAAAAAI/AAAAAAAAAAA/ov5lQz69FmY/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Action Movies On Nollywood 5 Star",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/-n6A595gwrdY/AAAAAAAAAAI/AAAAAAAAAAA/ov5lQz69FmY/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nigerian Movies On Nollywood 5 Star",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://yt3.ggpht.com/-n6A595gwrdY/AAAAAAAAAAI/AAAAAAAAAAA/ov5lQz69FmY/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christian Movies On Nollywood 5 Star",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://yt3.ggpht.com/-n6A595gwrdY/AAAAAAAAAAI/AAAAAAAAAAA/ov5lQz69FmY/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Romantic Movies On Nollywood 5 Star",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-n6A595gwrdY/AAAAAAAAAAI/AAAAAAAAAAA/ov5lQz69FmY/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Comedy Movies On Nollywood 5 Star",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://yt3.ggpht.com/-n6A595gwrdY/AAAAAAAAAAI/AAAAAAAAAAA/ov5lQz69FmY/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Epic Movies On Nollywood 5 Star",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-n6A595gwrdY/AAAAAAAAAAI/AAAAAAAAAAA/ov5lQz69FmY/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best of Golden Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Intrigue On Nollywood Gold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Faith On Nollywood Gold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Epic On Nollywood Gold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Drama On Nollywood Gold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Africa Cinema (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/-ECDvJBHKjXs/AAAAAAAAAAI/AAAAAAAAAAA/3mjtLpPT7BU/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Suspense On Nollywood Gold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Romance On Nollywood Gold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="18+ Movies On Nollywood Gold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tragedy On Nollywood Gold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Comedy On Nollywood Gold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://yt3.ggpht.com/-FTu48BOl9Y8/AAAAAAAAAAI/AAAAAAAAAAA/_sFRn9-6nuk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Family Nollywood Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://yt3.ggpht.com/-_Cj5e0sqBfg/AAAAAAAAAAI/AAAAAAAAAAA/Pb8ia3rocZ4/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Romance Nollywood movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://yt3.ggpht.com/-_Cj5e0sqBfg/AAAAAAAAAAI/AAAAAAAAAAA/Pb8ia3rocZ4/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Top Best Nollywood Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://yt3.ggpht.com/-_Cj5e0sqBfg/AAAAAAAAAAI/AAAAAAAAAAA/Pb8ia3rocZ4/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Epic But Ageless Nollywood Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://yt3.ggpht.com/-_Cj5e0sqBfg/AAAAAAAAAAI/AAAAAAAAAAA/Pb8ia3rocZ4/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HOT SEXY POPULAR IkORO TV MOVIES",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://yt3.ggpht.com/-ZKe79blip5M/AAAAAAAAAAI/AAAAAAAAAAA/oEGDoiVa46M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ikoro TV Sex/Crazy/Fun",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://yt3.ggpht.com/-ZKe79blip5M/AAAAAAAAAAI/AAAAAAAAAAA/oEGDoiVa46M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hot Nolly TV (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://yt3.ggpht.com/-CMHssqcjvJs/AAAAAAAAAAI/AAAAAAAAAAA/S_-WDGIH2Zc/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="RealNolly TV (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://yt3.ggpht.com/-IiV6IOZFO0Y/AAAAAAAAAAI/AAAAAAAAAAA/oYm1qQq9cJM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="tvNolly (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://yt3.ggpht.com/-oKxwd-zBoUk/AAAAAAAAAAI/AAAAAAAAAAA/UA42Tr_say0/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NewNollywood (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://yt3.ggpht.com/-06ttOFH1sBc/AAAAAAAAAAI/AAAAAAAAAAA/ExwRUzTitDo/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nollywood Best (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="https://yt3.ggpht.com/-WI3roIlOKsk/AAAAAAAAAAI/AAAAAAAAAAA/4gWBSXOe68A/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nollywood Pictures TV (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="https://yt3.ggpht.com/-HajcYG3iAhk/AAAAAAAAAAI/AAAAAAAAAAA/zb98UE-sYmM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NollyOptions (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="https://yt3.ggpht.com/-m_S2vf0-slg/AAAAAAAAAAI/AAAAAAAAAAA/IK3flLufTWM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nollywood Encore (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="https://yt3.ggpht.com/-8bsS7PYV6r0/AAAAAAAAAAI/AAAAAAAAAAA/tIaf4mNiu_M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nollywood5ive (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://yt3.ggpht.com/-mX1EN1S8x0Q/AAAAAAAAAAI/AAAAAAAAAAA/e5OYOF2OSLs/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nolly Prestige (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://yt3.ggpht.com/-O0kD3UtkCrI/AAAAAAAAAAI/AAAAAAAAAAA/I4ZYpr6mMjM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
run()
