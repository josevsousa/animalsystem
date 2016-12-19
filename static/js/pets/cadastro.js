

// antes do DOM
function init(){

}


// depois do DOM
window.onload = function(){
	// preview_picture(); // preview na view
	// addImgNoInputFile();

	// especie();
}

function especie(){
	//campo de Raca
	var pets_raca = document.getElementById('pets_raca'); 
	pets_raca.parentElement.style.display = 'none'; //esconde

	//raca temp
	var select = 'Raça'+
		'<select class=" transitory_especie form-control border-input" id="pets_sexo" name="sexo">'+
		'<option>dddd</option>'+
		'<option>ddwwwdd</option>'+
		'</select>';

	//input temp 
	var input = 'Raça<input class="transitory_especie  form-control border-input" name="transit" type="text" value="">'	
	//add input temp ao raca
	// $('.row')[4].children[0].children[0].innerHTML = input	


	// inputs
	var pets_especie = document.getElementById('pets_especie');
	var transitory = document.getElementById('transitory');

	pets_especie.addEventListener('change', function(){
		valor = this.value;
		transitory.value = valor
		if (valor == 'Gato') {
			// monta o select do Gato
			$('.row')[4].children[0].children[0].innerHTML = select	
		}else if(valor == 'Cão') {
			// monta o select do Cao
			$('.row')[4].children[0].children[0].innerHTML = select	
		}else{
			// monta o input
			$('.row')[4].children[0].children[0].innerHTML = input	
		}

		// ajax('campo_especie', ['transitory'])
	});

}


// mostrar imagem selecionada na view
function preview_picture(){
	var pets_picture = document.getElementById('pets_picture');
	pets_picture.addEventListener('change', function(){
		console.log(this.value);
	});
}

function addImgNoInputFile(){
	// var pets_picture__row = document.getElementById('pets_picture__row');
	// console.log(pets_picture__row.children[1]);

	// var img = document.createElement("img");
	// img.setAttribute("src", "../static/images/camera.png");
	// img.setAttribute("id","imgPreview");
	// img.setAttribute("height", "64");
	// img.setAttribute("width", "64");
	// img.setAttribute("alt", "Flower");
	// pets_picture__row.children[1].appendChild(img);
}
// $(document).ready(function() {




//    $('#pets_picture').on('change',function(){ 
//    		console.log($(this).val());
//       $('html, body').animate({scrollTop:0}, 'slow');
//   		return false;
//      });
//  });