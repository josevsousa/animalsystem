
// antes do DOM
function init(){

}


// depois do DOM
window.onload = function(){
	preview_picture(); // preview na view
	// addImgNoInputFile();

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