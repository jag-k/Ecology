const loader_div = '<div id="loader"></div>';

function get_api_data(method, params, callback) {
    const http_request = new XMLHttpRequest();
    let p = '';
    for (let i in params) {
        p += i + '=' + params[i] + '&'
    }

    http_request.open('GET', '/api/' + method.replace('/', '') + '?' + p, true)
    try{
        http_request.send();
        document.body.innerHTML = loader_div + document.body.innerHTML
    }
    catch{
        console.error('Error in xhr');
    }
    http_request.onreadystatechange = function() {
        if (http_request.readyState !== 4) return;
        document.getElementById('loader').remove();
        return callback(http_request);
    }
}


function show_page(page_name) {
    //var run_on_server = !!location.href.indexOf('file://'); //debug code
    let run_on_server = true;
    if(run_on_server){
        get_api_data("get_page", {
            page_name: page_name
        }, xml => {
            document.getElementById('content').innerHTML = xml.responseText;
            fix_link();
        })
    }
    else location.href=page_name.slice(1);
}

function fix_link() {
    console.log("Started fix...");
    // Fix link
    let q = (document.querySelectorAll("a"));
    //console.log(q);
    q.forEach(elem => {
        elem.setAttribute('tab_link', elem.getAttribute('href'));
        elem.removeAttribute('href');

        elem.onclick = ev => {
            ev.preventDefault();
            console.log("Link to", elem.getAttribute('tab_link'));
            show_page(elem.getAttribute('tab_link').slice(1).replace('.html', ''));
            return false;
        };
    })
}

fix_link();