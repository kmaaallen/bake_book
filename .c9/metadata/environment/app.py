{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":136,"column":8},"end":{"row":136,"column":12},"action":"insert","lines":["    "],"id":4398}],[{"start":{"row":137,"column":7},"end":{"row":137,"column":8},"action":"insert","lines":[" "],"id":4399}],[{"start":{"row":137,"column":8},"end":{"row":137,"column":12},"action":"insert","lines":["    "],"id":4400}],[{"start":{"row":137,"column":12},"end":{"row":137,"column":13},"action":"remove","lines":[" "],"id":4401}],[{"start":{"row":129,"column":5},"end":{"row":138,"column":5},"action":"remove","lines":["   presigned_post = s3.generate_presigned_post(","            Bucket = S3_BUCKET,","            Key = file_name,","            Fields = {\"acl\": \"public-read\", \"Content-Type\": file_type},","            Conditions = [","                {\"acl\": \"public-read\"},","                {\"Content-Type\": file_type}","            ],","            ExpiresIn = 3600","    )"],"id":4402}],[{"start":{"row":129,"column":5},"end":{"row":129,"column":8},"action":"insert","lines":["   "],"id":4403}],[{"start":{"row":129,"column":8},"end":{"row":132,"column":53},"action":"insert","lines":["presigned_post = s3.generate_presigned_post(Bucket=S3_BUCKET,","        Key=file_name, Fields={'acl': 'public-read',","        'Content-Type': file_type}, Conditions=[{'acl': 'public-read'},","        {'Content-Type': file_type}], ExpiresIn=3600)"],"id":4404}],[{"start":{"row":132,"column":53},"end":{"row":133,"column":0},"action":"insert","lines":["",""],"id":4405},{"start":{"row":133,"column":0},"end":{"row":133,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":134,"column":0},"end":{"row":134,"column":4},"action":"insert","lines":["    "],"id":4406}],[{"start":{"row":134,"column":4},"end":{"row":134,"column":8},"action":"insert","lines":["    "],"id":4407}],[{"start":{"row":135,"column":4},"end":{"row":135,"column":8},"action":"insert","lines":["    "],"id":4408}],[{"start":{"row":136,"column":3},"end":{"row":136,"column":4},"action":"insert","lines":[" "],"id":4409}],[{"start":{"row":129,"column":7},"end":{"row":137,"column":4},"action":"remove","lines":[" presigned_post = s3.generate_presigned_post(Bucket=S3_BUCKET,","        Key=file_name, Fields={'acl': 'public-read',","        'Content-Type': file_type}, Conditions=[{'acl': 'public-read'},","        {'Content-Type': file_type}], ExpiresIn=3600)","        ","        return json.dumps({","        'data': presigned_post,","     'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)","  })"],"id":4410},{"start":{"row":129,"column":7},"end":{"row":136,"column":30},"action":"insert","lines":["presigned_post = s3.generate_presigned_post(Bucket=S3_BUCKET,","        Key=file_name, Fields={'acl': 'public-read',","        'Content-Type': file_type}, Conditions=[{'acl': 'public-read'},","        {'Content-Type': file_type}], ExpiresIn=3600)","","return json.dumps({'data': presigned_post,","                  'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,","                  file_name)})"]}],[{"start":{"row":129,"column":7},"end":{"row":129,"column":8},"action":"insert","lines":[" "],"id":4411}],[{"start":{"row":129,"column":52},"end":{"row":130,"column":0},"action":"insert","lines":["",""],"id":4412},{"start":{"row":130,"column":0},"end":{"row":130,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":131,"column":4},"end":{"row":131,"column":8},"action":"remove","lines":["    "],"id":4413},{"start":{"row":131,"column":0},"end":{"row":131,"column":4},"action":"remove","lines":["    "]},{"start":{"row":130,"column":29},"end":{"row":131,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":130,"column":29},"end":{"row":131,"column":0},"action":"insert","lines":["",""],"id":4414},{"start":{"row":131,"column":0},"end":{"row":131,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":131,"column":26},"end":{"row":131,"column":27},"action":"remove","lines":[" "],"id":4415},{"start":{"row":131,"column":26},"end":{"row":132,"column":0},"action":"insert","lines":["",""]},{"start":{"row":132,"column":0},"end":{"row":132,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":133,"column":4},"end":{"row":133,"column":8},"action":"remove","lines":["    "],"id":4416},{"start":{"row":133,"column":0},"end":{"row":133,"column":4},"action":"remove","lines":["    "]},{"start":{"row":132,"column":41},"end":{"row":133,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":132,"column":68},"end":{"row":132,"column":69},"action":"remove","lines":[" "],"id":4417},{"start":{"row":132,"column":68},"end":{"row":133,"column":0},"action":"insert","lines":["",""]},{"start":{"row":133,"column":0},"end":{"row":133,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":133,"column":24},"end":{"row":134,"column":0},"action":"insert","lines":["",""],"id":4418},{"start":{"row":134,"column":0},"end":{"row":134,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":135,"column":4},"end":{"row":135,"column":8},"action":"remove","lines":["    "],"id":4419},{"start":{"row":135,"column":0},"end":{"row":135,"column":4},"action":"remove","lines":["    "]},{"start":{"row":134,"column":39},"end":{"row":135,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":134,"column":39},"end":{"row":135,"column":0},"action":"insert","lines":["",""],"id":4420},{"start":{"row":135,"column":0},"end":{"row":135,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":135,"column":43},"end":{"row":136,"column":0},"action":"insert","lines":["",""],"id":4421},{"start":{"row":136,"column":0},"end":{"row":136,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":136,"column":18},"end":{"row":136,"column":19},"action":"remove","lines":[" "],"id":4422},{"start":{"row":136,"column":18},"end":{"row":137,"column":0},"action":"insert","lines":["",""]},{"start":{"row":137,"column":0},"end":{"row":137,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":137,"column":30},"end":{"row":138,"column":0},"action":"insert","lines":["",""],"id":4423},{"start":{"row":138,"column":0},"end":{"row":138,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":138,"column":8},"end":{"row":138,"column":12},"action":"remove","lines":["    "],"id":4424},{"start":{"row":138,"column":4},"end":{"row":138,"column":8},"action":"remove","lines":["    "]},{"start":{"row":138,"column":0},"end":{"row":138,"column":4},"action":"remove","lines":["    "]},{"start":{"row":137,"column":30},"end":{"row":138,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":137,"column":33},"end":{"row":137,"column":34},"action":"remove","lines":[" "],"id":4425},{"start":{"row":137,"column":32},"end":{"row":137,"column":33},"action":"remove","lines":[" "]},{"start":{"row":137,"column":31},"end":{"row":137,"column":32},"action":"remove","lines":[" "]},{"start":{"row":137,"column":30},"end":{"row":137,"column":31},"action":"remove","lines":[" "]}],[{"start":{"row":139,"column":0},"end":{"row":139,"column":4},"action":"insert","lines":["    "],"id":4426}],[{"start":{"row":139,"column":4},"end":{"row":139,"column":8},"action":"insert","lines":["    "],"id":4427}],[{"start":{"row":139,"column":27},"end":{"row":140,"column":0},"action":"insert","lines":["",""],"id":4428},{"start":{"row":140,"column":0},"end":{"row":140,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":141,"column":17},"end":{"row":141,"column":18},"action":"remove","lines":[" "],"id":4429},{"start":{"row":141,"column":16},"end":{"row":141,"column":17},"action":"remove","lines":[" "]},{"start":{"row":141,"column":12},"end":{"row":141,"column":16},"action":"remove","lines":["    "]},{"start":{"row":141,"column":8},"end":{"row":141,"column":12},"action":"remove","lines":["    "]},{"start":{"row":141,"column":4},"end":{"row":141,"column":8},"action":"remove","lines":["    "]},{"start":{"row":141,"column":0},"end":{"row":141,"column":4},"action":"remove","lines":["    "]},{"start":{"row":140,"column":35},"end":{"row":141,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":140,"column":35},"end":{"row":141,"column":0},"action":"insert","lines":["",""],"id":4430},{"start":{"row":141,"column":0},"end":{"row":141,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":142,"column":17},"end":{"row":142,"column":18},"action":"remove","lines":[" "],"id":4431},{"start":{"row":142,"column":16},"end":{"row":142,"column":17},"action":"remove","lines":[" "]},{"start":{"row":142,"column":12},"end":{"row":142,"column":16},"action":"remove","lines":["    "]},{"start":{"row":142,"column":8},"end":{"row":142,"column":12},"action":"remove","lines":["    "]},{"start":{"row":142,"column":4},"end":{"row":142,"column":8},"action":"remove","lines":["    "]},{"start":{"row":142,"column":0},"end":{"row":142,"column":4},"action":"remove","lines":["    "]},{"start":{"row":141,"column":65},"end":{"row":142,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":141,"column":75},"end":{"row":143,"column":8},"action":"insert","lines":["","            ","        "],"id":4432}],[{"start":{"row":142,"column":8},"end":{"row":142,"column":12},"action":"remove","lines":["    "],"id":4433},{"start":{"row":142,"column":4},"end":{"row":142,"column":8},"action":"remove","lines":["    "]},{"start":{"row":142,"column":0},"end":{"row":142,"column":4},"action":"remove","lines":["    "]},{"start":{"row":141,"column":75},"end":{"row":142,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":102,"column":82},"end":{"row":103,"column":0},"action":"insert","lines":["",""],"id":4434},{"start":{"row":103,"column":0},"end":{"row":103,"column":27},"action":"insert","lines":["                           "]}],[{"start":{"row":103,"column":26},"end":{"row":103,"column":27},"action":"remove","lines":[" "],"id":4435},{"start":{"row":103,"column":25},"end":{"row":103,"column":26},"action":"remove","lines":[" "]},{"start":{"row":103,"column":24},"end":{"row":103,"column":25},"action":"remove","lines":[" "]},{"start":{"row":103,"column":20},"end":{"row":103,"column":24},"action":"remove","lines":["    "]},{"start":{"row":103,"column":16},"end":{"row":103,"column":20},"action":"remove","lines":["    "]},{"start":{"row":103,"column":12},"end":{"row":103,"column":16},"action":"remove","lines":["    "]},{"start":{"row":103,"column":8},"end":{"row":103,"column":12},"action":"remove","lines":["    "]},{"start":{"row":103,"column":4},"end":{"row":103,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":103,"column":4},"end":{"row":103,"column":5},"action":"insert","lines":["e"],"id":4436},{"start":{"row":103,"column":5},"end":{"row":103,"column":6},"action":"insert","lines":["l"]},{"start":{"row":103,"column":6},"end":{"row":103,"column":7},"action":"insert","lines":["s"]},{"start":{"row":103,"column":7},"end":{"row":103,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":103,"column":8},"end":{"row":103,"column":9},"action":"insert","lines":[" "],"id":4437}],[{"start":{"row":103,"column":9},"end":{"row":103,"column":10},"action":"insert","lines":["f"],"id":4438},{"start":{"row":103,"column":10},"end":{"row":103,"column":11},"action":"insert","lines":["l"]},{"start":{"row":103,"column":11},"end":{"row":103,"column":12},"action":"insert","lines":["a"]},{"start":{"row":103,"column":12},"end":{"row":103,"column":13},"action":"insert","lines":["s"]},{"start":{"row":103,"column":13},"end":{"row":103,"column":14},"action":"insert","lines":["h"]}],[{"start":{"row":103,"column":14},"end":{"row":103,"column":16},"action":"insert","lines":["()"],"id":4439}],[{"start":{"row":103,"column":15},"end":{"row":103,"column":17},"action":"insert","lines":["''"],"id":4440}],[{"start":{"row":103,"column":16},"end":{"row":103,"column":17},"action":"insert","lines":["S"],"id":4441},{"start":{"row":103,"column":17},"end":{"row":103,"column":18},"action":"insert","lines":["o"]},{"start":{"row":103,"column":18},"end":{"row":103,"column":19},"action":"insert","lines":["r"]},{"start":{"row":103,"column":19},"end":{"row":103,"column":20},"action":"insert","lines":["r"]},{"start":{"row":103,"column":20},"end":{"row":103,"column":21},"action":"insert","lines":["y"]}],[{"start":{"row":103,"column":21},"end":{"row":103,"column":22},"action":"insert","lines":[" "],"id":4442},{"start":{"row":103,"column":22},"end":{"row":103,"column":23},"action":"insert","lines":["y"]},{"start":{"row":103,"column":23},"end":{"row":103,"column":24},"action":"insert","lines":["o"]},{"start":{"row":103,"column":24},"end":{"row":103,"column":25},"action":"insert","lines":["u"]}],[{"start":{"row":103,"column":25},"end":{"row":103,"column":26},"action":"insert","lines":[" "],"id":4443},{"start":{"row":103,"column":26},"end":{"row":103,"column":27},"action":"insert","lines":["d"]},{"start":{"row":103,"column":27},"end":{"row":103,"column":28},"action":"insert","lines":["o"]},{"start":{"row":103,"column":28},"end":{"row":103,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":103,"column":30},"end":{"row":103,"column":31},"action":"insert","lines":["t"],"id":4444}],[{"start":{"row":103,"column":31},"end":{"row":103,"column":32},"action":"insert","lines":[" "],"id":4445},{"start":{"row":103,"column":32},"end":{"row":103,"column":33},"action":"insert","lines":["h"]},{"start":{"row":103,"column":33},"end":{"row":103,"column":34},"action":"insert","lines":["a"]},{"start":{"row":103,"column":34},"end":{"row":103,"column":35},"action":"insert","lines":["v"]},{"start":{"row":103,"column":35},"end":{"row":103,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":103,"column":36},"end":{"row":103,"column":37},"action":"insert","lines":[" "],"id":4446},{"start":{"row":103,"column":37},"end":{"row":103,"column":38},"action":"insert","lines":["a"]},{"start":{"row":103,"column":38},"end":{"row":103,"column":39},"action":"insert","lines":["n"]}],[{"start":{"row":103,"column":38},"end":{"row":103,"column":39},"action":"remove","lines":["n"],"id":4447},{"start":{"row":103,"column":37},"end":{"row":103,"column":38},"action":"remove","lines":["a"]},{"start":{"row":103,"column":36},"end":{"row":103,"column":37},"action":"remove","lines":[" "]},{"start":{"row":103,"column":35},"end":{"row":103,"column":36},"action":"remove","lines":["e"]},{"start":{"row":103,"column":34},"end":{"row":103,"column":35},"action":"remove","lines":["v"]},{"start":{"row":103,"column":33},"end":{"row":103,"column":34},"action":"remove","lines":["a"]},{"start":{"row":103,"column":32},"end":{"row":103,"column":33},"action":"remove","lines":["h"]},{"start":{"row":103,"column":31},"end":{"row":103,"column":32},"action":"remove","lines":[" "]},{"start":{"row":103,"column":30},"end":{"row":103,"column":31},"action":"remove","lines":["t"]},{"start":{"row":103,"column":29},"end":{"row":103,"column":30},"action":"remove","lines":["'"]}],[{"start":{"row":103,"column":29},"end":{"row":103,"column":30},"action":"insert","lines":["|"],"id":4448}],[{"start":{"row":103,"column":29},"end":{"row":103,"column":30},"action":"remove","lines":["|"],"id":4449}],[{"start":{"row":103,"column":29},"end":{"row":103,"column":30},"action":"insert","lines":["\\"],"id":4450},{"start":{"row":103,"column":30},"end":{"row":103,"column":31},"action":"insert","lines":["'"]}],[{"start":{"row":103,"column":31},"end":{"row":103,"column":32},"action":"insert","lines":["t"],"id":4451}],[{"start":{"row":103,"column":32},"end":{"row":103,"column":33},"action":"insert","lines":[" "],"id":4452},{"start":{"row":103,"column":33},"end":{"row":103,"column":34},"action":"insert","lines":["h"]},{"start":{"row":103,"column":34},"end":{"row":103,"column":35},"action":"insert","lines":["a"]},{"start":{"row":103,"column":35},"end":{"row":103,"column":36},"action":"insert","lines":["v"]},{"start":{"row":103,"column":36},"end":{"row":103,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":103,"column":37},"end":{"row":103,"column":38},"action":"insert","lines":[" "],"id":4453},{"start":{"row":103,"column":38},"end":{"row":103,"column":39},"action":"insert","lines":["a"]},{"start":{"row":103,"column":39},"end":{"row":103,"column":40},"action":"insert","lines":["n"]},{"start":{"row":103,"column":40},"end":{"row":103,"column":41},"action":"insert","lines":["y"]}],[{"start":{"row":103,"column":41},"end":{"row":103,"column":42},"action":"insert","lines":[" "],"id":4454},{"start":{"row":103,"column":42},"end":{"row":103,"column":43},"action":"insert","lines":["s"]},{"start":{"row":103,"column":43},"end":{"row":103,"column":44},"action":"insert","lines":["a"]},{"start":{"row":103,"column":44},"end":{"row":103,"column":45},"action":"insert","lines":["v"]},{"start":{"row":103,"column":45},"end":{"row":103,"column":46},"action":"insert","lines":["e"]},{"start":{"row":103,"column":46},"end":{"row":103,"column":47},"action":"insert","lines":["d"]}],[{"start":{"row":103,"column":47},"end":{"row":103,"column":48},"action":"insert","lines":[" "],"id":4455},{"start":{"row":103,"column":48},"end":{"row":103,"column":49},"action":"insert","lines":["r"]},{"start":{"row":103,"column":49},"end":{"row":103,"column":50},"action":"insert","lines":["e"]},{"start":{"row":103,"column":50},"end":{"row":103,"column":51},"action":"insert","lines":["c"]},{"start":{"row":103,"column":51},"end":{"row":103,"column":52},"action":"insert","lines":["i"]},{"start":{"row":103,"column":52},"end":{"row":103,"column":53},"action":"insert","lines":["p"]},{"start":{"row":103,"column":53},"end":{"row":103,"column":54},"action":"insert","lines":["e"]},{"start":{"row":103,"column":54},"end":{"row":103,"column":55},"action":"insert","lines":["s"]},{"start":{"row":103,"column":55},"end":{"row":103,"column":56},"action":"insert","lines":["!"]}],[{"start":{"row":103,"column":55},"end":{"row":103,"column":56},"action":"remove","lines":["!"],"id":4456}],[{"start":{"row":103,"column":55},"end":{"row":103,"column":56},"action":"insert","lines":["."],"id":4457}],[{"start":{"row":103,"column":8},"end":{"row":103,"column":9},"action":"insert","lines":[":"],"id":4458}],[{"start":{"row":103,"column":9},"end":{"row":103,"column":10},"action":"remove","lines":[" "],"id":4459}],[{"start":{"row":103,"column":9},"end":{"row":104,"column":0},"action":"insert","lines":["",""],"id":4460},{"start":{"row":104,"column":0},"end":{"row":104,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":104,"column":55},"end":{"row":104,"column":56},"action":"insert","lines":["'"],"id":4463}],[{"start":{"row":104,"column":14},"end":{"row":104,"column":15},"action":"remove","lines":["'"],"id":4464}],[{"start":{"row":104,"column":14},"end":{"row":104,"column":15},"action":"insert","lines":["\""],"id":4465}],[{"start":{"row":104,"column":55},"end":{"row":104,"column":56},"action":"remove","lines":["'"],"id":4466}],[{"start":{"row":104,"column":55},"end":{"row":104,"column":56},"action":"insert","lines":["\""],"id":4467}],[{"start":{"row":104,"column":28},"end":{"row":104,"column":29},"action":"remove","lines":["\\"],"id":4468}],[{"start":{"row":104,"column":56},"end":{"row":105,"column":0},"action":"insert","lines":["",""],"id":4469},{"start":{"row":105,"column":0},"end":{"row":105,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":49},"action":"remove","lines":["# \"recipe_img_name\": recipe_img_name"],"id":4470},{"start":{"row":161,"column":12},"end":{"row":161,"column":13},"action":"remove","lines":[" "]},{"start":{"row":161,"column":8},"end":{"row":161,"column":12},"action":"remove","lines":["    "]},{"start":{"row":161,"column":4},"end":{"row":161,"column":8},"action":"remove","lines":["    "]},{"start":{"row":161,"column":0},"end":{"row":161,"column":4},"action":"remove","lines":["    "]},{"start":{"row":160,"column":0},"end":{"row":161,"column":0},"action":"remove","lines":["",""]},{"start":{"row":159,"column":18},"end":{"row":160,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":67,"column":58},"end":{"row":68,"column":0},"action":"insert","lines":["",""],"id":4471},{"start":{"row":68,"column":0},"end":{"row":68,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":68,"column":12},"end":{"row":68,"column":13},"action":"insert","lines":["l"],"id":4472},{"start":{"row":68,"column":13},"end":{"row":68,"column":14},"action":"insert","lines":["o"]}],[{"start":{"row":68,"column":14},"end":{"row":68,"column":15},"action":"insert","lines":["g"],"id":4473},{"start":{"row":68,"column":15},"end":{"row":68,"column":16},"action":"insert","lines":["g"]},{"start":{"row":68,"column":16},"end":{"row":68,"column":17},"action":"insert","lines":["e"]},{"start":{"row":68,"column":17},"end":{"row":68,"column":18},"action":"insert","lines":["d"]},{"start":{"row":68,"column":18},"end":{"row":68,"column":19},"action":"insert","lines":["_"]}],[{"start":{"row":68,"column":19},"end":{"row":68,"column":20},"action":"insert","lines":["i"],"id":4474},{"start":{"row":68,"column":20},"end":{"row":68,"column":21},"action":"insert","lines":["n"]}],[{"start":{"row":68,"column":21},"end":{"row":68,"column":22},"action":"insert","lines":[" "],"id":4475},{"start":{"row":68,"column":22},"end":{"row":68,"column":23},"action":"insert","lines":["i"]},{"start":{"row":68,"column":23},"end":{"row":68,"column":24},"action":"insert","lines":["n"]}],[{"start":{"row":68,"column":24},"end":{"row":68,"column":25},"action":"insert","lines":[" "],"id":4476},{"start":{"row":68,"column":25},"end":{"row":68,"column":26},"action":"insert","lines":["s"]},{"start":{"row":68,"column":26},"end":{"row":68,"column":27},"action":"insert","lines":["e"]},{"start":{"row":68,"column":27},"end":{"row":68,"column":28},"action":"insert","lines":["s"]},{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"insert","lines":["s"]},{"start":{"row":68,"column":29},"end":{"row":68,"column":30},"action":"insert","lines":["i"]},{"start":{"row":68,"column":30},"end":{"row":68,"column":31},"action":"insert","lines":["o"]},{"start":{"row":68,"column":31},"end":{"row":68,"column":32},"action":"insert","lines":["n"]}],[{"start":{"row":68,"column":32},"end":{"row":68,"column":33},"action":"insert","lines":[" "],"id":4477},{"start":{"row":68,"column":33},"end":{"row":68,"column":34},"action":"insert","lines":["="]},{"start":{"row":68,"column":34},"end":{"row":68,"column":35},"action":"insert","lines":["="]}],[{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"insert","lines":[" "],"id":4478},{"start":{"row":68,"column":36},"end":{"row":68,"column":37},"action":"insert","lines":["t"]},{"start":{"row":68,"column":37},"end":{"row":68,"column":38},"action":"insert","lines":["r"]},{"start":{"row":68,"column":38},"end":{"row":68,"column":39},"action":"insert","lines":["u"]},{"start":{"row":68,"column":39},"end":{"row":68,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":68,"column":0},"end":{"row":68,"column":40},"action":"remove","lines":["            logged_in in session == true"],"id":4479},{"start":{"row":67,"column":58},"end":{"row":68,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":116,"column":0},"end":{"row":117,"column":0},"action":"remove","lines":["",""],"id":4480},{"start":{"row":115,"column":8},"end":{"row":116,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":127,"column":8},"end":{"row":127,"column":10},"action":"insert","lines":["# "],"id":4481},{"start":{"row":128,"column":8},"end":{"row":128,"column":10},"action":"insert","lines":["# "]},{"start":{"row":129,"column":8},"end":{"row":129,"column":10},"action":"insert","lines":["# "]},{"start":{"row":130,"column":8},"end":{"row":130,"column":10},"action":"insert","lines":["# "]},{"start":{"row":132,"column":8},"end":{"row":132,"column":10},"action":"insert","lines":["# "]},{"start":{"row":133,"column":8},"end":{"row":133,"column":10},"action":"insert","lines":["# "]},{"start":{"row":134,"column":8},"end":{"row":134,"column":10},"action":"insert","lines":["# "]},{"start":{"row":135,"column":8},"end":{"row":135,"column":10},"action":"insert","lines":["# "]},{"start":{"row":136,"column":8},"end":{"row":136,"column":10},"action":"insert","lines":["# "]},{"start":{"row":137,"column":8},"end":{"row":137,"column":10},"action":"insert","lines":["# "]},{"start":{"row":138,"column":8},"end":{"row":138,"column":10},"action":"insert","lines":["# "]},{"start":{"row":139,"column":8},"end":{"row":139,"column":10},"action":"insert","lines":["# "]},{"start":{"row":140,"column":8},"end":{"row":140,"column":10},"action":"insert","lines":["# "]},{"start":{"row":142,"column":8},"end":{"row":142,"column":10},"action":"insert","lines":["# "]},{"start":{"row":143,"column":8},"end":{"row":143,"column":10},"action":"insert","lines":["# "]},{"start":{"row":144,"column":8},"end":{"row":144,"column":10},"action":"insert","lines":["# "]},{"start":{"row":145,"column":8},"end":{"row":145,"column":10},"action":"insert","lines":["# "]}],[{"start":{"row":127,"column":8},"end":{"row":127,"column":10},"action":"remove","lines":["# "],"id":4482},{"start":{"row":128,"column":8},"end":{"row":128,"column":10},"action":"remove","lines":["# "]},{"start":{"row":129,"column":8},"end":{"row":129,"column":10},"action":"remove","lines":["# "]},{"start":{"row":130,"column":8},"end":{"row":130,"column":10},"action":"remove","lines":["# "]},{"start":{"row":132,"column":8},"end":{"row":132,"column":10},"action":"remove","lines":["# "]},{"start":{"row":133,"column":8},"end":{"row":133,"column":10},"action":"remove","lines":["# "]},{"start":{"row":134,"column":8},"end":{"row":134,"column":10},"action":"remove","lines":["# "]},{"start":{"row":135,"column":8},"end":{"row":135,"column":10},"action":"remove","lines":["# "]},{"start":{"row":136,"column":8},"end":{"row":136,"column":10},"action":"remove","lines":["# "]},{"start":{"row":137,"column":8},"end":{"row":137,"column":10},"action":"remove","lines":["# "]},{"start":{"row":138,"column":8},"end":{"row":138,"column":10},"action":"remove","lines":["# "]},{"start":{"row":139,"column":8},"end":{"row":139,"column":10},"action":"remove","lines":["# "]},{"start":{"row":140,"column":8},"end":{"row":140,"column":10},"action":"remove","lines":["# "]},{"start":{"row":142,"column":8},"end":{"row":142,"column":10},"action":"remove","lines":["# "]},{"start":{"row":143,"column":8},"end":{"row":143,"column":10},"action":"remove","lines":["# "]},{"start":{"row":144,"column":8},"end":{"row":144,"column":10},"action":"remove","lines":["# "]},{"start":{"row":145,"column":8},"end":{"row":145,"column":10},"action":"remove","lines":["# "]}],[{"start":{"row":67,"column":58},"end":{"row":68,"column":0},"action":"insert","lines":["",""],"id":4483},{"start":{"row":68,"column":0},"end":{"row":68,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":68,"column":12},"end":{"row":68,"column":34},"action":"insert","lines":["'logged_in' in session"],"id":4484}],[{"start":{"row":68,"column":34},"end":{"row":68,"column":35},"action":"insert","lines":[" "],"id":4485},{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"insert","lines":["-"]},{"start":{"row":68,"column":36},"end":{"row":68,"column":37},"action":"insert","lines":["-"]}],[{"start":{"row":68,"column":37},"end":{"row":68,"column":38},"action":"insert","lines":[" "],"id":4486}],[{"start":{"row":68,"column":37},"end":{"row":68,"column":38},"action":"remove","lines":[" "],"id":4487},{"start":{"row":68,"column":36},"end":{"row":68,"column":37},"action":"remove","lines":["-"]},{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"remove","lines":["-"]}],[{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"insert","lines":["="],"id":4488},{"start":{"row":68,"column":36},"end":{"row":68,"column":37},"action":"insert","lines":["="]}],[{"start":{"row":68,"column":37},"end":{"row":68,"column":38},"action":"insert","lines":[" "],"id":4489},{"start":{"row":68,"column":38},"end":{"row":68,"column":39},"action":"insert","lines":["t"]},{"start":{"row":68,"column":39},"end":{"row":68,"column":40},"action":"insert","lines":["r"]},{"start":{"row":68,"column":40},"end":{"row":68,"column":41},"action":"insert","lines":["u"]},{"start":{"row":68,"column":41},"end":{"row":68,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":68,"column":12},"end":{"row":68,"column":42},"action":"remove","lines":["'logged_in' in session == true"],"id":4491},{"start":{"row":68,"column":8},"end":{"row":68,"column":12},"action":"remove","lines":["    "]},{"start":{"row":68,"column":4},"end":{"row":68,"column":8},"action":"remove","lines":["    "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":67,"column":58},"end":{"row":68,"column":0},"action":"remove","lines":["",""],"id":4492}],[{"start":{"row":68,"column":37},"end":{"row":68,"column":49},"action":"remove","lines":["show_recipes"],"id":4493},{"start":{"row":68,"column":37},"end":{"row":68,"column":38},"action":"insert","lines":["l"]},{"start":{"row":68,"column":38},"end":{"row":68,"column":39},"action":"insert","lines":["o"]},{"start":{"row":68,"column":39},"end":{"row":68,"column":40},"action":"insert","lines":["g"]},{"start":{"row":68,"column":40},"end":{"row":68,"column":41},"action":"insert","lines":["i"]},{"start":{"row":68,"column":41},"end":{"row":68,"column":42},"action":"insert","lines":["n"]}],[{"start":{"row":128,"column":48},"end":{"row":128,"column":59},"action":"remove","lines":["form_normal"],"id":4494},{"start":{"row":128,"column":48},"end":{"row":128,"column":49},"action":"insert","lines":["r"]},{"start":{"row":128,"column":49},"end":{"row":128,"column":50},"action":"insert","lines":["e"]},{"start":{"row":128,"column":50},"end":{"row":128,"column":51},"action":"insert","lines":["q"]},{"start":{"row":128,"column":51},"end":{"row":128,"column":52},"action":"insert","lines":["u"]},{"start":{"row":128,"column":52},"end":{"row":128,"column":53},"action":"insert","lines":["e"]},{"start":{"row":128,"column":53},"end":{"row":128,"column":54},"action":"insert","lines":["s"]},{"start":{"row":128,"column":54},"end":{"row":128,"column":55},"action":"insert","lines":["t"]}],[{"start":{"row":128,"column":55},"end":{"row":128,"column":56},"action":"insert","lines":["."],"id":4495},{"start":{"row":128,"column":56},"end":{"row":128,"column":57},"action":"insert","lines":["f"]},{"start":{"row":128,"column":57},"end":{"row":128,"column":58},"action":"insert","lines":["o"]},{"start":{"row":128,"column":58},"end":{"row":128,"column":59},"action":"insert","lines":["r"]},{"start":{"row":128,"column":59},"end":{"row":128,"column":60},"action":"insert","lines":["m"]}],[{"start":{"row":128,"column":60},"end":{"row":128,"column":61},"action":"insert","lines":["."],"id":4496}],[{"start":{"row":128,"column":61},"end":{"row":128,"column":62},"action":"insert","lines":["t"],"id":4497},{"start":{"row":128,"column":62},"end":{"row":128,"column":63},"action":"insert","lines":["o"]},{"start":{"row":128,"column":63},"end":{"row":128,"column":64},"action":"insert","lines":["_"]},{"start":{"row":128,"column":64},"end":{"row":128,"column":65},"action":"insert","lines":["d"]},{"start":{"row":128,"column":65},"end":{"row":128,"column":66},"action":"insert","lines":["i"]},{"start":{"row":128,"column":66},"end":{"row":128,"column":67},"action":"insert","lines":["c"]},{"start":{"row":128,"column":67},"end":{"row":128,"column":68},"action":"insert","lines":["t"]}],[{"start":{"row":128,"column":68},"end":{"row":128,"column":69},"action":"insert","lines":["("],"id":4498}],[{"start":{"row":128,"column":85},"end":{"row":128,"column":86},"action":"insert","lines":[")"],"id":4499}],[{"start":{"row":128,"column":69},"end":{"row":128,"column":85},"action":"remove","lines":["['recipe_title']"],"id":4500}],[{"start":{"row":128,"column":70},"end":{"row":128,"column":86},"action":"insert","lines":["['recipe_title']"],"id":4501}]]},"ace":{"folds":[],"scrolltop":1560,"scrollleft":0,"selection":{"start":{"row":128,"column":86},"end":{"row":128,"column":86},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":110,"state":"start","mode":"ace/mode/python"}},"timestamp":1568398949069,"hash":"d505c8928da9fb5bbcbaae71ac7739009078023a"}