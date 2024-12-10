<h3>The Recipe Vault</h3>

The Recipe Vault is a site for sharing recipes and articles around food/diets. It's written on Django with PostgreSQL as DB.

Not registered users have only GET permissions, seeing already published articles and recipes with comments/rating attached to them. They can also see the profile of the user that published the article/recipe, trying to edit/delete any of them will have them redirected to the details page of articles or recipes, depending on which they try to modify.
If they try to modify any of the user data, they will be redirected to a login page, if they log in with another user not the one they are trying to modify, they will get redirected to home.

Registered users have permissions to do everything a non registered user does, but they can also create/delete/update recipes, can modify their own profile. Another perk of registered users is that they can also comment and rate articles and recipes.

It has two groups of admins, first one is staff. 
Staff is responsible for moderating the content registered user put in, editing or deleting recipes/comments.
Superusers can do everything staff members do, but they can also edit and delete users profile, which a staff member cannot do.
