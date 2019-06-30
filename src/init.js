import connect from '@vkontakte/vkui-connect-promise';

(async () => {
    try {
        // Initialize web app
        await connect.send('VKWebAppInit', {});
        // await connect.send("VKWebAppGetGeodata", {});
        let user_data = await connect.send("VKWebAppGetUserInfo", {});
        console.log(user_data.data.id);
        localStorage.setItem('user_id', user_data.data.id)

    } catch (e) {
        console.error(`Error initialize web app: ${e}`);
    }
})();