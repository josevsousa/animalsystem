# @auth.requires_login()
# @auth.requires_membership('admin')


def index():
    marcaDagua = MARCADAGUA()

    # lista de pets
    PETS = db(db.pets.id>0).select()

    # tbody
    tbody = TBODY()
    tbodyy = db(db.pets.id>0).select()
    # row
    row = DIV(_class="row card_pet") 
    cont = 1
    for pet in PETS:
        # tem avatar?
        avatar = pet.thumbnail
        if avatar:
            avatar = IMG(_src=URL('home','download', args='%s'%avatar), _class="card_pet-img" )
        else:
            avatar = IMG(_src=URL('static','images/no-photo.png'), _class="card_pet-img" )
            pass

        cart = DIV(
                DIV(
                    avatar,
                    DIV(SPAN(pet.name),_class="card_pet-nome"),
                    BR(),
                    DIV(SPAN(pet.name),_class="card_pet-data"),
                    _class="card"),
                _class="col-md-4")        
        if cont == 4: 
            tbody.append(row) # 1 add a row a tbody

            # 2 limpa a row
            row = DIV(_class="row card_pet") 

            row.append(cart) # add um card ao row
            cont = 0    

        else:
            row.append(cart) # add um card ao row
            cont += 1    
    tbody.append(row)
       
     

#             <img class="card_pet-img" src="{{=URL('static','images/blog-1.jpg')}}" alt="">
#             <div class="card_pet-nome">
#                 <small>Cocotinho</small>
#             </div>
#             <br>
#             <div class="card_pet-data">
#                 <small>03/03/2030</small>
#             </div>





    return dict(marcaDagua=marcaDagua,PETS=tbodyy)

def cadastro():
    
    # hide_fields("pets",["name"]) #esconder campos

    form = SQLFORM(db.pets) # form pets

    # custumizando elementos do form
    form.elements('select')[0].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[0].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[2].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[1].attributes['_class'] = 'form-control datetime border-input' 
    # form.elements('input')[1].attributes['_type'] = 'date' 
    form.elements('input')[3].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[5].attributes['_class'] = 'btn btn-info btn-fill btn-wd' 
    form.elements('input')[5].attributes['_value'] = 'Cadastrar' 

    # custumizando bt upload
    
    

    if form.process().accepted:
        redirect(URL('pets','index'))
    elif form.errors:
        response.flash = T("Dados com erro")
    # cod = max(db(db.product).select('code'))['code'] #maior numero da coluna 'code'
    return dict(form=form)
