### What it does?

It will allow users to register on a site.

### How?

* When users register, a User instance will be created in the database.
* There will be url which shows user registration form.
* A UserRegistrationForm is needed.
* People should be able to use UserRegistrationForm or their own form they write.
* They might ask a lot of information during registration.
* All form data must be passed in the signal.
* Provide a default template which uses registration form.
* People should be able to provide another template name to be used.
* On form POST:
    * Create User instance
    * People can write custom form which contains only subset of User fields. So that data needs to be properly saved. So assume form field names will map to User field names.
* On successfule POST, redirect to a page saying User is registered.
* Need a separate page which says User registered. This requires a view. Needs a template. Allow customising this template.

### Later
* Allow custom user models to be used.
