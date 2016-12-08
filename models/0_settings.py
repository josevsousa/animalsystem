# -*- coding: utf-8 -*-

from uuid import uuid1 #codigo aleatorio
from datetime import datetime, timedelta #data

# settings
import os
file = open(os.path.join(request.folder,'private','settings.txt'))
file_settings = file.readlines()


# logo min
def LOGINMIN():
    logomin = DIV(
        I('pets',_class='material-icons'),
        # H1(file_settings[0].capitalize(),SPAN(file_settings[1].capitalize()),_id='logoFont2'),
        A(H1('Animal',SPAN('System'),_id='logoFont2'),_href=URL('../../pets'))
    ,_class='logoBar')
    return logomin

# marcaDagua
def MARCADAGUA():
    marcaDagua = DIV(
        I('pets',_class="material-icons"),
        # H1((file_settings[0:2]),_id='logoFont3'),
        H1('AnimalSystem',_id='logoFont3'),
        SPAN('+ Proteção a seu animalzinho'),
    _id="logoBox")
    return marcaDagua



# <div id="logoBox">
#     <i class="material-icons">pets</i>
#     <h1 id='logoFont3'>Animal<span>System</span></h1>
#     <span>+ Proteção a seu animalzinho</span>
# </div>

SEXO = [
    'Macho',
    'Macho cadastrado',
    'Fêmea',
    'Fêmea cadastrada'
]
RACAS = {
    'Cão':[
        'Sem raça',
        'Vira lata',
        'Alano Espanhol',
        'Airedale Terrier',
        'American Staffordshire Terrier',
        'American Water Spaniel',
        'Antigo Cão de Pastor Inglês',
        'Basset Azul da Gasconha',
        'Basset Fulvo da Bretanha',
        'Basset Hound',
        'Beagle',
        'Bearded Collie',
        'Bichon Maltês',
        'Bobtail',
        'Border Collie',
        'Boston Terrier',
        'Boxer',
        'Bull Terrier',
        'Bullmastiff',
        'Bulldog',
        'Cão de Montanha dos Pirinéus',
        'Caniche',
        'Chihuahua',
        'Cirneco do Etna',
        'Chow Chow ',
        'Cocker Spaniel (Americano ou Inglês)',
        'Dálmata',
        'Dobermann',
        'Dogue Alemão',
        'Dogue Argentino',
        'Dogue Canário',
        'Fox Terrier',
        'Foxhound',
        'Galgo',
        'Golden Retriever',
        "Gos d'Atura",
        'Husky Siberiano',
        'Laika',
        'Labrador Retriever',
        'Malamute-do-Alasca',
        'Mastin dos Pirenéus',
        'Mastin do Tibete',
        'Mastin Espanhol',
        'Mastín Napolitano',
        'Pastor Alemão',
        'Pastor Belga ',
        'Pastor de Brie',
        'Pastor dos Pirenéus de Cara Rosa',
        'Pequinês',
        'Perdigueiro',
        'Pitbull',
        'Podengo',
        'Pointer',
        'Pug',
        'Rhodesian Ridgeback',
        'Rottweiler ',
        'Rough Collie',
        'Sabueso (Espanhol ou Italiano)',
        'Saluki',
        'Samoiedo',
        'São Bernardo',
        'Scottish Terrier',
        'Setter Irlandés',
        'Shar-Pei',
        'Shiba Inu ',
        'Smooth Collie',
        'Staffordshire Bull Terrier',
        'Teckel',
        'Terra-nova',
        'Terrier Australiano',
        'Terrier Escocês',
        'Terrier Irlandês',
        'Terrier Japonês',
        'Terrier Negro Russo',
        'Terrier Norfolk',
        'Terrier Norwich',
        'Terrier Tibetano',
        'Welhs Terrier',
        'West Highland T',
        'Wolfspitz',
        'Yorkshire Terrier'
    ],
    'Gato':[
        'Abissínio',
        'Angorá turco',
        'American curl',
        'American Shorthair',
        'American wirehair',
        'Azul ruso',
        'Balinês',
        'Bengal',
        'Bobtail Japonês',
        'Bombay',
        'British Shorthair',
        'Burmês',
        'Burmês Europeu',
        'California spangled',
        'Chartreux',
        'Cornish rex',
        'Devon Rex',
        'Exótico',
        'Habana',
        'Himalayan',
        'Javanês',
        'Korat',
        'Maine coon',
        'Manx',
        'Mau Egípcio	N',
        'Nibelungo',
        'Noruega da floresta',
        'Ocicat',
        'Oriental de pêlo curto',
        'Persa',
        'Ragamuffin',
        'Ragdoll',
        'Sagrado da Birmânia',
        'Scottish fold',
        'Selkirk rex',
        'Siamês',
        'Singapur',
        'Shorthair Americano',
        'Shorthair Britânico',
        'Shorthair Exótico',
        'Snowshoe',
        'Somali',
        'Sphynx',
        'Tiffanie',
        'Tonquinês',
        'Van turco'
    ]
}
