# Author: Leah Jameson
# Date: April 9, 2025
# Description: Parse stats from html from WUL stats website

from bs4 import BeautifulSoup
import re 
import json

class Player:
    def __init__(self):
        self.id = None
        self.jersey = None

        self.name = None
        self.PP = None
        self.plusMinus = None
        self.goals = None
        self.assists = None
        self.blocks = None
        self.throwingYards = None
        self.receivingYards = None

    def __str__(self):
        return f"Player Id: {self.id}, Name: {self.name}, #{self.jersey}, Points Played: {self.PP}, +/-: {self.plusMinus}, G: {self.goals}, A: {self.assists}, B: {self.blocks}, ThY: {self.throwingYards}, RecY: {self.receivingYards}"
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def to_typescript(self):
        print(f"{{\n\tid: {self.id},\n\tname: '{self.name}',\n\tjersey: '{self.jersey}',\n\tpointsPlayed: '{self.PP}',\n\tplusMinus: '{self.plusMinus}',\n\tgoals: '{self.goals}',\n\tassists: '{self.assists}',\n\tblocks: '{self.blocks}',\n\tthrowingYards: '{self.throwingYards}',\n\treceivingYards: '{self.receivingYards}',\n\tphoto: '',\n\tlogo: 'https://static.wixstatic.com/media/29d923_719ce83b05194b0da66d50e2b7a71f7b~mv2.png/v1/fill/w_146,h_146,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/Sidewinders%20Logo%20-%20Final-High%20Res-transparent-06%20(1).png'\n}},")



def extract_data(fileName: str, tag: str):
    soup = BeautifulSoup(open(fileName), 'html.parser')
    elements = soup.findAll(tag)
    return elements
    
def get_team_attributes(player_list: list[Player], team_data):
    for player_data in team_data:
        attr = get_player_stats(player_data)
        myPlayer = Player()

        myPlayer.id = attr[0]
        myPlayer.jersey = re.search('\\d+', attr[1]).group()
        myPlayer.name = re.search(r'[A-Za-z].*', attr[1]).group()
        myPlayer.PP = attr[3]
        myPlayer.plusMinus = attr[8]
        myPlayer.goals = attr[9]
        myPlayer.assists = attr[10]
        myPlayer.blocks = attr[11]
        myPlayer.throwingYards = attr[13]
        myPlayer.receivingYards = attr[14]

        player_list.append(myPlayer)

def get_player_stats(player_data):
    tds = player_data.find_all('td')
    stat_list = []
    for td in tds:
        stat_array = td.contents
        stat = stat_array[0]
        stat_list.append(stat)
    
    #print(stat_list)
    return stat_list

def make_player_service(players):
    json = ''
    for player in players:
        temp_json = player.to_json()
        json = json + temp_json + ','
    return json

def print_typescript(players):
    for player in players:
        player.to_typescript()


tag = 'tr'
players: list[Player] = []
stat_sheet: list[str] = []

elems = extract_data('stats.html', tag)
get_team_attributes(players, elems) 








    


    
