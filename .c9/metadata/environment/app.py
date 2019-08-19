{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":4,"column":0},"end":{"row":4,"column":14},"action":"remove","lines":["import pymongo"],"id":387}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["p"],"id":388}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["P"],"id":389}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["m"],"id":390}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["M"],"id":391}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":20},"action":"remove","lines":["mongo = PyMongo(app)"],"id":392}],[{"start":{"row":12,"column":37},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":393},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":20},"action":"insert","lines":["mongo = PyMongo(app)"],"id":394}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["-"],"id":395},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["_"]}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":396}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":71},"action":"insert","lines":["app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')"],"id":400}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":8},"action":"remove","lines":["DBS_NAME"],"id":401}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":24},"action":"remove","lines":["MONGO_DBNAME"],"id":402},{"start":{"row":9,"column":12},"end":{"row":9,"column":20},"action":"insert","lines":["DBS_NAME"]}],[{"start":{"row":13,"column":3},"end":{"row":13,"column":22},"action":"remove","lines":["\"bakingBookRecipes\""],"id":403}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":39},"action":"remove","lines":["'task_manager'"],"id":404},{"start":{"row":9,"column":25},"end":{"row":9,"column":44},"action":"insert","lines":["\"bakingBookRecipes\""]}],[{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["d"],"id":405},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["b"]}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"remove","lines":["b"],"id":406},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"remove","lines":["d"]}],[{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["D"],"id":407},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["B"]}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":23},"action":"remove","lines":["MONGODB_URI"],"id":408},{"start":{"row":10,"column":12},"end":{"row":10,"column":23},"action":"insert","lines":["MONGODB_URI"]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":59},"action":"remove","lines":["MONGODB_URI = os.getenv('MONGO_URI', 'mongodb://localhost')"],"id":409}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":[" "],"id":410},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":["="]},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":[" "]},{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":37},"action":"remove","lines":["","COLLECTION_NAME = 'bakingBookRecipes'"],"id":411},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"remove","lines":["B"],"id":412},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"remove","lines":["D"]}],[{"start":{"row":18,"column":43},"end":{"row":18,"column":60},"action":"remove","lines":["bakingBookRecipes"],"id":413},{"start":{"row":18,"column":43},"end":{"row":18,"column":44},"action":"insert","lines":["r"]},{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"insert","lines":["e"]},{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"insert","lines":["c"]},{"start":{"row":18,"column":46},"end":{"row":18,"column":47},"action":"insert","lines":["i"]},{"start":{"row":18,"column":47},"end":{"row":18,"column":48},"action":"insert","lines":["p"]},{"start":{"row":18,"column":48},"end":{"row":18,"column":49},"action":"insert","lines":["e"]},{"start":{"row":18,"column":49},"end":{"row":18,"column":50},"action":"insert","lines":["s"]}],[{"start":{"row":18,"column":43},"end":{"row":18,"column":50},"action":"remove","lines":["recipes"],"id":414},{"start":{"row":18,"column":43},"end":{"row":18,"column":44},"action":"insert","lines":["b"]},{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"insert","lines":["a"]},{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"insert","lines":["k"]},{"start":{"row":18,"column":46},"end":{"row":18,"column":47},"action":"insert","lines":["i"]},{"start":{"row":18,"column":47},"end":{"row":18,"column":48},"action":"insert","lines":["n"]},{"start":{"row":18,"column":48},"end":{"row":18,"column":49},"action":"insert","lines":["g"]},{"start":{"row":18,"column":49},"end":{"row":18,"column":50},"action":"insert","lines":["B"]},{"start":{"row":18,"column":50},"end":{"row":18,"column":51},"action":"insert","lines":["o"]},{"start":{"row":18,"column":51},"end":{"row":18,"column":52},"action":"insert","lines":["o"]},{"start":{"row":18,"column":52},"end":{"row":18,"column":53},"action":"insert","lines":["k"]},{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"insert","lines":["R"]},{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"insert","lines":["c"],"id":415},{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"insert","lines":["i"]},{"start":{"row":18,"column":57},"end":{"row":18,"column":58},"action":"insert","lines":["p"]},{"start":{"row":18,"column":58},"end":{"row":18,"column":59},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":43},"end":{"row":18,"column":59},"action":"remove","lines":["bakingBookRecipe"],"id":416},{"start":{"row":18,"column":43},"end":{"row":18,"column":60},"action":"insert","lines":["bakingBookRecipes"]}],[{"start":{"row":18,"column":60},"end":{"row":18,"column":61},"action":"insert","lines":[" "],"id":417}],[{"start":{"row":18,"column":62},"end":{"row":18,"column":63},"action":"insert","lines":[" "],"id":418}],[{"start":{"row":18,"column":70},"end":{"row":18,"column":71},"action":"remove","lines":["b"],"id":419},{"start":{"row":18,"column":69},"end":{"row":18,"column":70},"action":"remove","lines":["d"]},{"start":{"row":18,"column":68},"end":{"row":18,"column":69},"action":"remove","lines":["."]}],[{"start":{"row":18,"column":43},"end":{"row":18,"column":60},"action":"remove","lines":["bakingBookRecipes"],"id":420},{"start":{"row":18,"column":43},"end":{"row":18,"column":44},"action":"insert","lines":["r"]},{"start":{"row":18,"column":44},"end":{"row":18,"column":45},"action":"insert","lines":["e"]},{"start":{"row":18,"column":45},"end":{"row":18,"column":46},"action":"insert","lines":["c"]},{"start":{"row":18,"column":46},"end":{"row":18,"column":47},"action":"insert","lines":["i"]},{"start":{"row":18,"column":47},"end":{"row":18,"column":48},"action":"insert","lines":["p"]},{"start":{"row":18,"column":48},"end":{"row":18,"column":49},"action":"insert","lines":["e"]},{"start":{"row":18,"column":49},"end":{"row":18,"column":50},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":49},"end":{"row":18,"column":50},"action":"remove","lines":["d"],"id":421}],[{"start":{"row":18,"column":49},"end":{"row":18,"column":50},"action":"insert","lines":["s"],"id":422}],[{"start":{"row":18,"column":58},"end":{"row":18,"column":59},"action":"insert","lines":["."],"id":423},{"start":{"row":18,"column":59},"end":{"row":18,"column":60},"action":"insert","lines":["d"]},{"start":{"row":18,"column":60},"end":{"row":18,"column":61},"action":"insert","lines":["b"]},{"start":{"row":18,"column":61},"end":{"row":18,"column":62},"action":"insert","lines":["."]}],[{"start":{"row":18,"column":61},"end":{"row":18,"column":62},"action":"remove","lines":["."],"id":424}],[{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"remove","lines":["S"],"id":425}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["c"],"id":426},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["d"]}],[{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":[" "],"id":427},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":["."]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["."]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"remove","lines":["."],"id":428},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"remove","lines":["."]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"remove","lines":[" "]},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"remove","lines":["d"]},{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["c"]}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["M"],"id":429},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["O"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["N"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["G"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["O"]}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["_"],"id":430}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["="],"id":431}],[{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["="],"id":432},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["_"]}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"remove","lines":["\""],"id":433}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["'"],"id":434}],[{"start":{"row":9,"column":47},"end":{"row":9,"column":48},"action":"remove","lines":["\""],"id":435}],[{"start":{"row":9,"column":47},"end":{"row":9,"column":48},"action":"insert","lines":["'"],"id":436}],[{"start":{"row":18,"column":52},"end":{"row":18,"column":53},"action":"remove","lines":[" "],"id":437}],[{"start":{"row":18,"column":50},"end":{"row":18,"column":51},"action":"remove","lines":[" "],"id":438}],[{"start":{"row":18,"column":60},"end":{"row":18,"column":77},"action":"remove","lines":["bakingBookRecipes"],"id":444},{"start":{"row":18,"column":60},"end":{"row":18,"column":61},"action":"insert","lines":["r"]},{"start":{"row":18,"column":61},"end":{"row":18,"column":62},"action":"insert","lines":["e"]},{"start":{"row":18,"column":62},"end":{"row":18,"column":63},"action":"insert","lines":["c"]},{"start":{"row":18,"column":63},"end":{"row":18,"column":64},"action":"insert","lines":["i"]},{"start":{"row":18,"column":64},"end":{"row":18,"column":65},"action":"insert","lines":["p"]},{"start":{"row":18,"column":65},"end":{"row":18,"column":66},"action":"insert","lines":["e"]},{"start":{"row":18,"column":66},"end":{"row":18,"column":67},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["P"],"id":445}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["p"],"id":446}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["M"],"id":447}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["m"],"id":448}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":15},"action":"remove","lines":["pymongo"],"id":449},{"start":{"row":13,"column":8},"end":{"row":13,"column":15},"action":"insert","lines":["pymongo"]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["p"],"id":450}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["P"],"id":451}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["m"],"id":452}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["M"],"id":453}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":454},{"start":{"row":3,"column":34},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":75},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":455},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":4},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "],"id":456}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["@"],"id":457},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["a"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["p"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["p"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["."]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["r"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["u"],"id":458},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["t"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":10},"end":{"row":18,"column":12},"action":"insert","lines":["()"],"id":459}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":13},"action":"insert","lines":["''"],"id":460}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["/"],"id":461},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["r"]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["c"],"id":462},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["i"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["p"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["e"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["_"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["c"]},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["a"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["r"]},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":26},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":463},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["d"]},{"start":{"row":19,"column":1},"end":{"row":19,"column":2},"action":"insert","lines":["e"]},{"start":{"row":19,"column":2},"end":{"row":19,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"insert","lines":[" "],"id":464},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["r"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["e"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["c"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["i"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["p"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["_"],"id":465},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["c"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["a"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["r"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":17},"action":"insert","lines":["()"],"id":466}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":[":"],"id":467}],[{"start":{"row":19,"column":18},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":468},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":["r"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["e"]},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":["t"]},{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"insert","lines":["u"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["r"]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":[" "],"id":469},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":["r"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["e"]},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["n"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["d"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["e"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["r"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["_"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["t"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":["m"],"id":470},{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"insert","lines":["p"]},{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"insert","lines":["l"]},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"insert","lines":["a"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["t"]},{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":28},"action":"insert","lines":["()"],"id":471}],[{"start":{"row":20,"column":27},"end":{"row":20,"column":29},"action":"insert","lines":["\"\""],"id":472}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["r"],"id":473},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":["e"]},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"insert","lines":["c"]},{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"insert","lines":["i"]},{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"insert","lines":["p"]},{"start":{"row":20,"column":33},"end":{"row":20,"column":34},"action":"insert","lines":["e"]},{"start":{"row":20,"column":34},"end":{"row":20,"column":35},"action":"insert","lines":["c"]},{"start":{"row":20,"column":35},"end":{"row":20,"column":36},"action":"insert","lines":["a"]},{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"insert","lines":["r"]},{"start":{"row":20,"column":37},"end":{"row":20,"column":38},"action":"insert","lines":["d"]},{"start":{"row":20,"column":38},"end":{"row":20,"column":39},"action":"insert","lines":["."]}],[{"start":{"row":20,"column":39},"end":{"row":20,"column":40},"action":"insert","lines":["h"],"id":474},{"start":{"row":20,"column":40},"end":{"row":20,"column":41},"action":"insert","lines":["t"]},{"start":{"row":20,"column":41},"end":{"row":20,"column":42},"action":"insert","lines":["m"]},{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"insert","lines":["l"]}],[{"start":{"row":20,"column":44},"end":{"row":20,"column":45},"action":"insert","lines":[","],"id":475}],[{"start":{"row":20,"column":45},"end":{"row":20,"column":46},"action":"insert","lines":[" "],"id":476},{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"insert","lines":["r"]},{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"insert","lines":["e"]},{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"insert","lines":["c"]},{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"insert","lines":["i"]},{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"insert","lines":["p"]},{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"insert","lines":["e"]},{"start":{"row":20,"column":52},"end":{"row":20,"column":53},"action":"insert","lines":["s"]}],[{"start":{"row":20,"column":53},"end":{"row":20,"column":54},"action":"insert","lines":["="],"id":477},{"start":{"row":20,"column":54},"end":{"row":20,"column":55},"action":"insert","lines":["m"]},{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"insert","lines":["o"]},{"start":{"row":20,"column":56},"end":{"row":20,"column":57},"action":"insert","lines":["n"]},{"start":{"row":20,"column":57},"end":{"row":20,"column":58},"action":"insert","lines":["g"]},{"start":{"row":20,"column":58},"end":{"row":20,"column":59},"action":"insert","lines":["o"]},{"start":{"row":20,"column":59},"end":{"row":20,"column":60},"action":"insert","lines":["."]}],[{"start":{"row":20,"column":60},"end":{"row":20,"column":61},"action":"insert","lines":["d"],"id":478},{"start":{"row":20,"column":61},"end":{"row":20,"column":62},"action":"insert","lines":["b"]},{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"insert","lines":["."]},{"start":{"row":20,"column":63},"end":{"row":20,"column":64},"action":"insert","lines":["r"]},{"start":{"row":20,"column":64},"end":{"row":20,"column":65},"action":"insert","lines":["e"]},{"start":{"row":20,"column":65},"end":{"row":20,"column":66},"action":"insert","lines":["c"]},{"start":{"row":20,"column":66},"end":{"row":20,"column":67},"action":"insert","lines":["i"]},{"start":{"row":20,"column":67},"end":{"row":20,"column":68},"action":"insert","lines":["p"]},{"start":{"row":20,"column":68},"end":{"row":20,"column":69},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":69},"end":{"row":20,"column":70},"action":"insert","lines":["s"],"id":479},{"start":{"row":20,"column":70},"end":{"row":20,"column":71},"action":"insert","lines":["."]},{"start":{"row":20,"column":71},"end":{"row":20,"column":72},"action":"insert","lines":["f"]},{"start":{"row":20,"column":72},"end":{"row":20,"column":73},"action":"insert","lines":["i"]},{"start":{"row":20,"column":73},"end":{"row":20,"column":74},"action":"insert","lines":["n"]},{"start":{"row":20,"column":74},"end":{"row":20,"column":75},"action":"insert","lines":["d"]}],[{"start":{"row":20,"column":75},"end":{"row":20,"column":77},"action":"insert","lines":["()"],"id":480}],[{"start":{"row":20,"column":45},"end":{"row":20,"column":46},"action":"insert","lines":[" "],"id":481},{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"insert","lines":["l"]},{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"insert","lines":["e"]},{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"insert","lines":["n"]},{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"insert","lines":["="]}],[{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"insert","lines":["l"],"id":482},{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"insert","lines":["e"]},{"start":{"row":20,"column":52},"end":{"row":20,"column":53},"action":"insert","lines":["n"]}],[{"start":{"row":20,"column":53},"end":{"row":20,"column":55},"action":"insert","lines":["()"],"id":483}],[{"start":{"row":20,"column":53},"end":{"row":20,"column":55},"action":"remove","lines":["()"],"id":484},{"start":{"row":20,"column":52},"end":{"row":20,"column":53},"action":"remove","lines":["n"]},{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"remove","lines":["e"]},{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"remove","lines":["l"]},{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"remove","lines":["="]},{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"remove","lines":["n"]},{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"remove","lines":["e"]},{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"remove","lines":["l"]},{"start":{"row":20,"column":45},"end":{"row":20,"column":46},"action":"remove","lines":[" "]}],[{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"insert","lines":["l"],"id":485},{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"insert","lines":["e"]},{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"insert","lines":["n"]}],[{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"insert","lines":[" "],"id":486},{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"insert","lines":["="]}],[{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"insert","lines":[" "],"id":487},{"start":{"row":20,"column":52},"end":{"row":20,"column":53},"action":"insert","lines":["l"]},{"start":{"row":20,"column":53},"end":{"row":20,"column":54},"action":"insert","lines":["e"]},{"start":{"row":20,"column":54},"end":{"row":20,"column":55},"action":"insert","lines":["n"]},{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"insert","lines":["("]}],[{"start":{"row":20,"column":56},"end":{"row":20,"column":57},"action":"insert","lines":["r"],"id":488},{"start":{"row":20,"column":57},"end":{"row":20,"column":58},"action":"insert","lines":["e"]},{"start":{"row":20,"column":58},"end":{"row":20,"column":59},"action":"insert","lines":["c"]},{"start":{"row":20,"column":59},"end":{"row":20,"column":60},"action":"insert","lines":["i"]},{"start":{"row":20,"column":60},"end":{"row":20,"column":61},"action":"insert","lines":["p"]},{"start":{"row":20,"column":61},"end":{"row":20,"column":62},"action":"insert","lines":["e"]},{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"insert","lines":["s"]},{"start":{"row":20,"column":63},"end":{"row":20,"column":64},"action":"insert","lines":["."]}],[{"start":{"row":20,"column":63},"end":{"row":20,"column":64},"action":"remove","lines":["."],"id":489},{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"remove","lines":["s"]},{"start":{"row":20,"column":61},"end":{"row":20,"column":62},"action":"remove","lines":["e"]},{"start":{"row":20,"column":60},"end":{"row":20,"column":61},"action":"remove","lines":["p"]},{"start":{"row":20,"column":59},"end":{"row":20,"column":60},"action":"remove","lines":["i"]},{"start":{"row":20,"column":58},"end":{"row":20,"column":59},"action":"remove","lines":["c"]},{"start":{"row":20,"column":57},"end":{"row":20,"column":58},"action":"remove","lines":["e"]},{"start":{"row":20,"column":56},"end":{"row":20,"column":57},"action":"remove","lines":["r"]},{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"remove","lines":["("]},{"start":{"row":20,"column":54},"end":{"row":20,"column":55},"action":"remove","lines":["n"]},{"start":{"row":20,"column":53},"end":{"row":20,"column":54},"action":"remove","lines":["e"]},{"start":{"row":20,"column":52},"end":{"row":20,"column":53},"action":"remove","lines":["l"]},{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"remove","lines":[" "]},{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"remove","lines":["="]},{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"remove","lines":[" "]}],[{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"remove","lines":["n"],"id":490},{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"remove","lines":["e"]},{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"remove","lines":["l"]}],[{"start":{"row":20,"column":76},"end":{"row":20,"column":77},"action":"remove","lines":[")"],"id":491},{"start":{"row":20,"column":75},"end":{"row":20,"column":77},"action":"remove","lines":["()"]},{"start":{"row":20,"column":74},"end":{"row":20,"column":75},"action":"remove","lines":["d"]},{"start":{"row":20,"column":73},"end":{"row":20,"column":74},"action":"remove","lines":["n"]},{"start":{"row":20,"column":72},"end":{"row":20,"column":73},"action":"remove","lines":["i"]},{"start":{"row":20,"column":71},"end":{"row":20,"column":72},"action":"remove","lines":["f"]}],[{"start":{"row":20,"column":71},"end":{"row":20,"column":72},"action":"insert","lines":[")"],"id":492}],[{"start":{"row":20,"column":71},"end":{"row":20,"column":72},"action":"insert","lines":["t"],"id":493},{"start":{"row":20,"column":72},"end":{"row":20,"column":73},"action":"insert","lines":["h"]},{"start":{"row":20,"column":73},"end":{"row":20,"column":74},"action":"insert","lines":["i"]},{"start":{"row":20,"column":74},"end":{"row":20,"column":75},"action":"insert","lines":["s"]}],[{"start":{"row":20,"column":74},"end":{"row":20,"column":75},"action":"remove","lines":["s"],"id":494},{"start":{"row":20,"column":73},"end":{"row":20,"column":74},"action":"remove","lines":["i"]},{"start":{"row":20,"column":72},"end":{"row":20,"column":73},"action":"remove","lines":["h"]},{"start":{"row":20,"column":71},"end":{"row":20,"column":72},"action":"remove","lines":["t"]},{"start":{"row":20,"column":70},"end":{"row":20,"column":71},"action":"remove","lines":["."]},{"start":{"row":20,"column":69},"end":{"row":20,"column":70},"action":"remove","lines":["s"]},{"start":{"row":20,"column":68},"end":{"row":20,"column":69},"action":"remove","lines":["e"]},{"start":{"row":20,"column":67},"end":{"row":20,"column":68},"action":"remove","lines":["p"]},{"start":{"row":20,"column":66},"end":{"row":20,"column":67},"action":"remove","lines":["i"]},{"start":{"row":20,"column":65},"end":{"row":20,"column":66},"action":"remove","lines":["c"]},{"start":{"row":20,"column":64},"end":{"row":20,"column":65},"action":"remove","lines":["e"]},{"start":{"row":20,"column":63},"end":{"row":20,"column":64},"action":"remove","lines":["r"]},{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"remove","lines":["."]},{"start":{"row":20,"column":61},"end":{"row":20,"column":62},"action":"remove","lines":["b"]},{"start":{"row":20,"column":60},"end":{"row":20,"column":61},"action":"remove","lines":["d"]},{"start":{"row":20,"column":59},"end":{"row":20,"column":60},"action":"remove","lines":["."]},{"start":{"row":20,"column":58},"end":{"row":20,"column":59},"action":"remove","lines":["o"]},{"start":{"row":20,"column":57},"end":{"row":20,"column":58},"action":"remove","lines":["g"]},{"start":{"row":20,"column":56},"end":{"row":20,"column":57},"action":"remove","lines":["n"]}],[{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"remove","lines":["o"],"id":495},{"start":{"row":20,"column":54},"end":{"row":20,"column":55},"action":"remove","lines":["m"]},{"start":{"row":20,"column":53},"end":{"row":20,"column":54},"action":"remove","lines":["="]},{"start":{"row":20,"column":52},"end":{"row":20,"column":53},"action":"remove","lines":["s"]},{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"remove","lines":["e"]},{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"remove","lines":["p"]},{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"remove","lines":["i"]},{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"remove","lines":["c"]},{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"remove","lines":["e"]},{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"remove","lines":["r"]},{"start":{"row":20,"column":45},"end":{"row":20,"column":46},"action":"remove","lines":[" "]},{"start":{"row":20,"column":44},"end":{"row":20,"column":45},"action":"remove","lines":[","]}]]},"ace":{"folds":[],"scrolltop":111,"scrollleft":0,"selection":{"start":{"row":20,"column":44},"end":{"row":20,"column":44},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":8,"state":"start","mode":"ace/mode/python"}},"timestamp":1566247218269,"hash":"6e6ac6259e32357b5e97c184211b475901080f35"}