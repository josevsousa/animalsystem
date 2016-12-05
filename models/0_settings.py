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
        H1('Animal',SPAN('System'),_id='logoFont2'),
    _class='logoBar')
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
