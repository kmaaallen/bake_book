{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":96,"column":8},"end":{"row":96,"column":9},"action":"remove","lines":[" "],"id":3986}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":8},"action":"remove","lines":["    "],"id":3987}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":8},"action":"insert","lines":["    "],"id":3990}],[{"start":{"row":83,"column":0},"end":{"row":104,"column":91},"action":"remove","lines":["@app.route('/save_recipe/<recipe_id>', methods=['GET','POST'])","def save_recipe(recipe_id):","    \"\"\" debugging \"\"\"","    flash(\"got to save_recipe function\")","    \"\"\"Check user is logged in \"\"\"","    if 'logged_in' in session:","        flash(\"user is logged in\")","        recipe = ObjectId(recipe_id)","        flash(recipe)","        user = mongo.db.users.find_one({'user': session['username']})","        flash(\"user id is\" + user['user'])","        saved = user['saved_recipes']","        flash (saved)","        \"\"\"Check recipe is not already saved\"\"\"","        if recipe not in saved:","            flash(\"recipe not in saved\")","            mongo.db.users.update_one({'user': session['username']}, {\"$push\" : {\"saved_recipes\" : recipe}})","            flash (saved)","        else:","            flash(\"recipe is in saved\")","    return render_template('recipecard.html',","                           recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))"],"id":3991},{"start":{"row":83,"column":0},"end":{"row":104,"column":91},"action":"insert","lines":["@app.route('/save_recipe/<recipe_id>', methods=['GET', 'POST'])","def save_recipe(recipe_id):","    \"\"\" debugging \"\"\"","    flash(\"got to save_recipe function\")","    \"\"\"Check user is logged in \"\"\"","    if 'logged_in' in session:","        flash(\"user is logged in\")","        recipe = ObjectId(recipe_id)","        flash(recipe)","        user = mongo.db.users.find_one({'user': session['username']})","        flash(\"user id is\" + user['user'])","        saved = user['saved_recipes']","        flash(saved)","        \"\"\"Check recipe is not already saved\"\"\"","        if recipe not in saved:","            flash(\"recipe not in saved\")","            mongo.db.users.update_one({'user': session['username']}, {\"$push\": {\"saved_recipes\": recipe}})","            flash(saved)","        else:","            flash(\"recipe is in saved\")","    return render_template('recipecard.html',","                           recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))"]}],[{"start":{"row":111,"column":57},"end":{"row":111,"column":59},"action":"insert","lines":["{}"],"id":3992}],[{"start":{"row":111,"column":58},"end":{"row":111,"column":60},"action":"insert","lines":["''"],"id":3993}],[{"start":{"row":111,"column":59},"end":{"row":111,"column":60},"action":"insert","lines":["_"],"id":3994},{"start":{"row":111,"column":60},"end":{"row":111,"column":61},"action":"insert","lines":["i"]},{"start":{"row":111,"column":61},"end":{"row":111,"column":62},"action":"insert","lines":["d"]}],[{"start":{"row":111,"column":63},"end":{"row":111,"column":64},"action":"insert","lines":[":"],"id":3995}],[{"start":{"row":111,"column":64},"end":{"row":111,"column":65},"action":"insert","lines":[" "],"id":3996}],[{"start":{"row":111,"column":65},"end":{"row":111,"column":67},"action":"insert","lines":["{}"],"id":3997}],[{"start":{"row":111,"column":66},"end":{"row":111,"column":67},"action":"insert","lines":["&"],"id":3998}],[{"start":{"row":111,"column":66},"end":{"row":111,"column":67},"action":"remove","lines":["&"],"id":3999}],[{"start":{"row":111,"column":66},"end":{"row":111,"column":67},"action":"insert","lines":["$"],"id":4000},{"start":{"row":111,"column":67},"end":{"row":111,"column":68},"action":"insert","lines":["i"]},{"start":{"row":111,"column":68},"end":{"row":111,"column":69},"action":"insert","lines":["n"]},{"start":{"row":111,"column":69},"end":{"row":111,"column":70},"action":"insert","lines":[":"]}],[{"start":{"row":111,"column":70},"end":{"row":111,"column":71},"action":"insert","lines":[" "],"id":4001}],[{"start":{"row":111,"column":71},"end":{"row":111,"column":72},"action":"insert","lines":["s"],"id":4002},{"start":{"row":111,"column":72},"end":{"row":111,"column":73},"action":"insert","lines":["a"]},{"start":{"row":111,"column":73},"end":{"row":111,"column":74},"action":"insert","lines":["v"]},{"start":{"row":111,"column":74},"end":{"row":111,"column":75},"action":"insert","lines":["e"]},{"start":{"row":111,"column":75},"end":{"row":111,"column":76},"action":"insert","lines":["d"]}],[{"start":{"row":109,"column":75},"end":{"row":110,"column":0},"action":"insert","lines":["",""],"id":4003},{"start":{"row":110,"column":0},"end":{"row":110,"column":8},"action":"insert","lines":["        "]},{"start":{"row":110,"column":8},"end":{"row":110,"column":9},"action":"insert","lines":["s"]},{"start":{"row":110,"column":9},"end":{"row":110,"column":10},"action":"insert","lines":["a"]},{"start":{"row":110,"column":10},"end":{"row":110,"column":11},"action":"insert","lines":["v"]},{"start":{"row":110,"column":11},"end":{"row":110,"column":12},"action":"insert","lines":["e"]},{"start":{"row":110,"column":12},"end":{"row":110,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":110,"column":13},"end":{"row":110,"column":14},"action":"insert","lines":[" "],"id":4004},{"start":{"row":110,"column":14},"end":{"row":110,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":110,"column":15},"end":{"row":110,"column":16},"action":"insert","lines":[" "],"id":4005},{"start":{"row":110,"column":16},"end":{"row":110,"column":17},"action":"insert","lines":["u"]},{"start":{"row":110,"column":17},"end":{"row":110,"column":18},"action":"insert","lines":["s"]},{"start":{"row":110,"column":18},"end":{"row":110,"column":19},"action":"insert","lines":["e"]},{"start":{"row":110,"column":19},"end":{"row":110,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":110,"column":8},"end":{"row":110,"column":20},"action":"remove","lines":["saved = user"],"id":4006},{"start":{"row":110,"column":8},"end":{"row":112,"column":37},"action":"insert","lines":["user = mongo.db.users.find_one({'user': session['username']})","        flash(\"user id is\" + user['user'])","        saved = user['saved_recipes']"]}],[{"start":{"row":111,"column":8},"end":{"row":111,"column":42},"action":"remove","lines":["flash(\"user id is\" + user['user'])"],"id":4007},{"start":{"row":111,"column":4},"end":{"row":111,"column":8},"action":"remove","lines":["    "]},{"start":{"row":111,"column":0},"end":{"row":111,"column":4},"action":"remove","lines":["    "]},{"start":{"row":110,"column":69},"end":{"row":111,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":113,"column":66},"end":{"row":113,"column":67},"action":"insert","lines":["\""],"id":4008}],[{"start":{"row":113,"column":70},"end":{"row":113,"column":71},"action":"insert","lines":["\""],"id":4009}],[{"start":{"row":113,"column":82},"end":{"row":114,"column":0},"action":"insert","lines":["",""],"id":4010},{"start":{"row":114,"column":0},"end":{"row":114,"column":27},"action":"insert","lines":["                           "]}],[{"start":{"row":114,"column":26},"end":{"row":114,"column":27},"action":"remove","lines":[" "],"id":4011},{"start":{"row":114,"column":25},"end":{"row":114,"column":26},"action":"remove","lines":[" "]},{"start":{"row":114,"column":24},"end":{"row":114,"column":25},"action":"remove","lines":[" "]},{"start":{"row":114,"column":20},"end":{"row":114,"column":24},"action":"remove","lines":["    "]},{"start":{"row":114,"column":16},"end":{"row":114,"column":20},"action":"remove","lines":["    "]},{"start":{"row":114,"column":12},"end":{"row":114,"column":16},"action":"remove","lines":["    "]}],[{"start":{"row":114,"column":8},"end":{"row":114,"column":12},"action":"remove","lines":["    "],"id":4012}],[{"start":{"row":112,"column":32},"end":{"row":112,"column":39},"action":"remove","lines":["recipes"],"id":4013},{"start":{"row":112,"column":32},"end":{"row":112,"column":33},"action":"insert","lines":["s"]},{"start":{"row":112,"column":33},"end":{"row":112,"column":34},"action":"insert","lines":["a"]},{"start":{"row":112,"column":34},"end":{"row":112,"column":35},"action":"insert","lines":["v"]},{"start":{"row":112,"column":35},"end":{"row":112,"column":36},"action":"insert","lines":["e"]},{"start":{"row":112,"column":36},"end":{"row":112,"column":37},"action":"insert","lines":["d"]}],[{"start":{"row":112,"column":37},"end":{"row":112,"column":38},"action":"insert","lines":["r"],"id":4014},{"start":{"row":112,"column":38},"end":{"row":112,"column":39},"action":"insert","lines":["e"]},{"start":{"row":112,"column":39},"end":{"row":112,"column":40},"action":"insert","lines":["c"]},{"start":{"row":112,"column":40},"end":{"row":112,"column":41},"action":"insert","lines":["i"]},{"start":{"row":112,"column":41},"end":{"row":112,"column":42},"action":"insert","lines":["p"]},{"start":{"row":112,"column":42},"end":{"row":112,"column":43},"action":"insert","lines":["e"]},{"start":{"row":112,"column":43},"end":{"row":112,"column":44},"action":"insert","lines":["s"]}],[{"start":{"row":113,"column":82},"end":{"row":114,"column":0},"action":"insert","lines":["",""],"id":4015},{"start":{"row":114,"column":0},"end":{"row":114,"column":27},"action":"insert","lines":["                           "]}],[{"start":{"row":114,"column":26},"end":{"row":114,"column":27},"action":"remove","lines":[" "],"id":4016},{"start":{"row":114,"column":25},"end":{"row":114,"column":26},"action":"remove","lines":[" "]},{"start":{"row":114,"column":24},"end":{"row":114,"column":25},"action":"remove","lines":[" "]},{"start":{"row":114,"column":20},"end":{"row":114,"column":24},"action":"remove","lines":["    "]},{"start":{"row":114,"column":16},"end":{"row":114,"column":20},"action":"remove","lines":["    "]},{"start":{"row":114,"column":12},"end":{"row":114,"column":16},"action":"remove","lines":["    "]},{"start":{"row":114,"column":8},"end":{"row":114,"column":12},"action":"remove","lines":["    "]},{"start":{"row":114,"column":4},"end":{"row":114,"column":8},"action":"remove","lines":["    "]},{"start":{"row":114,"column":0},"end":{"row":114,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":114,"column":0},"end":{"row":115,"column":0},"action":"insert","lines":["",""],"id":4017},{"start":{"row":115,"column":0},"end":{"row":115,"column":1},"action":"insert","lines":["@"]},{"start":{"row":115,"column":1},"end":{"row":115,"column":2},"action":"insert","lines":["a"]},{"start":{"row":115,"column":2},"end":{"row":115,"column":3},"action":"insert","lines":["p"]},{"start":{"row":115,"column":3},"end":{"row":115,"column":4},"action":"insert","lines":["p"]}],[{"start":{"row":115,"column":4},"end":{"row":115,"column":5},"action":"insert","lines":["."],"id":4018},{"start":{"row":115,"column":5},"end":{"row":115,"column":6},"action":"insert","lines":["r"]},{"start":{"row":115,"column":6},"end":{"row":115,"column":7},"action":"insert","lines":["o"]},{"start":{"row":115,"column":7},"end":{"row":115,"column":8},"action":"insert","lines":["u"]},{"start":{"row":115,"column":8},"end":{"row":115,"column":9},"action":"insert","lines":["t"]},{"start":{"row":115,"column":9},"end":{"row":115,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":115,"column":10},"end":{"row":115,"column":12},"action":"insert","lines":["()"],"id":4019}],[{"start":{"row":115,"column":11},"end":{"row":115,"column":13},"action":"insert","lines":["''"],"id":4020}],[{"start":{"row":115,"column":12},"end":{"row":115,"column":13},"action":"insert","lines":["/"],"id":4021},{"start":{"row":115,"column":13},"end":{"row":115,"column":14},"action":"insert","lines":["u"]},{"start":{"row":115,"column":14},"end":{"row":115,"column":15},"action":"insert","lines":["n"]},{"start":{"row":115,"column":15},"end":{"row":115,"column":16},"action":"insert","lines":["s"]},{"start":{"row":115,"column":16},"end":{"row":115,"column":17},"action":"insert","lines":["a"]},{"start":{"row":115,"column":17},"end":{"row":115,"column":18},"action":"insert","lines":["v"]},{"start":{"row":115,"column":18},"end":{"row":115,"column":19},"action":"insert","lines":["e"]},{"start":{"row":115,"column":19},"end":{"row":115,"column":20},"action":"insert","lines":["_"]}],[{"start":{"row":115,"column":20},"end":{"row":115,"column":21},"action":"insert","lines":["r"],"id":4022},{"start":{"row":115,"column":21},"end":{"row":115,"column":22},"action":"insert","lines":["e"]},{"start":{"row":115,"column":22},"end":{"row":115,"column":23},"action":"insert","lines":["c"]},{"start":{"row":115,"column":23},"end":{"row":115,"column":24},"action":"insert","lines":["i"]},{"start":{"row":115,"column":24},"end":{"row":115,"column":25},"action":"insert","lines":["p"]},{"start":{"row":115,"column":25},"end":{"row":115,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":115,"column":26},"end":{"row":115,"column":27},"action":"insert","lines":["/"],"id":4023},{"start":{"row":115,"column":27},"end":{"row":115,"column":28},"action":"insert","lines":[">"]}],[{"start":{"row":115,"column":27},"end":{"row":115,"column":28},"action":"remove","lines":[">"],"id":4024}],[{"start":{"row":115,"column":27},"end":{"row":115,"column":28},"action":"insert","lines":["<"],"id":4025},{"start":{"row":115,"column":28},"end":{"row":115,"column":29},"action":"insert","lines":["r"]},{"start":{"row":115,"column":29},"end":{"row":115,"column":30},"action":"insert","lines":["e"]},{"start":{"row":115,"column":30},"end":{"row":115,"column":31},"action":"insert","lines":["c"]},{"start":{"row":115,"column":31},"end":{"row":115,"column":32},"action":"insert","lines":["i"]},{"start":{"row":115,"column":32},"end":{"row":115,"column":33},"action":"insert","lines":["p"]},{"start":{"row":115,"column":33},"end":{"row":115,"column":34},"action":"insert","lines":["e"]},{"start":{"row":115,"column":34},"end":{"row":115,"column":35},"action":"insert","lines":["_"]},{"start":{"row":115,"column":35},"end":{"row":115,"column":36},"action":"insert","lines":["i"]},{"start":{"row":115,"column":36},"end":{"row":115,"column":37},"action":"insert","lines":["d"]},{"start":{"row":115,"column":37},"end":{"row":115,"column":38},"action":"insert","lines":[">"]}],[{"start":{"row":115,"column":39},"end":{"row":115,"column":40},"action":"insert","lines":[","],"id":4026}],[{"start":{"row":115,"column":40},"end":{"row":115,"column":41},"action":"insert","lines":[" "],"id":4027},{"start":{"row":115,"column":41},"end":{"row":115,"column":42},"action":"insert","lines":["m"]},{"start":{"row":115,"column":42},"end":{"row":115,"column":43},"action":"insert","lines":["e"]},{"start":{"row":115,"column":43},"end":{"row":115,"column":44},"action":"insert","lines":["t"]},{"start":{"row":115,"column":44},"end":{"row":115,"column":45},"action":"insert","lines":["h"]},{"start":{"row":115,"column":45},"end":{"row":115,"column":46},"action":"insert","lines":["o"]},{"start":{"row":115,"column":46},"end":{"row":115,"column":47},"action":"insert","lines":["d"]},{"start":{"row":115,"column":47},"end":{"row":115,"column":48},"action":"insert","lines":["s"]}],[{"start":{"row":115,"column":48},"end":{"row":115,"column":49},"action":"insert","lines":["="],"id":4028}],[{"start":{"row":115,"column":49},"end":{"row":115,"column":51},"action":"insert","lines":["[]"],"id":4029}],[{"start":{"row":115,"column":50},"end":{"row":115,"column":52},"action":"insert","lines":["''"],"id":4030}],[{"start":{"row":115,"column":51},"end":{"row":115,"column":52},"action":"insert","lines":["G"],"id":4031},{"start":{"row":115,"column":52},"end":{"row":115,"column":53},"action":"insert","lines":["E"]},{"start":{"row":115,"column":53},"end":{"row":115,"column":54},"action":"insert","lines":["T"]}],[{"start":{"row":115,"column":55},"end":{"row":115,"column":56},"action":"insert","lines":[","],"id":4032}],[{"start":{"row":115,"column":56},"end":{"row":115,"column":57},"action":"insert","lines":[" "],"id":4033}],[{"start":{"row":115,"column":57},"end":{"row":115,"column":59},"action":"insert","lines":["''"],"id":4034}],[{"start":{"row":115,"column":58},"end":{"row":115,"column":59},"action":"insert","lines":["P"],"id":4035},{"start":{"row":115,"column":59},"end":{"row":115,"column":60},"action":"insert","lines":["O"]},{"start":{"row":115,"column":60},"end":{"row":115,"column":61},"action":"insert","lines":["S"]},{"start":{"row":115,"column":61},"end":{"row":115,"column":62},"action":"insert","lines":["T"]}],[{"start":{"row":115,"column":63},"end":{"row":115,"column":64},"action":"insert","lines":["}"],"id":4036}],[{"start":{"row":115,"column":63},"end":{"row":115,"column":64},"action":"remove","lines":["}"],"id":4037}],[{"start":{"row":115,"column":65},"end":{"row":116,"column":0},"action":"insert","lines":["",""],"id":4038},{"start":{"row":116,"column":0},"end":{"row":116,"column":1},"action":"insert","lines":["d"]},{"start":{"row":116,"column":1},"end":{"row":116,"column":2},"action":"insert","lines":["e"]},{"start":{"row":116,"column":2},"end":{"row":116,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":116,"column":3},"end":{"row":116,"column":4},"action":"insert","lines":[" "],"id":4039},{"start":{"row":116,"column":4},"end":{"row":116,"column":5},"action":"insert","lines":["u"]},{"start":{"row":116,"column":5},"end":{"row":116,"column":6},"action":"insert","lines":["n"]},{"start":{"row":116,"column":6},"end":{"row":116,"column":7},"action":"insert","lines":["s"]},{"start":{"row":116,"column":7},"end":{"row":116,"column":8},"action":"insert","lines":["a"]},{"start":{"row":116,"column":8},"end":{"row":116,"column":9},"action":"insert","lines":["v"]},{"start":{"row":116,"column":9},"end":{"row":116,"column":10},"action":"insert","lines":["e"]},{"start":{"row":116,"column":10},"end":{"row":116,"column":11},"action":"insert","lines":["_"]},{"start":{"row":116,"column":11},"end":{"row":116,"column":12},"action":"insert","lines":["r"]},{"start":{"row":116,"column":12},"end":{"row":116,"column":13},"action":"insert","lines":["e"]},{"start":{"row":116,"column":13},"end":{"row":116,"column":14},"action":"insert","lines":["c"]}],[{"start":{"row":116,"column":14},"end":{"row":116,"column":15},"action":"insert","lines":["i"],"id":4040},{"start":{"row":116,"column":15},"end":{"row":116,"column":16},"action":"insert","lines":["p"]},{"start":{"row":116,"column":16},"end":{"row":116,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":116,"column":17},"end":{"row":116,"column":19},"action":"insert","lines":["()"],"id":4041}],[{"start":{"row":116,"column":19},"end":{"row":116,"column":20},"action":"insert","lines":[":"],"id":4042}],[{"start":{"row":116,"column":20},"end":{"row":117,"column":0},"action":"insert","lines":["",""],"id":4043},{"start":{"row":117,"column":0},"end":{"row":117,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":117,"column":4},"end":{"row":122,"column":82},"action":"insert","lines":["if 'logged_in' in session:","        \"\"\" returning show recipes template for now while I fix dropdown\"\"\"","        user = mongo.db.users.find_one({'user': session['username']})","        saved = user['saved_recipes']","        return render_template('savedrecipes.html',","                           recipes=mongo.db.recipes.find({'_id': {\"$in\": saved}}))"],"id":4044}],[{"start":{"row":109,"column":0},"end":{"row":109,"column":75},"action":"remove","lines":["        \"\"\" returning show recipes template for now while I fix dropdown\"\"\""],"id":4045},{"start":{"row":108,"column":30},"end":{"row":109,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":117,"column":0},"end":{"row":117,"column":75},"action":"remove","lines":["        \"\"\" returning show recipes template for now while I fix dropdown\"\"\""],"id":4046},{"start":{"row":116,"column":30},"end":{"row":117,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":118,"column":37},"end":{"row":119,"column":0},"action":"insert","lines":["",""],"id":4047},{"start":{"row":119,"column":0},"end":{"row":119,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":119,"column":8},"end":{"row":119,"column":9},"action":"insert","lines":["s"],"id":4048},{"start":{"row":119,"column":9},"end":{"row":119,"column":10},"action":"insert","lines":["a"]},{"start":{"row":119,"column":10},"end":{"row":119,"column":11},"action":"insert","lines":["v"]},{"start":{"row":119,"column":11},"end":{"row":119,"column":12},"action":"insert","lines":["e"]},{"start":{"row":119,"column":12},"end":{"row":119,"column":13},"action":"insert","lines":["d"]},{"start":{"row":119,"column":13},"end":{"row":119,"column":14},"action":"insert","lines":["."]},{"start":{"row":119,"column":14},"end":{"row":119,"column":15},"action":"insert","lines":["r"]},{"start":{"row":119,"column":15},"end":{"row":119,"column":16},"action":"insert","lines":["e"]},{"start":{"row":119,"column":16},"end":{"row":119,"column":17},"action":"insert","lines":["m"]}],[{"start":{"row":119,"column":17},"end":{"row":119,"column":18},"action":"insert","lines":["o"],"id":4049},{"start":{"row":119,"column":18},"end":{"row":119,"column":19},"action":"insert","lines":["v"]},{"start":{"row":119,"column":19},"end":{"row":119,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":119,"column":14},"end":{"row":119,"column":20},"action":"remove","lines":["remove"],"id":4050},{"start":{"row":119,"column":14},"end":{"row":119,"column":50},"action":"insert","lines":["remove({'_id': ObjectId(recipe_id)})"]}],[{"start":{"row":119,"column":22},"end":{"row":119,"column":29},"action":"remove","lines":["'_id': "],"id":4051}],[{"start":{"row":115,"column":18},"end":{"row":115,"column":19},"action":"insert","lines":["r"],"id":4052},{"start":{"row":115,"column":19},"end":{"row":115,"column":20},"action":"insert","lines":["e"]},{"start":{"row":115,"column":20},"end":{"row":115,"column":21},"action":"insert","lines":["c"]},{"start":{"row":115,"column":21},"end":{"row":115,"column":22},"action":"insert","lines":["i"]},{"start":{"row":115,"column":22},"end":{"row":115,"column":23},"action":"insert","lines":["p"]},{"start":{"row":115,"column":23},"end":{"row":115,"column":24},"action":"insert","lines":["e"]},{"start":{"row":115,"column":24},"end":{"row":115,"column":25},"action":"insert","lines":["_"]},{"start":{"row":115,"column":25},"end":{"row":115,"column":26},"action":"insert","lines":["i"]},{"start":{"row":115,"column":26},"end":{"row":115,"column":27},"action":"insert","lines":["d"]}],[{"start":{"row":119,"column":22},"end":{"row":119,"column":30},"action":"remove","lines":["ObjectId"],"id":4053}],[{"start":{"row":119,"column":22},"end":{"row":119,"column":23},"action":"remove","lines":["("],"id":4054}],[{"start":{"row":119,"column":31},"end":{"row":119,"column":32},"action":"remove","lines":[")"],"id":4055}],[{"start":{"row":119,"column":31},"end":{"row":119,"column":32},"action":"remove","lines":["}"],"id":4056}],[{"start":{"row":119,"column":21},"end":{"row":119,"column":22},"action":"remove","lines":["{"],"id":4057}],[{"start":{"row":118,"column":37},"end":{"row":119,"column":0},"action":"insert","lines":["",""],"id":4058},{"start":{"row":119,"column":0},"end":{"row":119,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":119,"column":8},"end":{"row":119,"column":35},"action":"insert","lines":["flash(\"recipe is in saved\")"],"id":4059}],[{"start":{"row":119,"column":14},"end":{"row":119,"column":34},"action":"remove","lines":["\"recipe is in saved\""],"id":4060},{"start":{"row":119,"column":14},"end":{"row":119,"column":15},"action":"insert","lines":["s"]},{"start":{"row":119,"column":15},"end":{"row":119,"column":16},"action":"insert","lines":["a"]},{"start":{"row":119,"column":16},"end":{"row":119,"column":17},"action":"insert","lines":["v"]},{"start":{"row":119,"column":17},"end":{"row":119,"column":18},"action":"insert","lines":["e"]},{"start":{"row":119,"column":18},"end":{"row":119,"column":19},"action":"insert","lines":["d"]}],[{"start":{"row":120,"column":21},"end":{"row":120,"column":22},"action":"insert","lines":["O"],"id":4061},{"start":{"row":120,"column":22},"end":{"row":120,"column":23},"action":"insert","lines":["b"]},{"start":{"row":120,"column":23},"end":{"row":120,"column":24},"action":"insert","lines":["j"]},{"start":{"row":120,"column":24},"end":{"row":120,"column":25},"action":"insert","lines":["e"]},{"start":{"row":120,"column":25},"end":{"row":120,"column":26},"action":"insert","lines":["c"]},{"start":{"row":120,"column":26},"end":{"row":120,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":120,"column":27},"end":{"row":120,"column":28},"action":"insert","lines":["I"],"id":4062},{"start":{"row":120,"column":28},"end":{"row":120,"column":29},"action":"insert","lines":["d"]}],[{"start":{"row":120,"column":29},"end":{"row":120,"column":30},"action":"insert","lines":["("],"id":4063}],[{"start":{"row":120,"column":39},"end":{"row":120,"column":40},"action":"insert","lines":[")"],"id":4064}],[{"start":{"row":119,"column":20},"end":{"row":120,"column":0},"action":"insert","lines":["",""],"id":4065},{"start":{"row":120,"column":0},"end":{"row":120,"column":8},"action":"insert","lines":["        "]},{"start":{"row":120,"column":8},"end":{"row":120,"column":9},"action":"insert","lines":["f"]},{"start":{"row":120,"column":9},"end":{"row":120,"column":10},"action":"insert","lines":["l"]},{"start":{"row":120,"column":10},"end":{"row":120,"column":11},"action":"insert","lines":["a"]},{"start":{"row":120,"column":11},"end":{"row":120,"column":12},"action":"insert","lines":["s"]},{"start":{"row":120,"column":12},"end":{"row":120,"column":13},"action":"insert","lines":["h"]}],[{"start":{"row":120,"column":13},"end":{"row":120,"column":15},"action":"insert","lines":["()"],"id":4066}],[{"start":{"row":120,"column":14},"end":{"row":120,"column":15},"action":"insert","lines":["@"],"id":4067},{"start":{"row":120,"column":15},"end":{"row":120,"column":16},"action":"insert","lines":["r"]},{"start":{"row":120,"column":16},"end":{"row":120,"column":17},"action":"insert","lines":["e"]},{"start":{"row":120,"column":17},"end":{"row":120,"column":18},"action":"insert","lines":["c"]},{"start":{"row":120,"column":18},"end":{"row":120,"column":19},"action":"insert","lines":["i"]},{"start":{"row":120,"column":19},"end":{"row":120,"column":20},"action":"insert","lines":["p"]}],[{"start":{"row":120,"column":19},"end":{"row":120,"column":20},"action":"remove","lines":["p"],"id":4068},{"start":{"row":120,"column":18},"end":{"row":120,"column":19},"action":"remove","lines":["i"]},{"start":{"row":120,"column":17},"end":{"row":120,"column":18},"action":"remove","lines":["c"]},{"start":{"row":120,"column":16},"end":{"row":120,"column":17},"action":"remove","lines":["e"]},{"start":{"row":120,"column":15},"end":{"row":120,"column":16},"action":"remove","lines":["r"]},{"start":{"row":120,"column":14},"end":{"row":120,"column":15},"action":"remove","lines":["@"]}],[{"start":{"row":120,"column":14},"end":{"row":120,"column":16},"action":"insert","lines":["\"\""],"id":4069}],[{"start":{"row":120,"column":15},"end":{"row":120,"column":16},"action":"insert","lines":["r"],"id":4070},{"start":{"row":120,"column":16},"end":{"row":120,"column":17},"action":"insert","lines":["e"]},{"start":{"row":120,"column":17},"end":{"row":120,"column":18},"action":"insert","lines":["c"]},{"start":{"row":120,"column":18},"end":{"row":120,"column":19},"action":"insert","lines":["i"]},{"start":{"row":120,"column":19},"end":{"row":120,"column":20},"action":"insert","lines":["p"]},{"start":{"row":120,"column":20},"end":{"row":120,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":120,"column":21},"end":{"row":120,"column":22},"action":"insert","lines":[" "],"id":4071},{"start":{"row":120,"column":22},"end":{"row":120,"column":23},"action":"insert","lines":["i"]},{"start":{"row":120,"column":23},"end":{"row":120,"column":24},"action":"insert","lines":["d"]}],[{"start":{"row":120,"column":24},"end":{"row":120,"column":25},"action":"insert","lines":[" "],"id":4072},{"start":{"row":120,"column":25},"end":{"row":120,"column":26},"action":"insert","lines":["i"]},{"start":{"row":120,"column":26},"end":{"row":120,"column":27},"action":"insert","lines":["s"]}],[{"start":{"row":120,"column":28},"end":{"row":120,"column":29},"action":"insert","lines":[" "],"id":4073},{"start":{"row":120,"column":29},"end":{"row":120,"column":30},"action":"insert","lines":["+"]}],[{"start":{"row":120,"column":30},"end":{"row":120,"column":31},"action":"insert","lines":[" "],"id":4074},{"start":{"row":120,"column":31},"end":{"row":120,"column":32},"action":"insert","lines":["r"]},{"start":{"row":120,"column":32},"end":{"row":120,"column":33},"action":"insert","lines":["e"]},{"start":{"row":120,"column":33},"end":{"row":120,"column":34},"action":"insert","lines":["c"]},{"start":{"row":120,"column":34},"end":{"row":120,"column":35},"action":"insert","lines":["i"]},{"start":{"row":120,"column":35},"end":{"row":120,"column":36},"action":"insert","lines":["p"]},{"start":{"row":120,"column":36},"end":{"row":120,"column":37},"action":"insert","lines":["e"]},{"start":{"row":120,"column":37},"end":{"row":120,"column":38},"action":"insert","lines":["_"]},{"start":{"row":120,"column":38},"end":{"row":120,"column":39},"action":"insert","lines":["i"]},{"start":{"row":120,"column":39},"end":{"row":120,"column":40},"action":"insert","lines":["d"]}],[{"start":{"row":121,"column":29},"end":{"row":121,"column":30},"action":"insert","lines":["+"],"id":4075}],[{"start":{"row":121,"column":29},"end":{"row":121,"column":30},"action":"insert","lines":["'"],"id":4076}],[{"start":{"row":121,"column":21},"end":{"row":121,"column":22},"action":"insert","lines":["'"],"id":4077}],[{"start":{"row":121,"column":32},"end":{"row":121,"column":33},"action":"insert","lines":["'"],"id":4078}],[{"start":{"row":121,"column":34},"end":{"row":121,"column":35},"action":"insert","lines":["'"],"id":4079}],[{"start":{"row":121,"column":34},"end":{"row":121,"column":35},"action":"insert","lines":["\""],"id":4080}],[{"start":{"row":121,"column":36},"end":{"row":121,"column":37},"action":"insert","lines":["+"],"id":4081}],[{"start":{"row":121,"column":37},"end":{"row":121,"column":38},"action":"insert","lines":[" "],"id":4082}],[{"start":{"row":121,"column":47},"end":{"row":121,"column":48},"action":"insert","lines":[" "],"id":4083},{"start":{"row":121,"column":48},"end":{"row":121,"column":49},"action":"insert","lines":["+"]}],[{"start":{"row":121,"column":49},"end":{"row":121,"column":50},"action":"insert","lines":[" "],"id":4084}],[{"start":{"row":121,"column":50},"end":{"row":121,"column":52},"action":"insert","lines":["''"],"id":4085}],[{"start":{"row":121,"column":51},"end":{"row":121,"column":52},"action":"insert","lines":["\""],"id":4086}],[{"start":{"row":121,"column":52},"end":{"row":121,"column":53},"action":"remove","lines":["'"],"id":4087}],[{"start":{"row":121,"column":53},"end":{"row":121,"column":54},"action":"insert","lines":["'"],"id":4088}]]},"ace":{"folds":[],"scrolltop":1188,"scrollleft":0,"selection":{"start":{"row":121,"column":55},"end":{"row":121,"column":55},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":83,"state":"start","mode":"ace/mode/python"}},"timestamp":1568053501821,"hash":"9fcf5e12af9d875e553d81096826c85cbb45cf7a"}