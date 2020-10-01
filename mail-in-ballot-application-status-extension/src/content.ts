const firstNameId = '#ctl00_ContentPlaceHolder1_FirstNameText';
const lastNameId = '#ctl00_ContentPlaceHolder1_LastNameText';
const dobId = '#ctl00_ContentPlaceHolder1_DateOfBirthText';
const formId = '#aspnetForm';
const resultTableCells =
    '#ctl00_ContentPlaceHolder1_ResultPanel table tr+tr+tr td';

function insertVoterData(voterData) {
    const lastName = voterData[0];
    const firstName = voterData[1];
    const dob = voterData[2];

    console.log('Entering voter: ', JSON.stringify(voterData));

    const firstNameInput = document.querySelector(firstNameId);
    (firstNameInput as HTMLInputElement).value = firstName;

    const lastNameInput = document.querySelector(lastNameId);
    (lastNameInput as HTMLInputElement).value = lastName;

    const dobNameInput = document.querySelector(dobId);
    (dobNameInput as HTMLInputElement).value = dob;
}

function getResults() {
    let results: string[] = [];
    const tableCells = document.querySelectorAll(resultTableCells);

    if (tableCells.length > 0) {
        for (let i = 0; i < tableCells.length; i++) {
            const cell = tableCells[i];
            let cellText = (cell as HTMLTableCellElement).textContent || '';
            cellText = cellText.trim();
            results.push(cellText);
        }
        browser.runtime.sendMessage(results);
    }
}

// window.addEventListener('DOMContentLoaded', (event) => {
//     console.log('DOM fully loaded and parsed');
// });

browser.runtime.onMessage.addListener((msg) => {
    console.log('Received message: ', JSON.stringify(msg));
    // const type = msg.type;
    // const payload = msg.payload;

    // if (type === 'voterData') {
    //     insertVoterData(payload);
    // } else if (type === 'getResults') {
    //     getResults();
    // }
    insertVoterData(msg);
    getResults();
});
