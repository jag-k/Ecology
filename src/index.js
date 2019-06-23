const vk = require('@vkontakte/vkui-connect-promise');

console.log();

vk.default.send('VKWebAppInit', {}) 
  .then(data => {
      console.log(`Test: ${data}`);
  }) //Обработка события EventNameResult в случае успеха 
  .catch(error => {
      console.log(`Error: ${error}`);
  }); //Обработка события EventNameFailed в случае ошибки