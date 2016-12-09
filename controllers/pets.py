@auth.requires_login()
# @auth.requires_membership('admin')
def index():
    marcaDagua = MARCADAGUA()

    # pets
    PETS = []

    pet =   DIV(
                DIV(
                    DIV(
                        SPAN(I(_class='ti-gift'),' 03/03/2015',_class='aniversario'),
                        SPAN('Cocotinho',_class='nomePet'),
                    _class="textPet"),
                _class="card",_id="cardPets"),
            _class="col-md-6")

    PETS.append(pet)
    PETS.append(pet)

    return dict(marcaDagua=marcaDagua,PETS=PETS)

def cadastro():
    
    # hide_fields("pets",["name"]) #esconder campos

    form = SQLFORM(db.pets) 


    form.elements('select')[0].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[0].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[2].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[1].attributes['_class'] = 'form-control datetime border-input' 
    # form.elements('input')[1].attributes['_type'] = 'date' 
    form.elements('input')[3].attributes['_class'] = 'form-control border-input' 
    form.elements('input')[5].attributes['_class'] = 'btn btn-info btn-fill btn-wd' 
    form.elements('input')[5].attributes['_value'] = 'Cadastrar' 

    if form.process().accepted:
        redirect(URL('pets','index'))
    elif form.errors:
        response.flash = T("Dados com erro")
    # cod = max(db(db.product).select('code'))['code'] #maior numero da coluna 'code'
    return dict(form=form)
