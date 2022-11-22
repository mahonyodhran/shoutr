# Shoutr

Application where you can post to a timeline in a manner that is definitely not similar to any other company in the world. 


## Resources

 - [Flask](https://flask.palletsprojects.com/en/2.2.x/)
 - [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Roadmap

In no particular order
* UI Work
  * Register page ✔️ 19/11
  * Login page ✔️ 19/11
  * File to extend Register/Login from
  * Nav bar (side? Top?)
  * Shout on timeline

- User profile page (just details etc - no shouts linked to them) ✔️ 19/11

- User profile page shows shouts from user

- Follow a user

- View followers

- View if followers are following you back

- Like a shout

- Tab for liked shouts

- Route similar to getting the profile by id but done by username

- Clicking @username brings you to users page

- Customise 404 page [example](https://flask.palletsprojects.com/en/2.2.x/errorhandling/#custom-error-pages)

- A detail view to show a single shout. Click a shout to go to its 'page' (comments to come etc)

- Like / unlike a shout. (on shouts not authored by current user)

- Comments / replies

- Labels/Hashtag etc. Clicking a label shows all the posts with that label

- Pagination (Show most recent X amount of shouts with a load more button?)
### Usage
> Within the shoutr directory - create a file called env_vars and create a variable called SECRET_KEY and assign a value to it. This covers the import within \__init__.py
>
>Once that is assigned, make use of the bash file by running the below command from the root directory
```
bash runApp.sh
```