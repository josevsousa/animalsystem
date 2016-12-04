# -*- coding: utf-8 -*-

from uuid import uuid1 #codigo aleatorio
from datetime import datetime, timedelta #data

# settings
import os
file = open(os.path.join(request.folder,'private','settings.txt'))
file_settings = file.readlines()


# logo min
logomin = DIV(
    I('pets',_class='material-icons'),
    H1('Animal',SPAN('System'),_id='logoFont2'),
_class='logoBar')
