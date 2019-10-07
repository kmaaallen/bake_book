 //functions to add and remove extra inputs for method and ingredients
 function removeInput(e) {
     e.parentElement.remove(e.parentElement);
 }

 function addIngredient() {
     var newInput = $("<div><input required type='text' value='' class='ingredients extra-input extra-ing-input' name='ingredients'></input><a class='btn add-btn' onClick='removeInput(this)'><i class='material-icons del-btn-ing'>delete</i></a><a class='btn add-btn' onClick='addIngredient()'><i class='material-icons'>add</i></a></div>")
     $("#ingredients").append(newInput);
 }

 function addStep() {
     var newInput = $("<div><textarea value='' class='method extra-input extra-step-input' name='method'></textarea><a class='btn add-btn textarea-add-btn' onClick='removeInput(this)'><i class='material-icons del-btn-step'>delete</i></a><a class='btn add-btn textarea-add-btn' onClick='addStep()'><i class='material-icons'>add</i></a></div>")
     $("#method").append(newInput);
 }

 // show recipe url preview if not empty
 function showEditPreview() {
  var new_url = document.getElementById('recipe_url').value;
  if (document.getElementById('recipe_url').value != "") {
   document.getElementById('edit-preview').src = new_url;
  }
  else {
   document.getElementById('edit-preview').src = '/static/images/default.png';
  }
 }
 
 function showSubmitPreview() {
  var new_url = document.getElementById('recipe_url').value;
  if (document.getElementById('recipe_url').value != "") {
   document.getElementById('submit-preview').src = new_url;
  }
  else {
   document.getElementById('submit-preview').src = "/static/images/default.png";
  }
 }

 $(document).ready(function() {
  // if recipe_url field is present call showPreview
  if (document.getElementById('edit-preview')) {
   showEditPreview();
   document.getElementById('recipe_url').addEventListener('change', showEditPreview);
  }
  else if (document.getElementById('submit-preview')) {
   showSubmitPreview();
   document.getElementById('recipe_url').addEventListener('change', showSubmitPreview);
  }
 });