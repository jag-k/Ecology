import connect from '@vkontakte/vkui-connect-promise';

(async () => {
    try {
        // Initialize web app
        await connect.send('VKWebAppInit', {});
        // await connect.send("VKWebAppGetGeodata", {});

    } catch (e) {
        console.error(`Error initialize web app: ${e}`);
    }
})();