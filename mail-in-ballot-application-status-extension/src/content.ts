const firstNameId = '#ctl00_ContentPlaceHolder1_FirstNameText';
const lastNameId = '#ctl00_ContentPlaceHolder1_LastNameText';
const dobId = '#ctl00_ContentPlaceHolder1_DateOfBirthText';
const formId = '#aspnetForm';

browser.runtime.onMessage.addListener((msg) => {
    const firstName = msg[0];
    const lastName = msg[1];
    const dob = msg[2];

    console.log('Entering voter: ', JSON.stringify(msg));

    const firstNameInput = document.querySelector(firstNameId);
    (firstNameInput as HTMLInputElement).value = firstName;

    const lastNameInput = document.querySelector(lastNameId);
    (lastNameInput as HTMLInputElement).value = lastName;

    const dobNameInput = document.querySelector(dobId);
    (dobNameInput as HTMLInputElement).value = dob;
});

window.addEventListener('load', () => {
    console.log('page is fully loaded');
});