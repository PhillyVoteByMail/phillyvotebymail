const ballotStatusTrackerUrl =
    'https://www.pavoterservices.pa.gov/Pages/BallotTracking.aspx';
let index;

const voters = [
    ['Ignore this placeholder.', 'Select Philadelphia in the dropdown.', '01/01/1900'],

];

browser.runtime.onInstalled.addListener(async () => {
    console.log('onInstall()');

    // Set the index to zero on install.
    await browser.storage.local.set({ 'index': 0 });
});

browser.webNavigation.onCompleted.addListener(async (details) => {
    console.log('Ballot status tracker page loaded.');
    const tabId = details.tabId;

    // Load current index from storage. This is required in case the extension
    // is stopped/started.
    const results = await browser.storage.local.get('index');
    index = results['index'];
    console.log('index = ', index);

    if (index >= voters.length) {
        browser.tabs.sendMessage(tabId, ['All', 'Done!', '']);
        return;
    }

    // Load the correct voter to look up next.
    const voter = voters[index];
    console.log('Voter: ', JSON.stringify(voter));

    // Send the voter data to the content script.
    browser.tabs.sendMessage(tabId, voter);

    // Update and save the index.
    await browser.storage.local.set({ 'index': ++index });
}, {
    url: [
        { urlEquals: ballotStatusTrackerUrl }
    ]
});

browser.runtime.onMessage.addListener(async (results) => {
    const voter = voters[index - 2];

    console.log('===== Results received =====');
    console.log('Voter: ', JSON.stringify(voter));
    console.log('Results: ', JSON.stringify(results));
    console.log('==========');

    const voterKey = voter.join('_');
    await browser.storage.local.set({
        [voterKey]: results
    });
});
