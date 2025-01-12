
# Testing

Return back to the [README.md](README.md) file.

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)

- [Browser Compatibility](#browser-compatibility)

- [Responsiveness](#responsiveness)

- [Defensive Programming](#defensive-programming)

- [User Story Testing](#user-story-testing)

</details>

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
The validator picked up the ame error for all pages tested, this is due to using Jinja templating.

| Page | W3C URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| add_category | [W3C](https://workout-project3-8b4d937e7508.herokuapp.com/add_category) | ![screenshot](documentation/validators/add_category.png) | Section lacks header h2-h6 warning |
| add_workout| [W3C](https://workout-project3-8b4d937e7508.herokuapp.com/add_workout) | ![screenshot](documentation/validators/add_workout.png) | Section lacks header h2-h6 warning|
| base | [W3C]() | ![screenshot](documentation/validators/base.png) | Section lacks header h2-h6 warning |
| get_categories | [W3C](https://workout-project3-8b4d937e7508.herokuapp.com/get_categories) | ![screenshot](documentation/validators/categories.png) | Section lacks header h2-h6 warning |
| edit_category | [W3C](https://workout-project3-8b4d937e7508.herokuapp.com/edit_category) | ![screenshot](documentation/validators/edit_category.png) | Section lacks header h2-h6 warning |
| edit_workout| [W3C](https://workout-project3-8b4d937e7508.herokuapp.com/edit_workout) | ![screenshot](documentation/validators/edit_workout.png) | Section lacks header h2-h6 warning |
| login | [W3C](https://workout-project3-8b4d937e7508.herokuapp.com/login) | ![screenshot](documentation/validators/login.png) | Section lacks header h2-h6 warning |
| register | [W3C](https://workout-project3-8b4d937e7508.herokuapp.com/register) | ![screenshot](documentation/validators/register.png) | Section lacks header h2-h6 warning |
| tasks | [W3C](https://workout-project3-8b4d937e7508.herokuapp.com/get_tasks) | ![screenshot](documentation/validators/tasks.png) | Section lacks header h2-h6 warning |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](documentation/validators/css.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| :---: | :---: | :---: |
| script.js | ![screenshot](documentation/validators/javascript.png) | 	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). As this is direct code copied and pasted from Materialize, I did not change it. |

## Browser Compatibility

I have tested Your Weather on the following browsers to check for compatibility issues.

| Browser | Main | Login | Register | New Workout | Categories | Edit Category | Profile |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Chrome](https://www.google.com/chrome) | ![screenshot](documentation/browsers/chrome/chrome-home.png) | ![screenshot](documentation/browsers/chrome/chrome-login.png) | ![screenshot](documentation/browsers/chrome/chrome-register.png) | ![screenshot](documentation/browsers/chrome/chrome-new-workout.png) | ![screenshot](documentation/browsers/chrome/chrome-categories.png) | ![screenshot](documentation/browsers/chrome/chrome-edit-category.png) | ![screenshot](documentation/browsers/chrome/chrome-profile.png) | Works as expected |
| [Firefox](https://www.google.com/firefox) | ![screenshot](documentation/browsers/firefox/firefox-home.png) | ![screenshot](documentation/browsers/firefox/firefox-login.png) | ![screenshot](documentation/browsers/firefox/firefox-register.png) | ![screenshot](documentation/browsers/firefox/firefox-new-workout.png) | ![screenshot](documentation/browsers/firefox/firefox-categories.png) | ![screenshot](documentation/browsers/firefox/firefox-edit-category.png) | ![screenshot](documentation/browsers/firefox/firefox-profile.png) | Works as expected |
| [Edge](https://www.microsoft.com/en-us/edge/?form=MA13FJ) | ![screenshot](documentation/browsers/edge/edge-home.png) | ![screenshot](documentation/browsers/edge/edge-login.png) | ![screenshot](documentation/browsers/edge/edge-register.png) | ![screenshot](documentation/browsers/edge/edge-new-workout.png) | ![screenshot](documentation/browsers/edge/edge-categories.png) | ![screenshot](documentation/browsers/edge/edge-edit-category.png) | ![screenshot](documentation/browsers/edge/edge-profile.png) | Works as expected |
| [Safari](https://www.apple.com/safari/) | ![screenshot](documentation/browsers/safari/safari-home.png) | ![screenshot](documentation/browsers/safari/safari-login.png) | ![screenshot](documentation/browsers/safari/safari-register.png) | ![screenshot](documentation/browsers/safari/safari-new-workout.png) | ![screenshot](documentation/browsers/safari/safari-categories.png) | ![screenshot](documentation/browsers/safari/safari-edit-category.png) | ![screenshot](documentation/browsers/safari/safari-profile.png) | Works as expected |

## Responsiveness

I have tested my deployed project on multiple devices to check for responsiveness issues.

<details>
<summary>Click for report</summary>

| Device | Main | Login | Register| New Workout | Categories | Edit_Category | Profile |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Mobile (iPhone 15 Pro) | ![screenshot](documentation/responsiveness/iphone/iphone-home.PNG) | ![screenshot](documentation/responsiveness/iphone/iphone-login.PNG) | ![screenshot](documentation/responsiveness/iphone/iphone-register.PNG) | ![screenshot](documentation/responsiveness/iphone/iphone-add-workout.PNG) | ![screenshot](documentation/responsiveness/iphone/iphone-categories.PNG) | ![screenshot](documentation/responsiveness/iphone/iphone-edit-category.PNG) | ![screenshot](documentation/responsiveness/iphone/iphone-profile.PNG) | Some styling issues, but nothing that affects function. |
| Tablet (iPad Air) | ![screenshot](documentation/responsiveness/ipad/ipad-home.PNG) | ![screenshot](documentation/responsiveness/ipad/ipad-login.PNG) | ![screenshot](documentation/responsiveness/ipad/ipad-register.PNG) | ![screenshot](documentation/responsiveness/ipad/ipad-add-workout.PNG) | ![screenshot](documentation/responsiveness/ipad/ipad-categories.PNG) | ![screenshot](documentation/responsiveness/ipad/ipad-edit-category.PNG) | ![screenshot](documentation/responsiveness/ipad/ipad-profile.PNG) | No Issues |
| 13" Macbook Pro| ![screenshot](documentation/responsiveness/macbook/macbook-home.png) | ![screenshot](documentation/responsiveness/macbook/macbook-login.png) | ![screenshot](documentation/responsiveness/macbook/macbook-register.png) | ![screenshot](documentation/responsiveness/macbook/macbook-new-workout.png) | ![screenshot](documentation/responsiveness/macbook/macbook-categories.png) | ![screenshot](documentation/responsiveness/macbook/macbook-edit-category.png) | ![screenshot](documentation/responsiveness/macbook/macbook-profile.png) | No Issues |
| 15" Windows Laptop | ![screenshot](documentation/responsiveness/laptop/laptop-home.png) | ![screenshot](documentation/responsiveness/laptop/laptop-login.png) | ![screenshot](documentation/responsiveness/laptop/laptop-register.png) | ![screenshot](documentation/responsiveness/laptop/laptop-add-workout.png) | ![screenshot]() | ![screenshot]() | ![screenshot](documentation/responsiveness/laptop/laptop-profile.png) | User was not an admin so did not have access to categories. No Issues reported.  |
| Android Phone | ![screenshot](documentation/responsiveness/android/android-home.png) | ![screenshot](documentation/responsiveness/android/android-login.png) | ![screenshot](documentation/responsiveness/android/android-register.png) | ![screenshot](documentation/responsiveness/android/android-add-workout.png) | ![screenshot]() | ![screenshot](documentation/responsiveness/android/android-edit-workout.png) | ![screenshot](documentation/responsiveness/android/android-profile.png) | User was not an admin so did not have access to categories. No Issues reported. |

</details>

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

<details>
<summary>Click for report</summary>

| Page | Expectation | Test | Result | Fix | Screenshot |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Main | | | | | |
| | WorkoutCrew is expected to have a homepage that shows the workouts added by users that can then be previewed as a dropdown by clicking on them. | Tested this by opening the home page and clicking on the workouts. | The feature behaved as expected.| Test passed. | ![screenshot](documentation/defensive/defensive-home-dropdown.png) |
| Main | | | | | |
| | WorkoutCrew has a search function on the homepage for users to search workouts by keywords. If the keyword isn't there an appropriate result is shown.  | Tested the feature by searching a keyword in the database and one that was not. | The feature behaved as expected, and it opened the modal. | Test concluded and passed. | ![screenshot](documentation/defensive/defensive-search-keyword.png) [screenshot](documentation/defensive/defensive-search-unknown.png)|
| Register | | | | | |
| | WorkoutCrew has a page where users can register a username and password. The password has character restrictions. | Tested the feature by filling in the form. | The feature behaved as expected, but needed info on the password requirements. | Edited the page with info, tested again and passed. | ![screenshot](documentation/defensive/defensive-register.png) |
| New Workout | | | | | |
| | WorkoutCrew has a page where users can fill in a form to add their own workouts to the database. | Tested the feature by clicking New Workout and filling in the form. | The feature behaved as expected by opening the form, the datepicker worked and submitted to the homepage. | Test concluded and passed. | ![screenshot](documentation/defensive/defensive-new-workout.png) |
| Edit Workout | | | | | |
| | WorkoutCrew homepage list has an edit button that allows the owner or admin to edit the workout. A form is loaded and pre-filled with the previous information. | Tested the feature by clicking the edit button. | The feature worked but the multiple choice picker was not pre-filled. | No fix has been found for the prefill, this will be fixed in future update. | ![screenshot](documentation/defensive/defensive-edit-workout.png) |
| Edit Workout | | | | | |
| | WorkoutCrew homepage list has a 'done' button that allows the user to delete the workout. | Tested the feature by clicking the done button. | The feature behaved as expected, but does not have a confirm deletion modal. | Attempted to input a modal as a confirmation to deletion but it would not function, this will be fixed in a future update. | ![screenshot](documentation/defensive/defensive-delete-workout.png) |
| Edit Categories | | | | | |
| | WorkoutCrew admin has the ability to manage the categories by adding, editing and deleting the categories. | Tested the feature by clicking Manage Categories, edit & delete. | The feature behaved as expected, but had the same issue with deletion of no confirmation modal. | Attempted to input a modal but it would not function, this will be fixed in a future update. | ![screenshot](documentation/defensive/defensive-categories.png) ![screenshot](documentation/defensive/defensive-edit-category.png) ![screenshot](documentation/defensive/defensive-delete-category.png)|
| Login | | | | | |
| | WorkoutCrew is expected to log the user in when the user clicks the login in the top right corner and inputs the correct details then redirects to their profile page. | Tested the feature by clicking Login and signed in. | The feature behaved as expected, and it logged the user in. | Test concluded and passed. | ![screenshot](documentation/defensive/defensive-login.png) |
| Logout | | | | | |
| | WorkoutCrew is expected to log the user out when the user clicks the logout in the top right corner. | Tested the feature by clicking Logout. | The feature behaved as expected, and it logged the user out. | Test concluded and passed. | ![screenshot](documentation/defensive/defensive-logout.png) |



</details>

## User Story Testing

| User Story | Screenshot |
| :---: | :---: |
| As a new site user, I would like to know what the site is about, so that I understand what the site does. | ![screenshot](documentation/users/user-purpose.png) |
| - As a new site user, I would like to search the database for exercises.| ![screenshot](documentation/users/user-search-exercise.png) |
| As a new site user, I would like to search the database for body parts (targeted exercises) | ![screenshot](documentation/users/user-search-bodypart.png) |
| As a new site user, I would like to search workouts that exist as well as add new workouts. | ![screenshot](documentation/users/user-search-bodypart.png) ![screenshot](documentation/users/user-search-bodypart.png) |
| - As a new site user, I would like to have an overview of the upcoming workouts. | ![screenshot](documentation/users/user-home.png) |
| - As a returning site user, I would like to search the database for specific exercises. | ![screenshot](documentation/users/user-search-exercise.png) |
| - As a returning site user, I would like to be able to change/edit/delete the workouts I have added. | ![screenshot](documentation/users/user-edit-workout.png) |
| - As a returning site user, I would like to be able to sign in with ease. | ![screenshot](documentation/users/user-signin.png) |

