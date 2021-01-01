# django_live
Good Greetings to you all, In this readme I will be explaning my django project 
1. The django settings.py
>> (A) The settings.py has me edited and configured for more reusablity, like INSTALLED_APPS is segrigated into DEFAUT_APPS + LOCAL_APPS + THIRPARTY_APPS
   (B) The second is to configure the static and media ROOT & URL, so that the static and media files are collected within the sever
   That's all with the seeable part in settings.py
   
2. The allApps, I have created a directory where my django app can reside, and now it only does consist with regiuser app which handels the USER_REGISTRATION, SELLER_REGISTRATION, and PRODUCT_MANAGEMENT, as in this app I have only used one app to so these all task, but it can be a better approch if I would have segrigated it.
  (A). models.py - models.py has the two extended classes where userProfiles and sellerProfile is extended with the auth_user model with OneToOneField with User, after which the user and seller table is segrigated and then proccessed, there is one more model products which consist of product detalis which is connected with the sellerProfile.seername_id so when a seller add;s a product it can be having a seller details with it.
  
3. forms.py & views.py - The forms.py consist of custom forms which are modified as pe the need's, and the views.py for the all proccess.
4. admin.py - admin.py is added with all the models.
5 The site is hosted on pythonanywhere.com - Anyone can acces the site through http://neerajrana.pythonanywhere.com/
