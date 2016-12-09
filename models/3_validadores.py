# -*- coding: utf-8 -*-
from smarthumb import SMARTHUMB


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


# valida pets
db.pets.name.requires = IS_NOT_EMPTY( error_message='nome obrigatório')
db.pets.sexo.requires = IS_IN_SET(SEXO)
db.pets.thumbnail.compute = lambda row: SMARTHUMB(row.picture, (200, 200))
# db.pets.sexo.widget = SQLFORM.widgets.radio.widget



# chamada comum
def get_miniatura(row):
     if row.thumbnail: #se usar virtual field tem que ser "row.product.thumbnail"
          return IMG( _src=URL('home', 'download', args=[row.thumbnail]))
     else:
          return IMG(_width=50, _heigth=50,_src=URL('static','images/mini.png'))

# chamada de uma virtual field products
def get_miniatura_sqlformgrid_products(row):
     if row.product.thumbnail: #se usar virtual field tem que ser "row.product.thumbnail"
          return IMG(_width=50, _heigth=50, _src=URL('home', 'download', args=[row.product.thumbnail]))
     else:
          return IMG(_width=50, _heigth=50,_src=URL('static','images/mini.png'))

# chamada de uma virtual field registration
def get_miniatura_sqlformgrid_registration(row):
     if row.registration.thumbnail: #se usar virtual field tem que ser "row.registration.thumbnail"
          return IMG(_width=50, _heigth=50, _src=URL('home', 'download', args=[row.registration.thumbnail]))
     else:
          return IMG(_width=50, _heigth=50,_src=URL('static','images/mini.png'))

#esconde campos da tabela passada por parametro
def hide_fields(tablename, fields):
    for field in fields:
        db[tablename][field].writable = \
            db[tablename][field].readable = False
