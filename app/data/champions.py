VERSION = "15.15.1"

pool = [ # Talvez isso nem seja usado
    "Lulu",
    "Alistar",
    "Rakan",
    "Nautilus",
    "Thresh",
    "Pantheon",
    "Neeko",
    "Nami"
]

supports = {
    "Alistar": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Alistar.png", "label": ["Tanque", "Engage"]}, # Tem um leve peel e sustain aqui, leve
    "Bard": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Bard.png", "label": ["Poke", "CC_dano"]},
    "Blitzcrank": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Blitzcrank.png", "label": ["Tanque"]}, # Não coloquei engage aqui porque o site é meu e eu faço o que eu quiser, mas ainda é relevante contra Nami
    "Braum": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Braum.png", "label": ["Tanque", "Peel"]},
    "Brand": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Brand.png", "label": ["Poke"]}, # Leve CC
    "Karma": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Karma.png", "label": ["Enchanter", "Poke", "Peel"]}, # Bom blind
    "Leona": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Leona.png", "label": ["Tanque", "Engage"]},
    "Lulu": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Lulu.png", "label": ["Enchanter", "Peel"]},
    "Lux": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Lux.png", "label": ["Poke", "CC_dano"]}, # Lux não é nem suporte primeiramente
    "Milio": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Milio.png", "label": ["Enchanter", "Peel"]},
    "Morgana": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Morgana.png", "label": ["Peel", "CC_dano"]},
    "Nami": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Nami.png", "label": ["Enchanter", "Sustain"]},
    "Nautilus": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Nautilus.png", "label": ["Tanque", "Engage"]},
    "Neeko": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Neeko.png", "label": ["CC_dano", "Poke"]},
    "Pantheon": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Pantheon.png", "label": ["CC_dano", "Engage"]},
    "Pyke": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Pyke.png", "label": ["CC_dano", "Engage"]},
    "Rakan": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Rakan.png", "label": ["Engage", "Peel"]},
    "Rell": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Rell.png", "label": ["Tanque", "Engage"]},
    "Renata Glasc": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Renata.png", "label": ["Enchanter", "Peel"]},
    "Senna": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Senna.png", "label": ["Sustain", "Poke"]},
    "Seraphine": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Seraphine.png", "label": ["Enchanter", "Poke"]},
    "Sona": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Sona.png", "label": ["Enchanter", "Sustain", "Poke"]},
    "Soraka": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Soraka.png", "label": ["Sustain"]},
    "Tahm Kench": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/TahmKench.png", "label": ["Tanque", "Engage"]},
    "Taric": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Taric.png", "label": ["Tanque", "Peel", "Sustain"]},
    "Thresh": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Thresh.png", "label": ["Engage", "Peel"]}, # Não coloquei tanque, mas ele fica um pouco
    "Vel'Koz": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Velkoz.png", "label": ["Poke"]},
    "Xerath": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Xerath.png", "label": ["Poke"]},
    "Yuumi": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Yuumi.png", "label": ["Enchanter", "Peel"]},
    "Zilean": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Zilean.png", "label": ["Poke", "Peel"]}, # Não faço ideia se isso tá certo
    "Zyra": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Zyra.png", "label": ["Poke", "CC_dano"]},
}

adcarries = {
    "Aphelios": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Aphelios.png", "label": "Hypercarry"},
    "Ashe": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Ashe.png", "label": "Lane Bully"},
    "Brand": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Brand.png", "label": "Adcaster"},
    "Caitlyn": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Caitlyn.png", "label": "Lane Bully"},
    "Corki": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Corki.png", "label": "Adcaster"},
    "Draven": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Draven.png", "label": "Lane Bully"},
    "Ezreal": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Ezreal.png", "label": "Adcaster"},
    "Jhin": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Jhin.png", "label": "Adcaster"},
    "Jinx": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Jinx.png", "label": "Hypercarry"},
    "Kai'Sa": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/KaiSa.png", "label": "Skirmisher"},
    "Kalista": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Kalista.png", "label": "Skirmisher"},
    "Karthus": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Karthus.png", "label": "Adcaster"},
    "Kog'Maw": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/KogMaw.png", "label": "Hypercarry"},
    "Lucian": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Lucian.png", "label": "Skirmisher"},
    "Miss Fortune": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/MissFortune.png", "label": "Lane Bully"},
    "Nilah": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Nilah.png", "label": "Skirmisher"},
    "Samira": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Samira.png", "label": "Skirmisher"},
    "Senna": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Senna.png", "label": "Adcaster"},
    "Seraphine": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Seraphine.png", "label": "Adcaster"},
    "Sivir": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Sivir.png", "label": "Hypercarry"},
    "Smolder": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Smolder.png", "label": "Hypercarry"},
    "Swain": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Swain.png", "label": "Adcaster"},
    "Tristana": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Tristana.png", "label": "Skirmisher"},
    "Twitch": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Twitch.png", "label": "Hypercarry"},
    "Varus": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Varus.png", "label": "Adcaster"},
    "Vayne": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Vayne.png", "label": "Skirmisher"},
    "Veigar": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Veigar.png", "label": "Adcaster"},
    "Vel'Koz": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Velkoz.png", "label": "Adcaster"},
    "Xayah": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Xayah.png", "label": "Hypercarry"},
    "Xerath": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Xerath.png", "label": "Adcaster"},
    "Zeri": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Zeri.png", "label": "Hypercarry"},
    "Ziggs": {"img": f"https://ddragon.leagueoflegends.com/cdn/{VERSION}/img/champion/Ziggs.png", "label": "Adcaster"},
}