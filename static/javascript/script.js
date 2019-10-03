 //functions to add and remove extra inputs for method and ingredients
 function removeInput(e) {
     e.parentElement.remove(e.parentElement);
 }

 function addIngredient() {
     var newInput = $("<div><input required type='text' value='' class='ingredients extra-input' name='ingredients'></input><a class='btn add-btn' onClick='removeInput(this)'><i class='material-icons'>delete</i></a><a class='btn add-btn' onClick='addIngredient()'><i class='material-icons'>add</i></a></div>")
     $("#ingredients").append(newInput);
 }

 function addStep() {
     var newInput = $("<div><textarea value='' class='method extra-input' name='method'></textarea><a class='btn add-btn textarea-add-btn' onClick='removeInput(this)'><i class='material-icons'>delete</i></a><a class='btn add-btn textarea-add-btn' onClick='addStep()'><i class='material-icons'>add</i></a></div>")
     $("#method").append(newInput);
 }

 // show recipe url preview if not empty
 function showPreview() {
     var new_url = document.getElementById('recipe_url').value;
     if (document.getElementById('edit_preview') != null) {
         document.getElementById('edit_preview').src = new_url;
     }else if (document.getElementByIs('submit-preview') != null){
      document.getElementById('submit_preview').src = new_url;
     }else{
      document.getElementById('edit_preview').src = '/static/images/default.png';
     }
 }

 $(document).ready(function() {
     // if recipe_url field is present call showPreview
     if (document.getElementById('recipe_url')) {
         showPreview();
         document.getElementById('recipe_url').addEventListener('change', showPreview);
     }
 });