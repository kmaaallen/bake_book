<h1>Resources</h1>
<h2>Image sources</h2>
<h3>Brownies:</h3>
https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Chocolate_brownies.jpg/800px-Chocolate_brownies.jpg
<h3>Christmas Biscuits:</h3>
https://c.pxhere.com/photos/e2/7e/santa's_arm_hot_chocolate_cocoa_christmas_cookie_chocolate_hot_cookies_holiday-1264689.jpg!d
<h3>Chocolate chip cookies</h3>
https://c.pxhere.com/images/9d/d6/d3a64f8beb97ee0bcf550dbe4dd1-1453093.jpg!d
<h3>Classic Victoria Sponge</h3>
https://upload.wikimedia.org/wikipedia/commons/0/05/111rfyh.jpg
<h3>Pumpkin Pie</h3>
https://cdn.pixabay.com/photo/2015/11/13/02/06/pumpkin-pie-1041330_960_720.jpg
<h3> New York Cheesecake</h3>
https://upload.wikimedia.org/wikipedia/commons/d/d6/New_york_cheesecake_with_strawberries.jpg
<h3>Raspberry cupcakes</h3>
https://www.maxpixel.net/static/photo/1x/Food-Raspberries-Nutrition-Lime-Fruit-Lemon-2546686.jpg

<h2>Recipes</h2>
<ul>

<li>Christmas Biscuits</li>
<ul>
<li>Family recipe</li>
</ul>

<li>Chocolate Chip Cookies</li>
<ul>
<li>Family recipe</li>
</ul>

<li>The Old Mans Bacon and Egg Pie</li>
<ul>
<li>Family recipe adapted from <a href="http://www.radionz.co.nz/collections/recipes/best-ever-bacon-and-egg-pie">http://www.radionz.co.nz/collections/recipes/best-ever-bacon-and-egg-pie</a></li>
</ul>

<li>BBC Good Food: Best Ever Chocolate Brownies</li>
<ul>
<li>https://www.bbcgoodfood.com/recipes/1223/bestever-brownies</li>
</ul>

<li>Classic Victoria Sponge</li>
<ul>
<li>https://www.bbcgoodfood.com/recipes/1997/classic-victoria-sandwich</li>
</ul>

<li>Pumpkin Pie</li>
<ul>
<li>https://www.bbcgoodfood.com/recipes/pumpkin-pie</li>
</ul>

<li>New York Cheesecake</li>
<ul>
<li>https://www.bbcgoodfood.com/recipes/2869/new-york-cheesecake</li>
</ul>

<li>Raspberry Cupcakes</li>
<ul>
<li>https://www.bbcgoodfood.com/recipes/2210/warm-raspberry-cupcakes-with-orange-sugar-drizzle</li>
</ul>


</ul>


<h2> Code Snippets </h2>
{% codeblock %}

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

{% endcodeblock %}

<p>Messages template with button, sourced from https://pythonprogramming.net/flash-flask-tutorial/</p>

{% codeblock %}
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404error.html'), 404
{% endcodeblock %}
<p>Error handler function sourced from https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/</p>