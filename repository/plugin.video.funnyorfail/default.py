# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Funny or Fail Addon by coldkeys
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

addonID = 'plugin.video.funnyorfail'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLOWSbqDrrI5T4AY9D66nqASG6r7rD2XPC"
YOUTUBE_CHANNEL_ID_2 = "PLOWSbqDrrI5QU6-kEuXq2eFqWZ3po6yHh"
YOUTUBE_CHANNEL_ID_3 = "PLOWSbqDrrI5Tb6W1EP9WZEaWTP6Ij-6bg"
YOUTUBE_CHANNEL_ID_4 = "PLOWSbqDrrI5RV1I7JKTWQnvJpjgqC_yzD"
YOUTUBE_CHANNEL_ID_5 = "PLOWSbqDrrI5Tdgvmzjk3GSTS0uYsKoDpR"
YOUTUBE_CHANNEL_ID_6 = "PLAaBltRDhMdh-2QReMP-wImYSEnu3Jca1"
YOUTUBE_CHANNEL_ID_7 = "PLQkaoIh35eHMdjMWsYSg5tThkysPxwHUP"
YOUTUBE_CHANNEL_ID_8 = "PLQkaoIh35eHN0XJe233B7AfUjkrJaYVUk"
YOUTUBE_CHANNEL_ID_9 = "PLEIVVA_XsEy-oIjKA6_wOzmAG-uGXGvfX"
YOUTUBE_CHANNEL_ID_10 = "PLEJpi2B2tk6gg5XGebOnL4q6rDRwBndgs"
YOUTUBE_CHANNEL_ID_11 = "PLnEgJF0UIKFBTVFF6du4d66LqmDHWluj9"
YOUTUBE_CHANNEL_ID_12 = "PLqWamYnsxbyuCM0LyihersD5qxDQwamwf"
YOUTUBE_CHANNEL_ID_13 = "PLIlbJUq9-xypZkcZBwziXxAzW90Qaa5G_"
YOUTUBE_CHANNEL_ID_14 = "PLVI4iL-N2fz-Xv2H52AAPei3hauCzptAw"
YOUTUBE_CHANNEL_ID_15 = "PLVI4iL-N2fz8_KkfT3ZzbLbG5kxOStLhR"
YOUTUBE_CHANNEL_ID_16 = "PLhAhjCDDyiHazYSO71Yo8r1d-Ab-S1Lz6"
YOUTUBE_CHANNEL_ID_17 = "PLS6-05Eref9mo7YBbZoL0_wd2p29QtB3_"
YOUTUBE_CHANNEL_ID_18 = "PLxiMX1T_Wj0IkJl0h_TkhDXL6DwDV_CvB"
YOUTUBE_CHANNEL_ID_19 = "PLKcOqx7x-2Jbq_MTZODhkDhEWS0EdTK-r"
YOUTUBE_CHANNEL_ID_20 = "PL6A5E9FC1A526B92D"
YOUTUBE_CHANNEL_ID_21 = "PL6BPLAHZEOQQFXXUTjrW3WSxql2eppked"
YOUTUBE_CHANNEL_ID_22 = "PLjRy4mVBoTO7f7vFqNpFHPIl5cA5SK0y_"
YOUTUBE_CHANNEL_ID_23 = "PLujt7KppNLovb8_rXyShFtnguoBQ1dOAh"
YOUTUBE_CHANNEL_ID_24 = "PLJHfedoaM2Z0qlkA0j1E9pVw0SX-E_egN"
YOUTUBE_CHANNEL_ID_25 = "PLxsVcyXgSDtI4v8Ub7k2W4bg7D1pIzU65"
YOUTUBE_CHANNEL_ID_26 = "PLJHfedoaM2Z1OdIjmqH8nUEhpktnT4g8Y"
YOUTUBE_CHANNEL_ID_27 = "PLhOYRw2LCXIa4Wcm3EZvO9vl3O8S1evEy"
YOUTUBE_CHANNEL_ID_28 = "PLTur7oukosPG-0YsOfU8NHMKycSc8UqdB"
YOUTUBE_CHANNEL_ID_29 = "PL15dtrx_ng4T1SO8Rp6qI-R2dy0EMzcXl"
YOUTUBE_CHANNEL_ID_30 = "PLujt7KppNLosAZVih3Z1SmxXqm70hvbQF"
YOUTUBE_CHANNEL_ID_31 = "PLgwTjRbkf4_MOWpo9Te1-tWhuAr40Su_f"
YOUTUBE_CHANNEL_ID_32 = "PL3qyRiLTGtCw27siY4v2Hug73xHxU2iHh"
YOUTUBE_CHANNEL_ID_33 = "PL8i4XUHc-J5yRNEEAiAx4WlDt1FhteKEj"
YOUTUBE_CHANNEL_ID_34 = "PL3qyRiLTGtCwh24iq4XsELVuiDAmFjflV"
YOUTUBE_CHANNEL_ID_35 = "PL3qyRiLTGtCybyTQixEdmXGwZkxQ6A4fE"
YOUTUBE_CHANNEL_ID_36 = "PL3qyRiLTGtCxvaLAdaZNqkTWmCrRqswlR"
YOUTUBE_CHANNEL_ID_37 = "PLed2R78QUHAuS_-jykLb75pB_iM7rWQxd"
YOUTUBE_CHANNEL_ID_38 = "PLWm08UzFRiAOqTzJApBnuuhFxhR1V6PwB"
YOUTUBE_CHANNEL_ID_39 = "PLz9JxPpKRG-SX_XJ9IWk1bmt-64tNMMrg"
YOUTUBE_CHANNEL_ID_40 = "PLJQew7BwE7YbLw5GTqmNDdsieIWWJtF2t"
YOUTUBE_CHANNEL_ID_41 = "PL48IcNMrDM9JvDekM7SLTJiKyqgANEmQQ"
YOUTUBE_CHANNEL_ID_42 = "PLk9FCj28WmD27NS4IN9OEddxi_EUzX9Ep"
YOUTUBE_CHANNEL_ID_43 = "PLIGST5YUQld7wr-aQHLJf7ZEbVIOfVEdL"
YOUTUBE_CHANNEL_ID_44 = "PLIZ7BsXFtpfVuY6P5xBuEcP58Z-uDIKfT"
YOUTUBE_CHANNEL_ID_45 = "PLZ-WfMzo06f6AXGV8Kg60P1T8WMWaAit9"
YOUTUBE_CHANNEL_ID_46 = "PLtven5AlrFdgJBT_xS5gZF20__lITQN0Y"
YOUTUBE_CHANNEL_ID_47 = "PLwODrD2ItXSJ91txjLOuU8H1LsFbhKiRj"
YOUTUBE_CHANNEL_ID_48 = "PLX-ZnS97SHIn2nGcyhDFJygrH4kSsFjHw"
YOUTUBE_CHANNEL_ID_49 = "PL7r9Vc3EtHlP-W0zKaUo3Muzq5a7vcjdL"
YOUTUBE_CHANNEL_ID_50 = "PLfYnyHdPcUR5utrH_8QIlGWHGmTLrUdZV"
YOUTUBE_CHANNEL_ID_51 = "PLrbOUcXk2JPXbE2_XK1M7r9GSS8ffhS77"
YOUTUBE_CHANNEL_ID_52 = "PLR3HDpepAYV43dhCY7cE3bzdceaNXE-tN"
YOUTUBE_CHANNEL_ID_53 = "PLn5HI3tIeeUjTVO6Q1k5USPXofZ-OTvUN"
YOUTUBE_CHANNEL_ID_54 = "PLE1H5rdNP-jPe0mIKCm0wNfV_-1rHArBl"
YOUTUBE_CHANNEL_ID_55 = "PLGf8djhBr-YrFeWQF0hXF349dpCo3EDMs"
YOUTUBE_CHANNEL_ID_56 = "PLSxVCgPWs0Lx3WC3VidwUELwkw_3kPVOX"
YOUTUBE_CHANNEL_ID_57 = "PL3MoGqSOvn2YMxgggM-dovyO1WyHWzHuu"
YOUTUBE_CHANNEL_ID_58 = "PLekM955lctTFJpeKI4NTDPrxi8yvvhrD7"
YOUTUBE_CHANNEL_ID_59 = "PLgOSJOil2tDL90o11_gBF-vJAqaNQVjlQ"
YOUTUBE_CHANNEL_ID_60 = "PLBki3xnxeJjeMZ8lkZ8I_7IZ7nxX4uCFM"
YOUTUBE_CHANNEL_ID_61 = "PLH4HIAY31IJ-dcSTohBVDwIrIz19AHNS6"
YOUTUBE_CHANNEL_ID_62 = "PLrpSNoXKB8GnJCQ6_hjbTfuKvQ8Rxla7l"
YOUTUBE_CHANNEL_ID_63 = "PL-CTTdieQaCcoX2YUBkYeKKS38Ys_XUho"
YOUTUBE_CHANNEL_ID_64 = "PLaPX5t7r_kCf2M-Mawk15lSi7VE9nPmAs"
YOUTUBE_CHANNEL_ID_65 = "PLdpqUU6bj782ywcwnmJhKNwqO9pK1T-tI"
YOUTUBE_CHANNEL_ID_66 = "PL8IvA21IxpXqm88I6nB-O8y7JvitXTo0L"
YOUTUBE_CHANNEL_ID_67 = "PL9dHHpXICjZZR8_2ryOTxDYOE9KRLGXuB"
YOUTUBE_CHANNEL_ID_68 = "PL-yAgRSeHLo_HIR-VRsgdUlOnlVsCwjT3"
YOUTUBE_CHANNEL_ID_69 = "PLoV9FA-MZwVPbop3oGDdkODVUZfBxtfWX"
YOUTUBE_CHANNEL_ID_70 = "PL152bjytsMC76ZjMEAJ_uh5Q5_B2MgcfC"
YOUTUBE_CHANNEL_ID_71 = "PLW9SfICSvxY0czeGP8BvcfnMkXpqpL2rN"
YOUTUBE_CHANNEL_ID_72 = "PLS7C-ySUpBRZdvnYjSaCvj2Kh1xuvHC45"
YOUTUBE_CHANNEL_ID_73 = "PLRIBB50h4LzfNV96mQ_elvqe0vIe3pm9t"
YOUTUBE_CHANNEL_ID_74 = "PLRIBB50h4LzexaMdfH-gme4rR7ZSgaiY8"
YOUTUBE_CHANNEL_ID_75 = "PLRIBB50h4Lze_3gAQ0h1uaGoSODY_HjMT"
YOUTUBE_CHANNEL_ID_76 = "PLRcB4n4CGcy8D8fRrmpnlUUNFKNnPGMdP"
YOUTUBE_CHANNEL_ID_77 = "PLRcB4n4CGcy_WXVg-oFNRxnIPEPrXkKF-"
YOUTUBE_CHANNEL_ID_78 = "PLRcB4n4CGcy8UEtapNfAr6_QYEZ7k53lI"
YOUTUBE_CHANNEL_ID_79 = "PLRcB4n4CGcy9uL80Efnr8r9eR46YHHEOM"
YOUTUBE_CHANNEL_ID_80 = "PL4FD8AB1659AC413B"

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
        title="FailArmy's Best Fails of the Month",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.ytimg.com/vi/AMyeP1xIyy4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FailArmy's Best Fails of the Week",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.ytimg.com/vi/gkAay0yPX5g/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Epic Fails - FailArmy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://i1.ytimg.com/vi/vjWFtkOI0NE/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FailArmy Specials: Best Themed Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.ytimg.com/vi/Zh3x9dl_xrg/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ultimate Fails Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.ytimg.com/vi/RL2BJD8Ecms/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Epic Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://i.ytimg.com/vi/lnJKFsuJx5Q/hqdefault.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Fail Hall of Fame",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.ytimg.com/vi/eS9vBshE3Xg/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funniest Fail Compilations!",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://i1.ytimg.com/vi/xoFEVpW8-Hw/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FailFun Ultimate Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://i.ytimg.com/vi/MZGQ18zZDD8/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="All Fails!!!",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://i.ytimg.com/vi/yOO46-atzuo/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fail Vine Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://i.ytimg.com/vi/BGkBSVzuVvg/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dumbest FAILS of the Internet",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://i.ytimg.com/vi/95YAYRMCBmA/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="World's Dumbest",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://i.ytimg.com/vi/nwnnegA4vRY/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://i.ytimg.com/vi/hJbyKD2no_8/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny Internet Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://i.ytimg.com/vi/elYnBQ8bFtM/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="America's Dumbest Criminals",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://i.ytimg.com/vi/RmxDLAtj6jE/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Game Show Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://i1.ytimg.com/vi/bmQyyiAiATA/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Off-road Epic Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://i.ytimg.com/vi/LgifW8m0qPY/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny Fail, Epic Fail",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://i.ytimg.com/vi/lnJKFsuJx5Q/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Epic Fail",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://i.ytimg.com/vi/nZHoONe2V58/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best World Fails Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://i.ytimg.com/vi/21D3HEutJsc/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Funny Fails and Bloopers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://i.ytimg.com/vi/-JrOTBvwy6o/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Animal Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://i.ytimg.com/vi/81hJRiHh4PM/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funniest Animal Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://i.ytimg.com/vi/wj3BILPQoCo/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Internet Haz Cats And Dogs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="http://i.ytimg.com/vi/HNtBphqE_LA/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny Cat Videos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="http://i1.ytimg.com/vi/G4-yDzQ0cyU/hqdefault.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Funny Dog Videos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://i.ytimg.com/vi/LX-pEGXYJB0/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Video Game Fails of the Week",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="http://i.ytimg.com/vi/tdHoC3gxri4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Horrible Photoshop Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://i.ytimg.com/vi/j6OxAVpcFsM/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fails Compilation",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://i.ytimg.com/vi/2jIiYFC9DQQ/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny Fails 2016",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://i.ytimg.com/vi/HG2rfXqME80/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Truck Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://i.ytimg.com/vi/Z2-qlSYYZ6g/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Truck Racing Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://i.ytimg.com/vi/PcGHH1nHJGs/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Car Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://i.ytimg.com/vi/vKRPJKJBe7E/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bus Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://i.ytimg.com/vi/h2pSAIPEOzQ/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Motorcycle Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="http://i1.ytimg.com/vi/xpG3W7x1mAM/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cyclo-Cross Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://i.ytimg.com/vi/KBDeJZAkr0Q/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mountain Biking Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="http://i.ytimg.com/vi/ejWurIFhyw8/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JukinVideo Favorite Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://i.ytimg.com/vi/tzDgvAuOJmY/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fail City",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://i.ytimg.com/vi/NtIImATBchY/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wedding Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="http://i1.ytimg.com/vi/SorWElpUwQU/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tricking Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://i.ytimg.com/vi/yzzDXAdYzwU/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny Fails Playlist",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="http://i1.ytimg.com/vi/ljPgAAFXBjY/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Epic Fails and Best Vine",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://i.ytimg.com/vi/ssn6IJc3deo/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bully Instant Karma Fail",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://i.ytimg.com/vi/PTrTxBlmFNk/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Top 5 Soccer/Football Fails of the Week",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="http://img.youtube.com/vi/LAJWcd5H6So/0.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Australian Football Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://i.ytimg.com/vi/zlgcLrpswhg/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Softball Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://i.ytimg.com/vi/6VXWI_fnfdo/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Athletics Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://i.ytimg.com/vi/GC3W3nrTtO8/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hockey Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="http://i1.ytimg.com/vi/15Vr2HVuLbw/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ice Hockey Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://i.ytimg.com/vi/bVeY_0wSHwM/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Shooting Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="http://i1.ytimg.com/vi/QbzOZR1X5gQ/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Golfing Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="http://i.ytimg.com/vi/K-CO3cO9hY0/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Skateboarding Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="http://i.ytimg.com/vi/NlgWq8bW4fI/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Winter Sports Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="http://i.ytimg.com/vi/_6BQPC-pY2A/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Snowboarding Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="http://i.ytimg.com/vi/pR3ZER8vpHw/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Alpine Skiing Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="https://i.ytimg.com/vi/Za8Xe22lHBQ/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Freestyle Skiing Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="http://i.ytimg.com/vi/HRCni8DBQfw/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Snowkiting Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="http://i.ytimg.com/vi/Di7cpL9my2Y/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Speed Flying Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://i.ytimg.com/vi/s0tdim4NCJk/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Waterskiing Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://i.ytimg.com/vi/ufU7ZkAn0GI/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jet Ski Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="http://i1.ytimg.com/vi/2I3mFpt_1zw/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Surfing Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="http://i.ytimg.com/vi/Y70bll1EHiY/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sailing Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="http://i.ytimg.com/vi/m7_vgQa6Fds/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Canoeing Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="https://i.ytimg.com/vi/6xpy5lW_eHI/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Powerboating Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="https://i.ytimg.com/vi/Z7Q3ElA8ITY/hqdefault.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Sail and Motor Boat Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="http://i.ytimg.com/vi/r0T7R2JgukM/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rodeo Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="https://i.ytimg.com/vi/0JkE4A8sLrg/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Horse Racing Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="https://i.ytimg.com/vi/dH9uqkZSH0M/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Funny Commercials/Banned Commercials",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="https://i.ytimg.com/vi/PRiYkwtBK34/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Amazing Life Funny Everyday",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="http://i1.ytimg.com/vi/VnIIRBWscMg/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="People Are Stupid Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="http://i1.ytimg.com/vi/ZNpb5bwuwp4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Fails of 2016",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="https://i.ytimg.com/vi/zephAD8WwMQ/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Fails of the Week",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="http://www.chicanonews.net/wp-content/uploads/2016/11/1479134454_hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Fails of the Month Compilations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_75+"/",
        thumbnail="https://i.ytimg.com/vi/AMyeP1xIyy4/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny or Die Has Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_76+"/",
        thumbnail="http://i.ytimg.com/vi/a2mH3JyHsGs/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny or Die Has Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_77+"/",
        thumbnail="https://i.ytimg.com/vi/F6g85lp2wJc/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny or Die Has Sex",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_78+"/",
        thumbnail="https://i.ytimg.com/vi/xGF9lwfr-t8/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny or Die Community",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_79+"/",
        thumbnail="http://t.fod4.com/t/06f01543af/c480x270_33.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny or Die Hall of Fame",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_80+"/",
        thumbnail="http://i.ytimg.com/vi/zAfrBr5vbMU/hqdefault.jpg",
        folder=True )
run()
