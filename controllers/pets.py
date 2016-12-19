# -*- conding: utf-8 -*-
# @auth.requires_membership('admin')
# @auth.requires_membershipres_login()


@auth.requires_login()
def index():
    # marca dagua
    marcaDagua = MARCADAGUA()
    # lista de pets
    PETS = db(db.pets.id>0).select()
    return dict(marcaDagua=marcaDagua,PETS=PETS)

@auth.requires_login()
def cadastro():
    # hide_fields("pets",["raca"]) #esconder campos

    form = SQLFORM(db.pets) # form pets

    # custumizando elementos do form
    form.elements('select')[0].attributes['_class'] = 'form-control border-input'
    form.elements('input')[0].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[2].attributes['_class'] = 'form-control border-input' 
    # form.elements('input')[1].attributes['_class'] = 'form-control datetime border-input' 
    # # form.elements('input')[3].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[4].attributes['_class'] = 'btn btn-info btn-fill btn-wd' 
    form.elements('input')[4].attributes['_value'] = 'Cadastrar' 
   # custumizando bt upload
    if form.process().accepted:
        redirect(URL('pets','index'))
    elif form.errors:
        response.flash = T("Dados com erro")
    # cod = max(db(db.product).select('code'))['code'] #maior numero da coluna 'code'
    return dict(form=form)


# Cuidados
@auth.requires_login()
def cuidados():
    pet = db(db.pets.id==request.args(0)) 
    name = pet.select('name')[0]['name']
    name = name.split(' ')[0]
    p_id = pet.select('id')[0]['id']
    form = SQLFORM(db.pets, int(p_id))
    form.elements('input')[4].attributes['_class'] = 'btn btn-info btn-fill btn-wd' 
    form.elements('input')[4].attributes['_value'] = 'Cadastrar' 
   # custumizando bt upload
    if form.process().accepted:
        redirect(URL('pets','cuidados',args=[p_id]))
    elif form.errors:
        response.flash = T("Dados com erro")

    avatar = URL('home','download',args=[pet.select('thumbnail')[0]['thumbnail']])
    especie = pet.select('especie')[0]['especie']
    return dict(pet=pet,name=name,avatar=avatar, especie=especie, form=form)

def editPets():
    p_id = request.vars.transitory
    hide_fields("pets",["id"]) #esconder campos
    form = SQLFORM(db.pets, int(p_id))
    form.elements('input')[4].attributes['_class'] = 'btn btn-info btn-fill btn-wd' 
    form.elements('input')[4].attributes['_value'] = 'Cadastrar'     

    # estilizar form





    formEdit = DIV(
                    DIV(
                        HR(),    
                        form,
                        _class="content"),
                 _class="row")
    return formEdit




