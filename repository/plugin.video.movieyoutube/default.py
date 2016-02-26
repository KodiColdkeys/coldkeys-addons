# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Movies on YouTube Addon by coldkeys
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

addonID = 'plugin.video.movieyoutube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCu0bxC7vG_HKWJ7ijO9QKwg"
YOUTUBE_CHANNEL_ID_2 = "UCfjp6_4aAvhDGzvSkkAo0Jg"
YOUTUBE_CHANNEL_ID_3 = "UCaDVeUo4Xw2J7CX7Oyet1HA"
YOUTUBE_CHANNEL_ID_4 = "UCnJjSZdHJ4wWiJ4Q0dt8L7A"
YOUTUBE_CHANNEL_ID_5 = "UC4wuPZvkfftAL9AkvRA1IZQ"
YOUTUBE_CHANNEL_ID_6 = "UCvNPgFaq0HyjQakHbp3f3Ug"
YOUTUBE_CHANNEL_ID_7 = "UC3RG3BR7fY6FFKDHKv3keAA"
YOUTUBE_CHANNEL_ID_8 = "UCue4o36_p6Oq6njkwnlkl0Q"
YOUTUBE_CHANNEL_ID_9 = "UCdlxrbT0ox6QoxdCd2GYY1w"
YOUTUBE_CHANNEL_ID_10 = "UCMMLfzsXe-EbRREJgMcb8cQ"
YOUTUBE_CHANNEL_ID_11 = "UCT3UAHCH0fCxLwodm7-2CKQ"
YOUTUBE_CHANNEL_ID_12 = "UCPUU5swJo5XLqvn77s6FB8g"
YOUTUBE_CHANNEL_ID_13 = "UC2u3R3pjOiPZu4LtTlKkxdw"
YOUTUBE_CHANNEL_ID_14 = "UCwcKQZZdZZ1b5xD64S6IObw"
YOUTUBE_CHANNEL_ID_15 = "UCSUMyPPmunaDKk0YHxCK-cw"
YOUTUBE_CHANNEL_ID_16 = "UCg6g3bL8VA40rxxJNXGeT8A"
YOUTUBE_CHANNEL_ID_17 = "UCOg0aMAXmF3o5m243PxhE5g"
YOUTUBE_CHANNEL_ID_18 = "UCWlLgwn2nfjnefINARfcquA"
YOUTUBE_CHANNEL_ID_19 = "UCh51cE9j1n206mAZslHtf6A"
YOUTUBE_CHANNEL_ID_20 = "UCkv6qsVcDNcjgUbR_II5UPw"
YOUTUBE_CHANNEL_ID_21 = "UCBhskwCpv4Df8-xC8_wGxzA"
YOUTUBE_CHANNEL_ID_22 = "UCYFhhf_dxCXiRKgjUVpmfaw"
YOUTUBE_CHANNEL_ID_23 = "UCdtHojCvWRkJ_mx290WwEeg"
YOUTUBE_CHANNEL_ID_24 = "UCcaVajvK5kGlRZ5j-iCynPA"
YOUTUBE_CHANNEL_ID_25 = "UC2i60C2W7MJRZi2lbXyECig"
YOUTUBE_CHANNEL_ID_26 = "UCCq30E9PwvbpXaaM26Btw2g"
YOUTUBE_CHANNEL_ID_27 = "UCcaM3NN1qU8JtH2XtVsT6Gg"
YOUTUBE_CHANNEL_ID_28 = "UC-n2mADCBq--iuhwlroP4ig"
YOUTUBE_CHANNEL_ID_29 = "UCQf0IhUn2-S5-mEP3Mw-Kog"
YOUTUBE_CHANNEL_ID_30 = "UCNLOeImyafrTNvHqdsBpGHQ"
YOUTUBE_CHANNEL_ID_31 = "UCRrpZec8AV3R6FL51AvhzMQ"
YOUTUBE_CHANNEL_ID_32 = "UC2J9K3MnVWo9KwMwBJPBnUg"
YOUTUBE_CHANNEL_ID_33 = "PLruNIMIIsoRQQa4j__xdy_0Poec0gqiJE"
YOUTUBE_CHANNEL_ID_34 = "UCtG36aNGHp_H0NNOFr-B-Qg"
YOUTUBE_CHANNEL_ID_35 = "UCKWXdsDWlfYCImwF_B5w3RQ"
YOUTUBE_CHANNEL_ID_36 = "UC3w82RzgDThubF3cJuMwWIw"
YOUTUBE_CHANNEL_ID_37 = "UCpqNeR8PGoU8zs86DAf2B0Q"
YOUTUBE_CHANNEL_ID_38 = "UCONNU13ySnUnt97NJZInjmw"
YOUTUBE_CHANNEL_ID_39 = "UCI0zDHgOc40F-YhaH9XXKJQ"
YOUTUBE_CHANNEL_ID_40 = "UCnMz8v0tcy5DqvewzgZJemQ"
YOUTUBE_CHANNEL_ID_41 = "PLYLlM9kXGIDlOlUGpdV3TAGKS14Hlov_j"
YOUTUBE_CHANNEL_ID_42 = "UCB_lrveBtVpDXA17AigBUZg"
YOUTUBE_CHANNEL_ID_43 = "PLeagipoZmyfnIxkk9qKN-ewkuDeI-JP0i"
YOUTUBE_CHANNEL_ID_44 = "PLmHgXUJMN1TWyW6nJCPdj51WA-sMOozwD"
YOUTUBE_CHANNEL_ID_45 = "UCqbHJxPdN01huY8VAetWeaw"
YOUTUBE_CHANNEL_ID_46 = "UCAXVlAPg_IYYzyXOAPO_Sow"
YOUTUBE_CHANNEL_ID_47 = "UCQtWO-WAiW2K_67StRyubUA"
YOUTUBE_CHANNEL_ID_48 = "UCRzntwQEZhgOErPTIpKhpXA"
YOUTUBE_CHANNEL_ID_49 = "UCOv4ucnKIphDdpn8m3ib30A"
YOUTUBE_CHANNEL_ID_50 = "UCHgtHjKFMKqh_rhuQbjDrfA"

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
        title="Kings of Horror",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-kQJTY1j3FwM/AAAAAAAAAAI/AAAAAAAAAAA/WYLXCrtBTGE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CiNENET",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-4PaF-kMXwvc/AAAAAAAAAAI/AAAAAAAAAAA/UYnCs4kSqJc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Adventure Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-nnYoNaEinJg/AAAAAAAAAAI/AAAAAAAAAAA/c-BsRFjaKLo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old Science Fiction Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-2JBQ9iwEyHg/AAAAAAAAAAI/AAAAAAAAAAA/E8MFen8HgMw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Comedy Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-eMJ4r2u0OCk/AAAAAAAAAAI/AAAAAAAAAAA/w2OPN7667rA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Mystery Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-YLrr88EKrgY/AAAAAAAAAAI/AAAAAAAAAAA/wT0QJS-q-z8/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Romance Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-rTkeUN4bWiI/AAAAAAAAAAI/AAAAAAAAAAA/dbU3G9xHeOA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Public Domain Full Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-Z6XCFHXssj8/AAAAAAAAAAI/AAAAAAAAAAA/mURlU68JKAc/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Full Horror",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-Y2CXkDfA2jo/AAAAAAAAAAI/AAAAAAAAAAA/7gl5qWST43w/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Manic Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-NdFGinBdHBk/AAAAAAAAAAI/AAAAAAAAAAA/hEXe4n5cJ3o/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Silent Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-1vfVHv6nSk8/AAAAAAAAAAI/AAAAAAAAAAA/6970qnuedZs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Western Mania",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-Xr84C-lRqLY/AAAAAAAAAAI/AAAAAAAAAAA/SE1-KWnNDs8/s100-c-k-no/photo.jpg",folder=True )

    plugintools.add_item( 
        #action="", 
        title="Maverick Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-4g7SFjT3oN0/AAAAAAAAAAI/AAAAAAAAAAA/PNF6AnANgCM/s100-c-k-no/photo.jpg",folder=True )

    plugintools.add_item( 
        #action="", 
        title="Public Domain Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-5qRqrxT342E/AAAAAAAAAAI/AAAAAAAAAAA/RW19UPKXcWs/s100-c-k-no/photo.jpg",folder=True )

    plugintools.add_item( 
        #action="", 
        title="Viewster",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-2IJeniUPrP8/AAAAAAAAAAI/AAAAAAAAAAA/aLMgMHFjMPc/s100-c-k-no/photo.jpg",folder=True )

    plugintools.add_item( 
        #action="", 
        title="MyFlix",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-TpjU-WIi724/AAAAAAAAAAI/AAAAAAAAAAA/_6rBGQwr9kU/s100-c-k-no/photo.jpg",folder=True )

    plugintools.add_item( 
        #action="", 
        title="Timeless Classic Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-59bxvAQY0FU/AAAAAAAAAAI/AAAAAAAAAAA/bWmE_eGapCk/s100-c-k-no/photo.jpg",folder=True )

    plugintools.add_item( 
        #action="", 
        title="Timeless Classic Films (see playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/--2UtXIRXjMw/AAAAAAAAAAI/AAAAAAAAAAA/2rue_pLv5oc/s100-c-k-no/photo.jpg",folder=True )

    plugintools.add_item( 
        #action="", 
        title="Timeless Western Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-VAmN310PZsY/AAAAAAAAAAI/AAAAAAAAAAA/4wsYX-3YuDg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Timeless Film Noir Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-zyCdYh_YSRM/AAAAAAAAAAI/AAAAAAAAAAA/9g1UdR4IBxY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Video Cellar (see playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-wUUsZatv4IU/AAAAAAAAAAI/AAAAAAAAAAA/ilplpO9VKf0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old Mystery Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-eEDf9a_oz_k/AAAAAAAAAAI/AAAAAAAAAAA/4vNh3mZ4UFs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old Romance Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/-UQdGhqLOs8U/AAAAAAAAAAI/AAAAAAAAAAA/q-vUmB50k3I/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old Comedy Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/-Y1p8Vh4wN7M/AAAAAAAAAAI/AAAAAAAAAAA/4KUuIfcW_Gs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old Drama Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/-d7lLUPIWpvQ/AAAAAAAAAAI/AAAAAAAAAAA/7wJBU1v92GA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Anton Pictures (check playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/-cHoKDdiWsKY/AAAAAAAAAAI/AAAAAAAAAAA/e5gfRGYAsTo/s100-c-k-no-mo/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AB Movie Channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-t7toB6M6RdQ/AAAAAAAAAAI/AAAAAAAAAAA/2N8_BIlF_9g/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic TV Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/-m5GUGB9ELKg/AAAAAAAAAAI/AAAAAAAAAAA/zqlJrcAeOYw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Froggy Flix",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://i.ytimg.com/i/Qf0IhUn2-S5-mEP3Mw-Kog/mq1.jpg?v=5218f89d",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Movies (drelbcom)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Am POP Films and TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-sFH4PtYNrMg/AAAAAAAAAAI/AAAAAAAAAAA/3tG2PmAx644/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Black Belt Theater",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://i.ytimg.com/i/2J9K3MnVWo9KwMwBJPBnUg/mq1.jpg?v=516d90f1",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Johnny Kung Fu Cinema",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-UY88QYL_Fxg/AAAAAAAAAAI/AAAAAAAAAAA/UL9TKjH7s9M/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wu Tang Collection (see playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/-V02HWS9xcCc/AAAAAAAAAAI/AAAAAAAAAAA/3VCyvLFigDA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mystery Movies Full Length",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/-AadBhA4q33M/AAAAAAAAAAI/AAAAAAAAAAA/olkqqcj8fks/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Movies to Watch",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-1aKsmziIEjk/AAAAAAAAAAI/AAAAAAAAAAA/AayFpBMTpKE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Movies (one4allfour1)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/-inBgw98ww-U/AAAAAAAAAAI/AAAAAAAAAAA/PeQ51anR5aE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="More Classic Movies (MrsTJ)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-2cr1i26DZFY/AAAAAAAAAAI/AAAAAAAAAAA/0MaFo4wNHjM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vintage Mystery Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/-XLIfApWNEmU/AAAAAAAAAAI/AAAAAAAAAAA/zotlfrlfxhg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vintage Comedy Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-TRkY9Nn9m8o/AAAAAAAAAAI/AAAAAAAAAAA/ew_SQbC-C4E/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hallmark and Romance Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/UEzKBgjurTAkKSbedB9EEUoBIk0g_VeFg6m52j19ZNxMcCoa_H1dd-5UCkAQ9UVyLuhnDhA8kXg2_V6aRQ=s100-nd",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Flicks",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/-nOhCKcfRpjg/AAAAAAAAAAI/AAAAAAAAAAA/GJV8p8O38bg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Great Classic Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/-hFyL8l5MUTs/AAAAAAAAAAI/AAAAAAAAAAA/tJr2V8acY74/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="World War Cinema",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://i.ytimg.com/i/Ml3r8TD4YKzZR3C42G9fNQ/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Movie Artists A-E (see playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://i.ytimg.com/i/qbHJxPdN01huY8VAetWeaw/mq1.jpg?v=511cc5e5",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Movie Artists F-J (see playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://yt3.ggpht.com/-KK8VWlsvqPU/AAAAAAAAAAI/AAAAAAAAAAA/d3SY9bTwRAQ/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Movie Artists K-Q (see playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://yt3.ggpht.com/-XSm-fZ6X6nQ/AAAAAAAAAAI/AAAAAAAAAAA/IcJSvMgmX6o/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Movie Artists R-Z (see playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://yt3.ggpht.com/-cuTWUCtnPP0/AAAAAAAAAAI/AAAAAAAAAAA/r-XK0Q7eMog/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kids Movies and Cartoons (see playlists)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://i.ytimg.com/i/Ov4ucnKIphDdpn8m3ib30A/mq1.jpg?v=5124dcc2",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Blasts from the Past (Vintage Movie Classics)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://yt3.ggpht.com/-ndPbxTqHXnY/AAAAAAAAAAI/AAAAAAAAAAA/XNxJqYbTCX0/s100-c-k-no/photo.jpg",
        folder=True )
run()
