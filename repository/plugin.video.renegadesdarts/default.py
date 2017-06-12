# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Renegades Darts by Coldkeys & AP
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import re
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.renegadesdarts'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID = "UC4hni3O2-HrgbAyY9QduJdg"

# Entry point

def run():
    #plugintools.log("UC4hni3O2-HrgbAyY9QduJdg.run")
    
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
    textfile = "https://raw.githubusercontent.com/KodiColdkeys/whitedevil-xml/master/renegadesdarts.txt"
    word = plugintools.read(textfile)
    #plugintools.log("UC4hni3O2-HrgbAyY9QduJdg.main_list"+repr(params))
    names = re.compile('.+?ame="(.+?)"').findall(word)
    urls = re.compile('.+?youtube.com/playlist/(.+?)"').findall(word)
    icons = re.compile('.+?con="(.+?)"').findall(word)
    for name,url,icon in zip(names,urls,icons):
        xbmc.log(name)
        xbmc.log(url)
        xbmc.log(icon)
        plugintools.add_item(
            title=name,
            url="plugin://plugin.video.youtube/playlist/"+url+"/",
            thumbnail=icon,
            folder=True)
run()