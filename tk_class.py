from Tkinter import *
import Tkinter as tk
import tkFileDialog
import matplotlib
matplotlib.use("Svg")

import matplotlib.pyplot as plt
from matplotlib.patches import Shadow
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageTk
import sys

from testing import *

root = Tk()
myVar = StringVar()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("League Of Legends Stats")
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="submit", command=self.on_button)
        self.button.pack()
        self.entry.pack()
        self.geometry("450x450+500+300")

    def on_button(self):
        summonerName = self.entry.get()
        name = summonerName.split()
        summonerName = "".join(name)

        responseJSON  = requestSummonerData(summonerName)

        ID = responseJSON[summonerName]['id']
        ID = str(ID)
        # prints ID onto console
        id_Display = Label(self, text = ID).pack()


        responseJSON2 = requestRankedData(ID)

        rank = "Rank: " + responseJSON2[ID][0]['tier'] + " " + responseJSON2[ID][0]['entries'][0]['division']
        cm_rank = "Rank: " + responseJSON2[ID][0]['tier']
        lp = "League Points: " + str(responseJSON2[ID][0]['entries'][0]['leaguePoints'])

        try:
            rank_display = Label(self, text = rank).pack()
        except:
            unranked_display = Label(self, text = "Rank: Unranked").pack()

        responseMASTERY = requestMasteryData(ID)

        for i in range(0,3):
            champ_ID = responseMASTERY[i]['championId']
            responseCHAMP = requestChampionName()
            champs = responseCHAMP['data']

            for k, v in champs.iteritems():
                if responseCHAMP['data'][k]['id'] == champ_ID:
                    champion = "Champion: " + responseCHAMP['data'][k]['name']
                    champion_level = "Champion Level: " + str(responseMASTERY[i]['championLevel'])
                    champion_display = Label(self, text = champion).pack()
                    champion_level_display = Label(self, text = champion_level).pack()



app = SampleApp()
app.mainloop()
