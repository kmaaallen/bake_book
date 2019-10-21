# Resources
## Image sources
### Brownies:
https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Chocolate_brownies.jpg/800px-Chocolate_brownies.jpg
### Christmas Biscuits:
https://c.pxhere.com/photos/e2/7e/santa's_arm_hot_chocolate_cocoa_christmas_cookie_chocolate_hot_cookies_holiday-1264689.jpg!d
### Chocolate chip cookies:
https://c.pxhere.com/images/9d/d6/d3a64f8beb97ee0bcf550dbe4dd1-1453093.jpg!d
### Classic Victoria Sponge:
https://upload.wikimedia.org/wikipedia/commons/0/05/111rfyh.jpg
### Pumpkin Pie:
https://cdn.pixabay.com/photo/2015/11/13/02/06/pumpkin-pie-1041330_960_720.jpg
### New York Cheesecake:
https://upload.wikimedia.org/wikipedia/commons/d/d6/New_york_cheesecake_with_strawberries.jpg
### Raspberry cupcakes:
https://www.maxpixel.net/static/photo/1x/Food-Raspberries-Nutrition-Lime-Fruit-Lemon-2546686.jpg

## Recipes
- Christmas Biscuits
	- Family recipe

- Chocolate Chip Cookies
	- Family recipe

- The Old Mans Bacon and Egg Pie
	- Adapted from [http://www.radionz.co.nz/collections/recipes/best-ever-bacon-and-egg-pie](http://www.radionz.co.nz/collections/recipes/best-ever-bacon-and-egg-pie)

- BBC Good Food: Best Ever Chocolate Brownies
	- https://www.bbcgoodfood.com/recipes/1223/bestever-brownies

- Classic Victoria Sponge
	- https://www.bbcgoodfood.com/recipes/1997/classic-victoria-sandwich

- Pumpkin Pie
	- https://www.bbcgoodfood.com/recipes/pumpkin-pie

- New York Cheesecake
	- https://www.bbcgoodfood.com/recipes/2869/new-york-cheesecake

- Raspberry Cupcakes
	- https://www.bbcgoodfood.com/recipes/2210/warm-raspberry-cupcakes-with-orange-sugar-drizzle

## Code Snippets
		{% with messages = get_flashed_messages() %}
			  {% if messages %}
			    {% for message in messages %}
				  <div class="alert alert-warning alert-dismissible" role="alert">
				  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
					{{message}}
				  </div>
				{% endfor %}
			  {% endif %}
			{% endwith %} 

Messages template with button, sourced from https://pythonprogramming.net/flash-flask-tutorial/


		@app.errorhandler(404)
		def page_not_found(e):
		    return render_template('404error.html'), 404

Error handler function sourced from https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/