{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":116,"column":9},"end":{"row":116,"column":19},"action":"remove","lines":["recipes = "],"id":2823},{"start":{"row":116,"column":9},"end":{"row":116,"column":72},"action":"insert","lines":["recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})"]}],[{"start":{"row":117,"column":0},"end":{"row":117,"column":4},"action":"remove","lines":["    "],"id":2824},{"start":{"row":118,"column":0},"end":{"row":118,"column":4},"action":"remove","lines":["    "]},{"start":{"row":119,"column":0},"end":{"row":119,"column":4},"action":"remove","lines":["    "]},{"start":{"row":120,"column":0},"end":{"row":120,"column":4},"action":"remove","lines":["    "]},{"start":{"row":121,"column":0},"end":{"row":121,"column":4},"action":"remove","lines":["    "]},{"start":{"row":122,"column":0},"end":{"row":122,"column":4},"action":"remove","lines":["    "]},{"start":{"row":123,"column":0},"end":{"row":123,"column":4},"action":"remove","lines":["    "]},{"start":{"row":124,"column":0},"end":{"row":124,"column":4},"action":"remove","lines":["    "]},{"start":{"row":125,"column":0},"end":{"row":125,"column":4},"action":"remove","lines":["    "]},{"start":{"row":126,"column":0},"end":{"row":126,"column":4},"action":"remove","lines":["    "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":4},"action":"remove","lines":["    "]},{"start":{"row":128,"column":0},"end":{"row":128,"column":4},"action":"remove","lines":["    "]},{"start":{"row":129,"column":0},"end":{"row":129,"column":4},"action":"remove","lines":["    "]},{"start":{"row":130,"column":0},"end":{"row":130,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":116,"column":8},"end":{"row":116,"column":9},"action":"remove","lines":[" "],"id":2825}],[{"start":{"row":116,"column":8},"end":{"row":116,"column":71},"action":"remove","lines":["recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})"],"id":2826}],[{"start":{"row":116,"column":4},"end":{"row":116,"column":8},"action":"remove","lines":["    "],"id":2827},{"start":{"row":116,"column":0},"end":{"row":116,"column":4},"action":"remove","lines":["    "]},{"start":{"row":115,"column":33},"end":{"row":116,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":114,"column":29},"end":{"row":115,"column":0},"action":"insert","lines":["",""],"id":2828},{"start":{"row":115,"column":0},"end":{"row":115,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":115,"column":4},"end":{"row":115,"column":67},"action":"insert","lines":["recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})"],"id":2829}],[{"start":{"row":117,"column":7},"end":{"row":117,"column":21},"action":"remove","lines":[" new_recipe = "],"id":2830}],[{"start":{"row":116,"column":4},"end":{"row":116,"column":5},"action":"remove","lines":[" "],"id":2831}],[{"start":{"row":117,"column":7},"end":{"row":117,"column":8},"action":"insert","lines":[" "],"id":2832}],[{"start":{"row":130,"column":12},"end":{"row":131,"column":0},"action":"insert","lines":["",""],"id":2833},{"start":{"row":131,"column":0},"end":{"row":131,"column":11},"action":"insert","lines":["           "]}],[{"start":{"row":131,"column":10},"end":{"row":131,"column":11},"action":"remove","lines":[" "],"id":2834},{"start":{"row":131,"column":9},"end":{"row":131,"column":10},"action":"remove","lines":[" "]},{"start":{"row":131,"column":8},"end":{"row":131,"column":9},"action":"remove","lines":[" "]},{"start":{"row":131,"column":4},"end":{"row":131,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":131,"column":4},"end":{"row":131,"column":5},"action":"insert","lines":["r"],"id":2835},{"start":{"row":131,"column":5},"end":{"row":131,"column":6},"action":"insert","lines":["e"]},{"start":{"row":131,"column":6},"end":{"row":131,"column":7},"action":"insert","lines":["t"]},{"start":{"row":131,"column":7},"end":{"row":131,"column":8},"action":"insert","lines":["u"]},{"start":{"row":131,"column":8},"end":{"row":131,"column":9},"action":"insert","lines":["r"]},{"start":{"row":131,"column":9},"end":{"row":131,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":131,"column":10},"end":{"row":131,"column":11},"action":"insert","lines":[" "],"id":2836}],[{"start":{"row":131,"column":4},"end":{"row":131,"column":11},"action":"remove","lines":["return "],"id":2837},{"start":{"row":131,"column":4},"end":{"row":131,"column":110},"action":"insert","lines":["return render_template(\"recipecard.html\", recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))"]}],[{"start":{"row":114,"column":29},"end":{"row":115,"column":0},"action":"insert","lines":["",""],"id":2838},{"start":{"row":115,"column":0},"end":{"row":115,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":115,"column":4},"end":{"row":115,"column":38},"action":"insert","lines":["form = AddRecipeForm(request.form)"],"id":2839}],[{"start":{"row":111,"column":28},"end":{"row":111,"column":34},"action":"remove","lines":["submit"],"id":2840},{"start":{"row":111,"column":28},"end":{"row":111,"column":29},"action":"insert","lines":["e"]},{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"insert","lines":["d"]},{"start":{"row":111,"column":30},"end":{"row":111,"column":31},"action":"insert","lines":["i"]},{"start":{"row":111,"column":31},"end":{"row":111,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":110,"column":27},"end":{"row":111,"column":0},"action":"insert","lines":["",""],"id":2841},{"start":{"row":111,"column":0},"end":{"row":111,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":111,"column":4},"end":{"row":111,"column":5},"action":"insert","lines":["r"],"id":2842},{"start":{"row":111,"column":5},"end":{"row":111,"column":6},"action":"insert","lines":["e"]},{"start":{"row":111,"column":6},"end":{"row":111,"column":7},"action":"insert","lines":["c"]},{"start":{"row":111,"column":7},"end":{"row":111,"column":8},"action":"insert","lines":["i"]},{"start":{"row":111,"column":8},"end":{"row":111,"column":9},"action":"insert","lines":["p"]},{"start":{"row":111,"column":9},"end":{"row":111,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":111,"column":10},"end":{"row":111,"column":11},"action":"insert","lines":[" "],"id":2843},{"start":{"row":111,"column":11},"end":{"row":111,"column":12},"action":"insert","lines":["="]}],[{"start":{"row":111,"column":12},"end":{"row":111,"column":13},"action":"insert","lines":[" "],"id":2844},{"start":{"row":111,"column":13},"end":{"row":111,"column":14},"action":"insert","lines":["m"]},{"start":{"row":111,"column":14},"end":{"row":111,"column":15},"action":"insert","lines":["o"]},{"start":{"row":111,"column":15},"end":{"row":111,"column":16},"action":"insert","lines":["n"]},{"start":{"row":111,"column":16},"end":{"row":111,"column":17},"action":"insert","lines":["g"]},{"start":{"row":111,"column":17},"end":{"row":111,"column":18},"action":"insert","lines":["o"]},{"start":{"row":111,"column":18},"end":{"row":111,"column":19},"action":"insert","lines":["."]}],[{"start":{"row":111,"column":19},"end":{"row":111,"column":20},"action":"insert","lines":["d"],"id":2845},{"start":{"row":111,"column":20},"end":{"row":111,"column":21},"action":"insert","lines":["b"]},{"start":{"row":111,"column":21},"end":{"row":111,"column":22},"action":"insert","lines":["."]},{"start":{"row":111,"column":22},"end":{"row":111,"column":23},"action":"insert","lines":["r"]},{"start":{"row":111,"column":23},"end":{"row":111,"column":24},"action":"insert","lines":["e"]},{"start":{"row":111,"column":24},"end":{"row":111,"column":25},"action":"insert","lines":["c"]},{"start":{"row":111,"column":25},"end":{"row":111,"column":26},"action":"insert","lines":["i"]},{"start":{"row":111,"column":26},"end":{"row":111,"column":27},"action":"insert","lines":["p"]},{"start":{"row":111,"column":27},"end":{"row":111,"column":28},"action":"insert","lines":["e"]},{"start":{"row":111,"column":28},"end":{"row":111,"column":29},"action":"insert","lines":["s"]},{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"insert","lines":["."]}],[{"start":{"row":111,"column":30},"end":{"row":111,"column":31},"action":"insert","lines":["f"],"id":2846},{"start":{"row":111,"column":31},"end":{"row":111,"column":32},"action":"insert","lines":["i"]},{"start":{"row":111,"column":32},"end":{"row":111,"column":33},"action":"insert","lines":["n"]},{"start":{"row":111,"column":33},"end":{"row":111,"column":34},"action":"insert","lines":["_"]}],[{"start":{"row":111,"column":33},"end":{"row":111,"column":34},"action":"remove","lines":["_"],"id":2847},{"start":{"row":111,"column":32},"end":{"row":111,"column":33},"action":"remove","lines":["n"]}],[{"start":{"row":111,"column":32},"end":{"row":111,"column":33},"action":"insert","lines":["d"],"id":2848}],[{"start":{"row":111,"column":32},"end":{"row":111,"column":33},"action":"remove","lines":["d"],"id":2849}],[{"start":{"row":111,"column":32},"end":{"row":111,"column":33},"action":"insert","lines":["n"],"id":2850},{"start":{"row":111,"column":33},"end":{"row":111,"column":34},"action":"insert","lines":["d"]}],[{"start":{"row":111,"column":30},"end":{"row":111,"column":34},"action":"remove","lines":["find"],"id":2851},{"start":{"row":111,"column":30},"end":{"row":111,"column":38},"action":"insert","lines":["find_one"]}],[{"start":{"row":111,"column":38},"end":{"row":111,"column":40},"action":"insert","lines":["()"],"id":2852}],[{"start":{"row":111,"column":39},"end":{"row":111,"column":41},"action":"insert","lines":["{}"],"id":2853}],[{"start":{"row":111,"column":40},"end":{"row":111,"column":42},"action":"insert","lines":["''"],"id":2854}],[{"start":{"row":111,"column":41},"end":{"row":111,"column":42},"action":"insert","lines":["_"],"id":2855},{"start":{"row":111,"column":42},"end":{"row":111,"column":43},"action":"insert","lines":["i"]},{"start":{"row":111,"column":43},"end":{"row":111,"column":44},"action":"insert","lines":["d"]}],[{"start":{"row":111,"column":45},"end":{"row":111,"column":46},"action":"insert","lines":[":"],"id":2856}],[{"start":{"row":111,"column":46},"end":{"row":111,"column":47},"action":"insert","lines":[" "],"id":2857},{"start":{"row":111,"column":47},"end":{"row":111,"column":48},"action":"insert","lines":["O"]},{"start":{"row":111,"column":48},"end":{"row":111,"column":49},"action":"insert","lines":["b"]},{"start":{"row":111,"column":49},"end":{"row":111,"column":50},"action":"insert","lines":["j"]},{"start":{"row":111,"column":50},"end":{"row":111,"column":51},"action":"insert","lines":["e"]},{"start":{"row":111,"column":51},"end":{"row":111,"column":52},"action":"insert","lines":["c"]},{"start":{"row":111,"column":52},"end":{"row":111,"column":53},"action":"insert","lines":["t"]},{"start":{"row":111,"column":53},"end":{"row":111,"column":54},"action":"insert","lines":["I"]}],[{"start":{"row":111,"column":54},"end":{"row":111,"column":55},"action":"insert","lines":["d"],"id":2858}],[{"start":{"row":111,"column":55},"end":{"row":111,"column":57},"action":"insert","lines":["()"],"id":2859}],[{"start":{"row":111,"column":56},"end":{"row":111,"column":57},"action":"insert","lines":["r"],"id":2860},{"start":{"row":111,"column":57},"end":{"row":111,"column":58},"action":"insert","lines":["e"]},{"start":{"row":111,"column":58},"end":{"row":111,"column":59},"action":"insert","lines":["c"]},{"start":{"row":111,"column":59},"end":{"row":111,"column":60},"action":"insert","lines":["i"]},{"start":{"row":111,"column":60},"end":{"row":111,"column":61},"action":"insert","lines":["p"]},{"start":{"row":111,"column":61},"end":{"row":111,"column":62},"action":"insert","lines":["e"]},{"start":{"row":111,"column":62},"end":{"row":111,"column":63},"action":"insert","lines":["_"]},{"start":{"row":111,"column":63},"end":{"row":111,"column":64},"action":"insert","lines":["i"]},{"start":{"row":111,"column":64},"end":{"row":111,"column":65},"action":"insert","lines":["d"]}],[{"start":{"row":111,"column":68},"end":{"row":112,"column":0},"action":"insert","lines":["",""],"id":2861},{"start":{"row":112,"column":0},"end":{"row":112,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":112,"column":4},"end":{"row":112,"column":5},"action":"insert","lines":["f"],"id":2862},{"start":{"row":112,"column":5},"end":{"row":112,"column":6},"action":"insert","lines":["o"]},{"start":{"row":112,"column":6},"end":{"row":112,"column":7},"action":"insert","lines":["r"]},{"start":{"row":112,"column":7},"end":{"row":112,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":112,"column":8},"end":{"row":112,"column":9},"action":"insert","lines":[" "],"id":2863},{"start":{"row":112,"column":9},"end":{"row":112,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":112,"column":10},"end":{"row":112,"column":11},"action":"insert","lines":[" "],"id":2864},{"start":{"row":112,"column":11},"end":{"row":112,"column":12},"action":"insert","lines":["A"]},{"start":{"row":112,"column":12},"end":{"row":112,"column":13},"action":"insert","lines":["d"]},{"start":{"row":112,"column":13},"end":{"row":112,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":112,"column":11},"end":{"row":112,"column":14},"action":"remove","lines":["Add"],"id":2865},{"start":{"row":112,"column":11},"end":{"row":112,"column":24},"action":"insert","lines":["AddRecipeForm"]}],[{"start":{"row":112,"column":24},"end":{"row":112,"column":26},"action":"insert","lines":["()"],"id":2866}],[{"start":{"row":112,"column":25},"end":{"row":112,"column":26},"action":"insert","lines":["r"],"id":2867},{"start":{"row":112,"column":26},"end":{"row":112,"column":27},"action":"insert","lines":["e"]},{"start":{"row":112,"column":27},"end":{"row":112,"column":28},"action":"insert","lines":["q"]},{"start":{"row":112,"column":28},"end":{"row":112,"column":29},"action":"insert","lines":["u"]},{"start":{"row":112,"column":29},"end":{"row":112,"column":30},"action":"insert","lines":["e"]},{"start":{"row":112,"column":30},"end":{"row":112,"column":31},"action":"insert","lines":["s"]},{"start":{"row":112,"column":31},"end":{"row":112,"column":32},"action":"insert","lines":["t"]},{"start":{"row":112,"column":32},"end":{"row":112,"column":33},"action":"insert","lines":["."]},{"start":{"row":112,"column":33},"end":{"row":112,"column":34},"action":"insert","lines":["P"]},{"start":{"row":112,"column":34},"end":{"row":112,"column":35},"action":"insert","lines":["O"]}],[{"start":{"row":112,"column":35},"end":{"row":112,"column":36},"action":"insert","lines":["S"],"id":2868},{"start":{"row":112,"column":36},"end":{"row":112,"column":37},"action":"insert","lines":["T"]},{"start":{"row":112,"column":37},"end":{"row":112,"column":38},"action":"insert","lines":[","]}],[{"start":{"row":112,"column":38},"end":{"row":112,"column":39},"action":"insert","lines":[" "],"id":2869}],[{"start":{"row":112,"column":39},"end":{"row":112,"column":40},"action":"insert","lines":["r"],"id":2870},{"start":{"row":112,"column":40},"end":{"row":112,"column":41},"action":"insert","lines":["e"]},{"start":{"row":112,"column":41},"end":{"row":112,"column":42},"action":"insert","lines":["c"]},{"start":{"row":112,"column":42},"end":{"row":112,"column":43},"action":"insert","lines":["i"]},{"start":{"row":112,"column":43},"end":{"row":112,"column":44},"action":"insert","lines":["p"]},{"start":{"row":112,"column":44},"end":{"row":112,"column":45},"action":"insert","lines":["e"]}],[{"start":{"row":110,"column":25},"end":{"row":110,"column":26},"action":"insert","lines":[","],"id":2871}],[{"start":{"row":110,"column":26},"end":{"row":110,"column":27},"action":"insert","lines":[" "],"id":2872},{"start":{"row":110,"column":27},"end":{"row":110,"column":28},"action":"insert","lines":["r"]},{"start":{"row":110,"column":28},"end":{"row":110,"column":29},"action":"insert","lines":["e"]},{"start":{"row":110,"column":29},"end":{"row":110,"column":30},"action":"insert","lines":["q"]},{"start":{"row":110,"column":30},"end":{"row":110,"column":31},"action":"insert","lines":["u"]},{"start":{"row":110,"column":31},"end":{"row":110,"column":32},"action":"insert","lines":["e"]},{"start":{"row":110,"column":32},"end":{"row":110,"column":33},"action":"insert","lines":["s"]},{"start":{"row":110,"column":33},"end":{"row":110,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":112,"column":46},"end":{"row":113,"column":0},"action":"insert","lines":["",""],"id":2873},{"start":{"row":113,"column":0},"end":{"row":113,"column":4},"action":"insert","lines":["    "]},{"start":{"row":113,"column":4},"end":{"row":113,"column":5},"action":"insert","lines":["i"]},{"start":{"row":113,"column":5},"end":{"row":113,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":113,"column":6},"end":{"row":113,"column":7},"action":"insert","lines":[" "],"id":2874},{"start":{"row":113,"column":7},"end":{"row":113,"column":8},"action":"insert","lines":["r"]},{"start":{"row":113,"column":8},"end":{"row":113,"column":9},"action":"insert","lines":["e"]},{"start":{"row":113,"column":9},"end":{"row":113,"column":10},"action":"insert","lines":["q"]},{"start":{"row":113,"column":10},"end":{"row":113,"column":11},"action":"insert","lines":["u"]},{"start":{"row":113,"column":11},"end":{"row":113,"column":12},"action":"insert","lines":["e"]},{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"insert","lines":["s"]},{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"insert","lines":["t"]},{"start":{"row":113,"column":14},"end":{"row":113,"column":15},"action":"insert","lines":["."]},{"start":{"row":113,"column":15},"end":{"row":113,"column":16},"action":"insert","lines":["m"]},{"start":{"row":113,"column":16},"end":{"row":113,"column":17},"action":"insert","lines":["e"]},{"start":{"row":113,"column":17},"end":{"row":113,"column":18},"action":"insert","lines":["t"]},{"start":{"row":113,"column":18},"end":{"row":113,"column":19},"action":"insert","lines":["h"]},{"start":{"row":113,"column":19},"end":{"row":113,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":113,"column":19},"end":{"row":113,"column":20},"action":"remove","lines":["o"],"id":2875},{"start":{"row":113,"column":18},"end":{"row":113,"column":19},"action":"remove","lines":["h"]}],[{"start":{"row":113,"column":18},"end":{"row":113,"column":19},"action":"insert","lines":["h"],"id":2876},{"start":{"row":113,"column":19},"end":{"row":113,"column":20},"action":"insert","lines":["o"]},{"start":{"row":113,"column":20},"end":{"row":113,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":113,"column":21},"end":{"row":113,"column":22},"action":"insert","lines":[" "],"id":2877},{"start":{"row":113,"column":22},"end":{"row":113,"column":23},"action":"insert","lines":["="]},{"start":{"row":113,"column":23},"end":{"row":113,"column":24},"action":"insert","lines":["="]}],[{"start":{"row":113,"column":24},"end":{"row":113,"column":25},"action":"insert","lines":[" "],"id":2878}],[{"start":{"row":113,"column":25},"end":{"row":113,"column":27},"action":"insert","lines":["''"],"id":2879}],[{"start":{"row":113,"column":26},"end":{"row":113,"column":27},"action":"insert","lines":["P"],"id":2880},{"start":{"row":113,"column":27},"end":{"row":113,"column":28},"action":"insert","lines":["O"]},{"start":{"row":113,"column":28},"end":{"row":113,"column":29},"action":"insert","lines":["S"]},{"start":{"row":113,"column":29},"end":{"row":113,"column":30},"action":"insert","lines":["T"]}],[{"start":{"row":113,"column":31},"end":{"row":113,"column":32},"action":"insert","lines":[" "],"id":2881}],[{"start":{"row":113,"column":31},"end":{"row":113,"column":32},"action":"remove","lines":[" "],"id":2882}],[{"start":{"row":113,"column":31},"end":{"row":113,"column":32},"action":"insert","lines":[":"],"id":2883}],[{"start":{"row":113,"column":32},"end":{"row":114,"column":0},"action":"insert","lines":["",""],"id":2884},{"start":{"row":114,"column":0},"end":{"row":114,"column":8},"action":"insert","lines":["        "]},{"start":{"row":114,"column":8},"end":{"row":114,"column":9},"action":"insert","lines":["f"]},{"start":{"row":114,"column":9},"end":{"row":114,"column":10},"action":"insert","lines":["o"]},{"start":{"row":114,"column":10},"end":{"row":114,"column":11},"action":"insert","lines":["r"]},{"start":{"row":114,"column":11},"end":{"row":114,"column":12},"action":"insert","lines":["m"]},{"start":{"row":114,"column":12},"end":{"row":114,"column":13},"action":"insert","lines":["."]},{"start":{"row":114,"column":13},"end":{"row":114,"column":14},"action":"insert","lines":["p"]},{"start":{"row":114,"column":14},"end":{"row":114,"column":15},"action":"insert","lines":["o"]},{"start":{"row":114,"column":15},"end":{"row":114,"column":16},"action":"insert","lines":["p"]},{"start":{"row":114,"column":16},"end":{"row":114,"column":17},"action":"insert","lines":["u"]}],[{"start":{"row":114,"column":17},"end":{"row":114,"column":18},"action":"insert","lines":["l"],"id":2885},{"start":{"row":114,"column":18},"end":{"row":114,"column":19},"action":"insert","lines":["a"]},{"start":{"row":114,"column":19},"end":{"row":114,"column":20},"action":"insert","lines":["t"]},{"start":{"row":114,"column":20},"end":{"row":114,"column":21},"action":"insert","lines":["e"]},{"start":{"row":114,"column":21},"end":{"row":114,"column":22},"action":"insert","lines":[")"]}],[{"start":{"row":114,"column":21},"end":{"row":114,"column":22},"action":"remove","lines":[")"],"id":2886}],[{"start":{"row":114,"column":21},"end":{"row":114,"column":22},"action":"insert","lines":["_"],"id":2887},{"start":{"row":114,"column":22},"end":{"row":114,"column":23},"action":"insert","lines":["o"]},{"start":{"row":114,"column":23},"end":{"row":114,"column":24},"action":"insert","lines":["b"]},{"start":{"row":114,"column":24},"end":{"row":114,"column":25},"action":"insert","lines":["j"]}],[{"start":{"row":114,"column":25},"end":{"row":114,"column":27},"action":"insert","lines":["()"],"id":2888}],[{"start":{"row":114,"column":26},"end":{"row":114,"column":27},"action":"insert","lines":["r"],"id":2889},{"start":{"row":114,"column":27},"end":{"row":114,"column":28},"action":"insert","lines":["e"]},{"start":{"row":114,"column":28},"end":{"row":114,"column":29},"action":"insert","lines":["c"]},{"start":{"row":114,"column":29},"end":{"row":114,"column":30},"action":"insert","lines":["i"]},{"start":{"row":114,"column":30},"end":{"row":114,"column":31},"action":"insert","lines":["p"]},{"start":{"row":114,"column":31},"end":{"row":114,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":114,"column":33},"end":{"row":115,"column":0},"action":"insert","lines":["",""],"id":2890},{"start":{"row":115,"column":0},"end":{"row":115,"column":8},"action":"insert","lines":["        "]},{"start":{"row":115,"column":8},"end":{"row":115,"column":9},"action":"insert","lines":["r"]},{"start":{"row":115,"column":9},"end":{"row":115,"column":10},"action":"insert","lines":["e"]},{"start":{"row":115,"column":10},"end":{"row":115,"column":11},"action":"insert","lines":["c"]},{"start":{"row":115,"column":11},"end":{"row":115,"column":12},"action":"insert","lines":["i"]},{"start":{"row":115,"column":12},"end":{"row":115,"column":13},"action":"insert","lines":["p"]},{"start":{"row":115,"column":13},"end":{"row":115,"column":14},"action":"insert","lines":["e"]},{"start":{"row":115,"column":14},"end":{"row":115,"column":15},"action":"insert","lines":["."]}],[{"start":{"row":115,"column":15},"end":{"row":115,"column":16},"action":"insert","lines":["s"],"id":2891},{"start":{"row":115,"column":16},"end":{"row":115,"column":17},"action":"insert","lines":["a"]},{"start":{"row":115,"column":17},"end":{"row":115,"column":18},"action":"insert","lines":["v"]},{"start":{"row":115,"column":18},"end":{"row":115,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":115,"column":19},"end":{"row":115,"column":21},"action":"insert","lines":["()"],"id":2892}],[{"start":{"row":115,"column":21},"end":{"row":116,"column":0},"action":"insert","lines":["",""],"id":2893},{"start":{"row":116,"column":0},"end":{"row":116,"column":8},"action":"insert","lines":["        "]},{"start":{"row":116,"column":8},"end":{"row":116,"column":9},"action":"insert","lines":["e"]},{"start":{"row":116,"column":9},"end":{"row":116,"column":10},"action":"insert","lines":["d"]},{"start":{"row":116,"column":10},"end":{"row":116,"column":11},"action":"insert","lines":["i"]},{"start":{"row":116,"column":11},"end":{"row":116,"column":12},"action":"insert","lines":["r"]},{"start":{"row":116,"column":12},"end":{"row":116,"column":13},"action":"insert","lines":["e"]},{"start":{"row":116,"column":13},"end":{"row":116,"column":14},"action":"insert","lines":["c"]},{"start":{"row":116,"column":14},"end":{"row":116,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":116,"column":15},"end":{"row":116,"column":17},"action":"insert","lines":["()"],"id":2894}],[{"start":{"row":116,"column":16},"end":{"row":116,"column":18},"action":"insert","lines":["''"],"id":2895}],[{"start":{"row":116,"column":17},"end":{"row":116,"column":18},"action":"insert","lines":["e"],"id":2896},{"start":{"row":116,"column":18},"end":{"row":116,"column":19},"action":"insert","lines":["d"]},{"start":{"row":116,"column":19},"end":{"row":116,"column":20},"action":"insert","lines":["i"]},{"start":{"row":116,"column":20},"end":{"row":116,"column":21},"action":"insert","lines":["t"]},{"start":{"row":116,"column":21},"end":{"row":116,"column":22},"action":"insert","lines":["_"]},{"start":{"row":116,"column":22},"end":{"row":116,"column":23},"action":"insert","lines":["r"]},{"start":{"row":116,"column":23},"end":{"row":116,"column":24},"action":"insert","lines":["e"]},{"start":{"row":116,"column":24},"end":{"row":116,"column":25},"action":"insert","lines":["c"]}],[{"start":{"row":116,"column":25},"end":{"row":116,"column":26},"action":"insert","lines":["i"],"id":2897},{"start":{"row":116,"column":26},"end":{"row":116,"column":27},"action":"insert","lines":["p"]},{"start":{"row":116,"column":27},"end":{"row":116,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":116,"column":8},"end":{"row":116,"column":9},"action":"insert","lines":["r"],"id":2898}],[{"start":{"row":116,"column":8},"end":{"row":116,"column":31},"action":"remove","lines":["redirect('edit_recipe')"],"id":2899},{"start":{"row":116,"column":4},"end":{"row":116,"column":8},"action":"remove","lines":["    "]},{"start":{"row":116,"column":0},"end":{"row":116,"column":4},"action":"remove","lines":["    "]},{"start":{"row":115,"column":21},"end":{"row":116,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":116,"column":46},"end":{"row":116,"column":47},"action":"insert","lines":["f"],"id":2900},{"start":{"row":116,"column":47},"end":{"row":116,"column":48},"action":"insert","lines":["o"]},{"start":{"row":116,"column":48},"end":{"row":116,"column":49},"action":"insert","lines":["r"]},{"start":{"row":116,"column":49},"end":{"row":116,"column":50},"action":"insert","lines":["m"]},{"start":{"row":116,"column":50},"end":{"row":116,"column":51},"action":"insert","lines":["="]},{"start":{"row":116,"column":51},"end":{"row":116,"column":52},"action":"insert","lines":["f"]},{"start":{"row":116,"column":52},"end":{"row":116,"column":53},"action":"insert","lines":["o"]},{"start":{"row":116,"column":53},"end":{"row":116,"column":54},"action":"insert","lines":["r"]}],[{"start":{"row":116,"column":54},"end":{"row":116,"column":55},"action":"insert","lines":["m"],"id":2901},{"start":{"row":116,"column":55},"end":{"row":116,"column":56},"action":"insert","lines":[","]}],[{"start":{"row":116,"column":56},"end":{"row":116,"column":57},"action":"insert","lines":[" "],"id":2902}],[{"start":{"row":116,"column":55},"end":{"row":116,"column":120},"action":"remove","lines":[", recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})"],"id":2903},{"start":{"row":116,"column":54},"end":{"row":116,"column":55},"action":"remove","lines":["m"]}],[{"start":{"row":116,"column":54},"end":{"row":116,"column":55},"action":"insert","lines":["m"],"id":2904}],[{"start":{"row":110,"column":16},"end":{"row":110,"column":34},"action":"remove","lines":["recipe_id, request"],"id":2905},{"start":{"row":110,"column":16},"end":{"row":110,"column":17},"action":"insert","lines":["r"]},{"start":{"row":110,"column":17},"end":{"row":110,"column":18},"action":"insert","lines":["e"]},{"start":{"row":110,"column":18},"end":{"row":110,"column":19},"action":"insert","lines":["q"]},{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"insert","lines":["u"]},{"start":{"row":110,"column":20},"end":{"row":110,"column":21},"action":"insert","lines":["e"]},{"start":{"row":110,"column":21},"end":{"row":110,"column":22},"action":"insert","lines":["s"]},{"start":{"row":110,"column":22},"end":{"row":110,"column":23},"action":"insert","lines":["t"]},{"start":{"row":110,"column":23},"end":{"row":110,"column":24},"action":"insert","lines":[","]}],[{"start":{"row":110,"column":24},"end":{"row":110,"column":25},"action":"insert","lines":[" "],"id":2906},{"start":{"row":110,"column":25},"end":{"row":110,"column":26},"action":"insert","lines":["r"]},{"start":{"row":110,"column":26},"end":{"row":110,"column":27},"action":"insert","lines":["e"]},{"start":{"row":110,"column":27},"end":{"row":110,"column":28},"action":"insert","lines":["c"]},{"start":{"row":110,"column":28},"end":{"row":110,"column":29},"action":"insert","lines":["u"]},{"start":{"row":110,"column":29},"end":{"row":110,"column":30},"action":"insert","lines":["p"]},{"start":{"row":110,"column":30},"end":{"row":110,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":110,"column":30},"end":{"row":110,"column":31},"action":"remove","lines":["e"],"id":2907},{"start":{"row":110,"column":29},"end":{"row":110,"column":30},"action":"remove","lines":["p"]},{"start":{"row":110,"column":28},"end":{"row":110,"column":29},"action":"remove","lines":["u"]}],[{"start":{"row":110,"column":28},"end":{"row":110,"column":29},"action":"insert","lines":["i"],"id":2908},{"start":{"row":110,"column":29},"end":{"row":110,"column":30},"action":"insert","lines":["p"]},{"start":{"row":110,"column":30},"end":{"row":110,"column":31},"action":"insert","lines":["e"]},{"start":{"row":110,"column":31},"end":{"row":110,"column":32},"action":"insert","lines":["_"]},{"start":{"row":110,"column":32},"end":{"row":110,"column":33},"action":"insert","lines":["i"]},{"start":{"row":110,"column":33},"end":{"row":110,"column":34},"action":"insert","lines":["d"]}],[{"start":{"row":110,"column":16},"end":{"row":110,"column":24},"action":"remove","lines":["request,"],"id":2909}],[{"start":{"row":110,"column":16},"end":{"row":110,"column":17},"action":"remove","lines":[" "],"id":2910}],[{"start":{"row":112,"column":25},"end":{"row":112,"column":45},"action":"remove","lines":["request.POST, recipe"],"id":2912}],[{"start":{"row":114,"column":12},"end":{"row":115,"column":21},"action":"remove","lines":[".populate_obj(recipe)","        recipe.save()"],"id":2913},{"start":{"row":114,"column":12},"end":{"row":114,"column":13},"action":"insert","lines":[" "]},{"start":{"row":114,"column":13},"end":{"row":114,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":114,"column":14},"end":{"row":114,"column":15},"action":"insert","lines":[" "],"id":2914}],[{"start":{"row":114,"column":15},"end":{"row":114,"column":16},"action":"insert","lines":["A"],"id":2915},{"start":{"row":114,"column":16},"end":{"row":114,"column":17},"action":"insert","lines":["d"]}],[{"start":{"row":114,"column":15},"end":{"row":114,"column":17},"action":"remove","lines":["Ad"],"id":2916},{"start":{"row":114,"column":15},"end":{"row":114,"column":28},"action":"insert","lines":["AddRecipeForm"]}],[{"start":{"row":114,"column":28},"end":{"row":114,"column":30},"action":"insert","lines":["()"],"id":2917}],[{"start":{"row":114,"column":29},"end":{"row":114,"column":30},"action":"insert","lines":["d"],"id":2918},{"start":{"row":114,"column":30},"end":{"row":114,"column":31},"action":"insert","lines":["a"]},{"start":{"row":114,"column":31},"end":{"row":114,"column":32},"action":"insert","lines":["t"]},{"start":{"row":114,"column":32},"end":{"row":114,"column":33},"action":"insert","lines":["a"]}],[{"start":{"row":114,"column":33},"end":{"row":114,"column":34},"action":"insert","lines":["="],"id":2919},{"start":{"row":114,"column":34},"end":{"row":114,"column":35},"action":"insert","lines":["r"]},{"start":{"row":114,"column":35},"end":{"row":114,"column":36},"action":"insert","lines":["e"]},{"start":{"row":114,"column":36},"end":{"row":114,"column":37},"action":"insert","lines":["c"]},{"start":{"row":114,"column":37},"end":{"row":114,"column":38},"action":"insert","lines":["i"]},{"start":{"row":114,"column":38},"end":{"row":114,"column":39},"action":"insert","lines":["p"]},{"start":{"row":114,"column":39},"end":{"row":114,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":119,"column":3},"end":{"row":119,"column":38},"action":"remove","lines":[" form = AddRecipeForm(request.form)"],"id":2920},{"start":{"row":119,"column":2},"end":{"row":119,"column":3},"action":"remove","lines":[" "]},{"start":{"row":119,"column":1},"end":{"row":119,"column":2},"action":"remove","lines":[" "]},{"start":{"row":119,"column":0},"end":{"row":119,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":118,"column":29},"end":{"row":119,"column":0},"action":"remove","lines":["",""],"id":2921}],[{"start":{"row":115,"column":55},"end":{"row":115,"column":56},"action":"insert","lines":[","],"id":2922}],[{"start":{"row":115,"column":56},"end":{"row":115,"column":57},"action":"insert","lines":[" "],"id":2923},{"start":{"row":115,"column":57},"end":{"row":115,"column":58},"action":"insert","lines":["r"]},{"start":{"row":115,"column":58},"end":{"row":115,"column":59},"action":"insert","lines":["e"]},{"start":{"row":115,"column":59},"end":{"row":115,"column":60},"action":"insert","lines":["c"]},{"start":{"row":115,"column":60},"end":{"row":115,"column":61},"action":"insert","lines":["i"]},{"start":{"row":115,"column":61},"end":{"row":115,"column":62},"action":"insert","lines":["p"]},{"start":{"row":115,"column":62},"end":{"row":115,"column":63},"action":"insert","lines":["e"]}],[{"start":{"row":115,"column":63},"end":{"row":115,"column":64},"action":"insert","lines":["="],"id":2924},{"start":{"row":115,"column":64},"end":{"row":115,"column":65},"action":"insert","lines":["r"]},{"start":{"row":115,"column":65},"end":{"row":115,"column":66},"action":"insert","lines":["e"]},{"start":{"row":115,"column":66},"end":{"row":115,"column":67},"action":"insert","lines":["c"]},{"start":{"row":115,"column":67},"end":{"row":115,"column":68},"action":"insert","lines":["i"]},{"start":{"row":115,"column":68},"end":{"row":115,"column":69},"action":"insert","lines":["p"]},{"start":{"row":115,"column":69},"end":{"row":115,"column":70},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":1425,"scrollleft":0,"selection":{"start":{"row":122,"column":10},"end":{"row":122,"column":10},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567446325172,"hash":"f6778aaf96bfb86c913442d1e8f05e11da2861b6"}