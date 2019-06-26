function get_api_data(method, params, callback) {
    const http_request = new XMLHttpRequest();
    let p = '';
    for (let i in params) {
        p += i + '=' + params[i] + '&'
    }

    http_request.open('GET', '/api/' + method.replace('/', '') + '?' + p, true)
    http_request.send();

    http_request.onreadystatechange = function() {
        if (http_request.readyState !== 4) return;
        return callback(http_request);
    }
}


function show_page(page_name) {
    get_api_data("get_page", {
        page_name: page_name
    }, xml => {
        document.getElementById('content').innerHTML = xml.responseText
    })
}

function fix_link() {
    console.log("Started fix...");
    // Fix link
    let q = (document.querySelectorAll("a"));
    console.log(q);
    q.forEach(elem => {
        elem.setAttribute('tab_link', elem.getAttribute('href'));
        elem.removeAttribute('href');

        elem.onclick = ev => {
            ev.preventDefault();
            console.log("Link to", elem.getAttribute('tab_link'));
            show_page(elem.getAttribute('tab_link').replace('.html', ''));
            return false;
        };
    })
}

fix_link();