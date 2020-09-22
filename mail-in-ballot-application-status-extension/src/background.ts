const statusTrackerUrl = 'https://www.pavoterservices.pa.gov/Pages/BallotTracking.aspx';
let tabId: number | undefined;
let index = 0;

const voters = [
    ['Ignore this placeholder.', 'Select Philadelphia in the dropdown.', '01/01/1900'],
    ['Alice', 'Smith', '01/01/1990'],
    ['Bob', 'Smith', '01/01/2000'],
    ['Charlie', 'Smith', '01/01/2000'],
    ['Dee', 'Smith', '01/01/2000'],
    ['Eleanor', 'Smith', '01/01/2000'],
]

browser.runtime.onInstalled.addListener(async () => {
    console.log('onInstalled()');
    let tab = await browser.tabs.create({ url: statusTrackerUrl });
    tabId = tab.id;
});

browser.webNavigation.onCompleted.addListener(async (details) => {
    console.log('Page loaded.');
    if (details.tabId !== tabId) {
        return;
    }
    if (index > 0) {
        const prevVoter = voters[index - 1];
        console.log(
            'Page is displaying results for: ',
            JSON.stringify(prevVoter)
        );
    }

    if (index >= voters.length) {
        browser.tabs.sendMessage(tabId, ['All', 'Done!', '']);
        return;
    }

    const currentVoter = voters[index];
    console.log(
        'Telling page to fill form for next voter: ',
        JSON.stringify(currentVoter)
    );
    browser.tabs.sendMessage(tabId, currentVoter);
    index++;
}, {
    url: [
        { urlEquals: statusTrackerUrl }
    ]
});
