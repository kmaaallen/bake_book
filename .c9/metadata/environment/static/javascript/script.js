{"filter":false,"title":"script.js","tooltip":"/static/javascript/script.js","undoManager":{"mark":27,"position":27,"stack":[[{"start":{"row":0,"column":0},"end":{"row":32,"column":7},"action":"insert","lines":[" //functions to add and remove extra inputs for method and ingredients","    function removeInput(e) {","        e.parentElement.remove(e.parentElement);","    }","    ","    function addIngredient() {","        var newInput = $(\"<div><input required type='text' value='' class='ingredients extra-input' name='ingredients'></input><a class='btn add-btn' onClick='removeInput(this)'><i class='material-icons'>delete</i></a><a class='btn add-btn' onClick='addIngredient()'><i class='material-icons'>add</i></a></div>\")","        $(\"#ingredients\").append(newInput);","    }","","    function addStep() {","        var newInput = $(\"<div><textarea value='' class='method extra-input' name='method'></textarea><a class='btn add-btn textarea-add-btn' onClick='removeInput(this)'><i class='material-icons'>delete</i></a><a class='btn add-btn textarea-add-btn' onClick='addStep()'><i class='material-icons'>add</i></a></div>\")","        $(\"#method\").append(newInput);","    }","    ","    // show recipe url preview if not empty","    function showPreview() {","        var new_url = document.getElementById('recipe_url').value;","        if (document.getElementById('edit_preview') != null) {","            document.getElementById('edit_preview').src = new_url;","        }else {","            document.getElementById('submit-preview').src = 'https://imgur.com/a/qeaCvhA';","            document.getElementById('edit_preview').src = 'https://imgur.com/a/qeaCvhA';","        }","    }","","    $(document).ready(function() {","        // if recipe_url field is present call showPreview","        if (document.getElementById('recipe_url')) {","            showPreview();","            document.getElementById('recipe_url').addEventListener('change', showPreview);","        }","    });"],"id":1}],[{"start":{"row":1,"column":1},"end":{"row":1,"column":4},"action":"remove","lines":["   "],"id":2},{"start":{"row":2,"column":0},"end":{"row":2,"column":3},"action":"remove","lines":["   "]},{"start":{"row":3,"column":1},"end":{"row":3,"column":4},"action":"remove","lines":["   "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":3},"action":"remove","lines":["   "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":3},"action":"remove","lines":["   "]},{"start":{"row":7,"column":5},"end":{"row":7,"column":8},"action":"remove","lines":["   "]},{"start":{"row":8,"column":1},"end":{"row":8,"column":4},"action":"remove","lines":["   "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":3},"action":"remove","lines":["   "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":3},"action":"remove","lines":["   "]},{"start":{"row":12,"column":5},"end":{"row":12,"column":8},"action":"remove","lines":["   "]},{"start":{"row":13,"column":1},"end":{"row":13,"column":4},"action":"remove","lines":["   "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":3},"action":"remove","lines":["   "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":3},"action":"remove","lines":["   "]},{"start":{"row":17,"column":5},"end":{"row":17,"column":8},"action":"remove","lines":["   "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":3},"action":"remove","lines":["   "]},{"start":{"row":19,"column":9},"end":{"row":19,"column":12},"action":"remove","lines":["   "]},{"start":{"row":20,"column":5},"end":{"row":21,"column":0},"action":"insert","lines":["}",""]},{"start":{"row":21,"column":3},"end":{"row":21,"column":4},"action":"remove","lines":["}"]},{"start":{"row":21,"column":3},"end":{"row":21,"column":5},"action":"insert","lines":["  "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":3},"action":"remove","lines":["   "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"remove","lines":[" "]},{"start":{"row":23,"column":9},"end":{"row":23,"column":11},"action":"remove","lines":["  "]},{"start":{"row":24,"column":5},"end":{"row":24,"column":8},"action":"remove","lines":["   "]},{"start":{"row":25,"column":1},"end":{"row":25,"column":4},"action":"remove","lines":["   "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":3},"action":"remove","lines":["   "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"remove","lines":[" "]},{"start":{"row":28,"column":5},"end":{"row":28,"column":7},"action":"remove","lines":["  "]},{"start":{"row":29,"column":5},"end":{"row":29,"column":8},"action":"remove","lines":["   "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":[" "]},{"start":{"row":30,"column":9},"end":{"row":30,"column":11},"action":"remove","lines":["  "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":3},"action":"remove","lines":["   "]},{"start":{"row":32,"column":5},"end":{"row":32,"column":8},"action":"remove","lines":["   "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":3},"action":"remove","lines":["   "]}],[{"start":{"row":25,"column":2},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":26,"column":0},"end":{"row":26,"column":1},"action":"insert","lines":[" "]},{"start":{"row":26,"column":1},"end":{"row":27,"column":0},"action":"insert","lines":["",""]},{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"insert","lines":[" "]},{"start":{"row":27,"column":1},"end":{"row":27,"column":2},"action":"insert","lines":["/"]},{"start":{"row":27,"column":2},"end":{"row":27,"column":3},"action":"insert","lines":["/"]}],[{"start":{"row":27,"column":3},"end":{"row":27,"column":4},"action":"insert","lines":[" "],"id":4},{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["c"]},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["h"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["e"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["c"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["k"]},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["i"]},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["n"]},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["g"]}],[{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":[" "],"id":5},{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":["i"]},{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"insert","lines":["f"]}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":[" "],"id":6},{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["n"]},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["o"]}],[{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":[" "],"id":7},{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"remove","lines":["s"],"id":8}],[{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":["s"],"id":9},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["e"]},{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"insert","lines":["a"]},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"insert","lines":["r"]},{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":["c"]},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["h"]}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":[" "],"id":10},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["r"]},{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":["e"]},{"start":{"row":27,"column":28},"end":{"row":27,"column":29},"action":"insert","lines":["s"]},{"start":{"row":27,"column":29},"end":{"row":27,"column":30},"action":"insert","lines":["u"]},{"start":{"row":27,"column":30},"end":{"row":27,"column":31},"action":"insert","lines":["l"]},{"start":{"row":27,"column":31},"end":{"row":27,"column":32},"action":"insert","lines":["t"]},{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":[" "],"id":11},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["t"]},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["o"]}],[{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":[" "],"id":12},{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["s"]}],[{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"remove","lines":["s"],"id":13}],[{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["d"],"id":14},{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"insert","lines":["i"]},{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"insert","lines":["s"]},{"start":{"row":27,"column":40},"end":{"row":27,"column":41},"action":"insert","lines":["p"]},{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"insert","lines":["l"]},{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"insert","lines":["a"]},{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"insert","lines":["y"]}],[{"start":{"row":27,"column":44},"end":{"row":27,"column":45},"action":"insert","lines":[" "],"id":15},{"start":{"row":27,"column":45},"end":{"row":27,"column":46},"action":"insert","lines":["n"]},{"start":{"row":27,"column":46},"end":{"row":27,"column":47},"action":"insert","lines":["o"]},{"start":{"row":27,"column":47},"end":{"row":27,"column":48},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":48},"end":{"row":27,"column":49},"action":"insert","lines":[" "],"id":16},{"start":{"row":27,"column":49},"end":{"row":27,"column":50},"action":"insert","lines":["f"]},{"start":{"row":27,"column":50},"end":{"row":27,"column":51},"action":"insert","lines":["o"]},{"start":{"row":27,"column":51},"end":{"row":27,"column":52},"action":"insert","lines":["u"]},{"start":{"row":27,"column":52},"end":{"row":27,"column":53},"action":"insert","lines":["n"]},{"start":{"row":27,"column":53},"end":{"row":27,"column":54},"action":"insert","lines":["d"]}],[{"start":{"row":27,"column":54},"end":{"row":27,"column":55},"action":"insert","lines":[" "],"id":17},{"start":{"row":27,"column":55},"end":{"row":27,"column":56},"action":"insert","lines":["m"]},{"start":{"row":27,"column":56},"end":{"row":27,"column":57},"action":"insert","lines":["e"]},{"start":{"row":27,"column":57},"end":{"row":27,"column":58},"action":"insert","lines":["s"]},{"start":{"row":27,"column":58},"end":{"row":27,"column":59},"action":"insert","lines":["s"]},{"start":{"row":27,"column":59},"end":{"row":27,"column":60},"action":"insert","lines":["a"]},{"start":{"row":27,"column":60},"end":{"row":27,"column":61},"action":"insert","lines":["g"]},{"start":{"row":27,"column":61},"end":{"row":27,"column":62},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":62},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":28,"column":1},"end":{"row":39,"column":3},"action":"insert","lines":["$('.search').on('keyup', function(event) { // Fired on 'keyup' event","","  if($('.list').children().length === 0) { // Checking if list is empty","","    $('.not-found').css('display', 'block'); // Display the Not Found message","","  } else {","","    $('.not-found').css('display', 'none'); // Hide the Not Found message","","  }","});"],"id":19}],[{"start":{"row":28,"column":69},"end":{"row":29,"column":0},"action":"remove","lines":["",""],"id":20}],[{"start":{"row":29,"column":71},"end":{"row":30,"column":0},"action":"remove","lines":["",""],"id":21}],[{"start":{"row":30,"column":77},"end":{"row":31,"column":0},"action":"remove","lines":["",""],"id":22}],[{"start":{"row":31,"column":10},"end":{"row":32,"column":0},"action":"remove","lines":["",""],"id":23}],[{"start":{"row":32,"column":73},"end":{"row":33,"column":0},"action":"remove","lines":["",""],"id":24}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":[" "],"id":25},{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":[" "]},{"start":{"row":31,"column":3},"end":{"row":32,"column":1},"action":"insert","lines":[""," "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":1},"action":"remove","lines":[" "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":28,"column":11},"end":{"row":28,"column":12},"action":"insert","lines":["-"],"id":26},{"start":{"row":28,"column":12},"end":{"row":28,"column":13},"action":"insert","lines":["f"]},{"start":{"row":28,"column":13},"end":{"row":28,"column":14},"action":"insert","lines":["o"]},{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"insert","lines":["r"]},{"start":{"row":28,"column":15},"end":{"row":28,"column":16},"action":"insert","lines":["m"]}],[{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"remove","lines":["p"],"id":27},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"remove","lines":["u"]},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"remove","lines":["y"]},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"remove","lines":["e"]},{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"remove","lines":["k"]}],[{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"insert","lines":["s"],"id":28},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"insert","lines":["u"]},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["b"]},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["m"]},{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"insert","lines":["i"]},{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":311,"scrollleft":0,"selection":{"start":{"row":37,"column":31},"end":{"row":37,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":256,"mode":"ace/mode/javascript"}},"timestamp":1570054122551,"hash":"2cccff7e437ba519b53f1a066d0096e8a131cb76"}