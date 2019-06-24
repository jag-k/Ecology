import connect from '@vkontakte/vkui-connect-promise';
require('./map.js')
(async () => {
    try {
        // Initialize web app
        await connect.send('VKWebAppInit', {})
    } catch (e) {
        console.error(`Error initialize web app: ${e}`);
    }
})();