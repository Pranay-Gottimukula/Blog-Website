# Blog-Website
This project is part of GDSC club induction process of IIT Indore

Task-5: Full-Stack (Beginner)
Blog application supporting user and author roles

I used html, css, django, bootstrap, SQLlite for this project
This project is made in an virtual environment by me

This website is fully functional blog website

I couldn't implement JWTAuth and OAuth due to time and knowledge constraints as the project itself took a lot of time learning

Versions used are
Python==3.12.3  ;  Django==4.2  ;  Bootstrap==4.6 ; pillow==11.1.0 ; django-crispy-forms==2.3

An anonymous user can view all posts without logging in but he cannot post
A logged in user can make posts, he can manage his posts like editing and deleting

CLicking on Bloggerz Nation icon in navbar will redirect user to home page 

Starting Page shows posts of other users even though user is not logged in 
Index Page when user is not logged in --> ![Loggedout_view_index](https://github.com/user-attachments/assets/b12c3b8e-df17-44f7-a782-b5052bcdc2c9)

Users can Post in index page itself when they log in
Index Page when user is logged in --> ![Logged in_outview_index](https://github.com/user-attachments/assets/8e277284-e604-4533-94fc-0544edd4e967)

Login option is available in navbar
Login Page -->  ![LoginPage](https://github.com/user-attachments/assets/861c9e3d-f003-4da2-bb88-02a1eae4d5c1)

Signup option is available in navbar
Sign up Page -->  ![SignUpPage](https://github.com/user-attachments/assets/3d28f2c0-d98c-462f-8a61-ce8a3f58d987)

Profile can be viewed in navbar once the user is logged in
Profile Page -->  ![ProfilePage](https://github.com/user-attachments/assets/96cba32c-fd03-435e-ab15-0afbb5d97ee9)

Profile and personal details including profile picture can be changed
Profile Update Page -->  ![ProfileUpdate](https://github.com/user-attachments/assets/e280ae99-b9db-4b7e-af7e-897b07563b08)
Initial user will have a default profile picture 

My Posts section in navbar shows all posts made by user and those posts can be edited and deleted
My Posts Page -->  ![myPosts](https://github.com/user-attachments/assets/24abab4c-d0d2-4646-a619-90b24e6aa1a7)

Editing a post
Post Editor Page -->  ![postEditor](https://github.com/user-attachments/assets/e197acc0-83c1-4598-b0b9-77de90700ca4)

Deleting post feature is also there
Post Deletion confirmation Page -->  ![postDelete](https://github.com/user-attachments/assets/28bc9b13-0674-47b3-86c9-dbf0cf5f44a6)

Posts can be seen in a detailed view, we can edit or delete our posts in detailed view which can not be done with other's posts

Other's post -->  ![postDetailedothers](https://github.com/user-attachments/assets/c9b466ff-7dc1-43f3-bc14-3e81f54fcc17)
User's post -->  ![postDetailedUser](https://github.com/user-attachments/assets/fc1385a3-63a8-47c0-9a5e-f198f39e8206)

