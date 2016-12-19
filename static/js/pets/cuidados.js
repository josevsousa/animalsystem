
$(document).ready(function(){
	$('#bt_editPet').on('click', function(){
		//passar o id do pet para o transitory
		$('#editPet').slideDown(400);
	})
})


// //carregado o DOM
// window.onload = function(){
// 	// inputs
// 	var bt_editPet = document.getElementById('bt_editPet')

// 	// carregar functions
// 	editCadastroPet()
// }


// // carragar form para editar o pet
// function editCadastroPet(){
// 	// ouvintes
// 	bt_editPet.addEventListener('click', function(){
// 		ajax('editPets', [], 'editPet')
// 	});
// }//fim do editCadastroPet	