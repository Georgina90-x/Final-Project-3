
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

- [Bugs](#bugs)

- [Unfixed Bugs](#unfixed-bugs)

</details>

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

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
| 15" Windows Laptop | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Notes |
| Android Phone | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Notes |

</details>

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

<details>
<summary>Click for report</summary>

| Page | Expectation | Test | Result | Fix | Screenshot |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Main | | | | | |
| | About Your Weather is expected to open a modal with information about the site when the user clicks on the About Your Weather button. | Tested the feature by clicking About Your Weather. | The feature behaved as expected, and it opened the modal. | Test concluded and passed. | ![screenshot]() |
| Login | | | | | |
| | About Your Weather is expected to open a modal with information about the site when the user clicks on the About Your Weather button. | Tested the feature by clicking About Your Weather. | The feature behaved as expected, and it opened the modal. | Test concluded and passed. | ![screenshot]() |
| Register | | | | | |
| | About Your Weather is expected to open a modal with information about the site when the user clicks on the About Your Weather button. | Tested the feature by clicking About Your Weather. | The feature behaved as expected, and it opened the modal. | Test concluded and passed. | ![screenshot]() |
| New Workout | | | | | |
| | About Your Weather is expected to open a modal with information about the site when the user clicks on the About Your Weather button. | Tested the feature by clicking About Your Weather. | The feature behaved as expected, and it opened the modal. | Test concluded and passed. | ![screenshot]() |
| Edit Workout | | | | | |
| | About Your Weather is expected to open a modal with information about the site when the user clicks on the About Your Weather button. | Tested the feature by clicking About Your Weather. | The feature behaved as expected, and it opened the modal. | Test concluded and passed. | ![screenshot]() |
| Categories | | | | | |
| | About Your Weather is expected to open a modal with information about the site when the user clicks on the About Your Weather button. | Tested the feature by clicking About Your Weather. | The feature behaved as expected, and it opened the modal. | Test concluded and passed. | ![screenshot]() |
| Edit Categories | | | | | |
| | About Your Weather is expected to open a modal with information about the site when the user clicks on the About Your Weather button. | Tested the feature by clicking About Your Weather. | The feature behaved as expected, and it opened the modal. | Test concluded and passed. | ![screenshot]() |
| Search | | | | | |
| | About Your Weather is expected to open a modal with information about the site when the user clicks on the About Your Weather button. | Tested the feature by clicking About Your Weather. | The feature behaved as expected, and it opened the modal. | Test concluded and passed. | ![screenshot]() |



</details>

## User Story Testing

| User Story | Screenshot |
| :---: | :---: |
| As a new site user, I would like to know what the site is about, so that I understand what the site does. | ![screenshot](documentation/features/modal.png) |
| - As a new site user, I would like to search the database for exercises.| ![screenshot]() ![screenshot]() |
| As a new site user, I would like to search the database for body parts (targeted exercises) | ![screenshot]() ![screenshot]() |
| As a new site user, I would like to search categories that exist as well as add new categories. | ![screenshot]() ![screenshot]() |
| - As a new site user, I would like to have an overview of the upcoming workouts. | ![screenshot]() ![screenshot]() |
| - As a returning site user, I would like to search the database for specific exercises. | ![screenshot]() ![screenshot]() |
| - As a returning site user, I would like to be able to change/edit/delete the workouts I have added. | ![screenshot]() ![screenshot]() |
| - As a returning site user, I would like to be able to sign in with ease. | ![screenshot]() ![screenshot]() |


## Bugs

The following are bugs that I have come across while creating the Your Weather site.

- Timezone displayed instead of city - The data being displayed was pulled from the timezone and not the city name.

| Original image | Bug fixed image |
| :---: | :---: |
| ![screenshot](documentation/bugs/miami-new-york-timezone.png) | ![screenshot](documentation/bugs/miami-city.png) |
| ![screenshot](documentation/bugs/hendon-london-timezone.png) | ![screenshot](documentation/bugs/hendon-town.png)

- To fix this I removed the const variable that was calling that data from the api enabling the HTML to use the place name from the input field instead.

***

- Initial Sunrise and Sunset times displayed as GMT timezone.

| Original image | Bug fixed image |
| :---: | :---: |
| ![screenshot](documentation/bugs/sunrise-set-gmt-date.png) | ![screenshot](documentation/bugs/sunrise-set-timezone-offset.png)

- To fix this I added a timezone offset and formatted the data to display only the time for the timezone of the city requested.

## Unfixed Bugs

| Error | Screenshot | Description |
| :---: | :---: | :---: |
| Permission policy error - Chrome devtools gives this google floc warning on the version that I am using. It appears to be a deprecated trial for data collection instead of using cookies. | ![screenshot](documentation/bugs/google-floc-warning.png) | I was unsuccessful at fixing this, however this does not affect the operation of the site and this trial operation is also blocked by GitHub as it breaks privacy policy. |
| The 404 page does not pick up the css if an error is created on the end of a .html url. | e.g. boderg.github.io/your-weather/index.html/data ![screenshot](documentation/bugs/html-error.png) | I was unable to fix this error but the 404 error does appear and the link button does work to return to the main page. I feel this is acceptable as it is an unlikely scenario to enter a url in this fashion. |

There are no remaining bugs that I am aware of.
