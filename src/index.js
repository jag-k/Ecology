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
        let res = http_request.responseText;
        try {
            res = JSON.parse(res);
            return callback(res)
        } catch {
            console.log("RESPONSE TEXT:", res);
        }
    }
}


function show_page(page_name, params) {
    let p = {
        page_name: page_name,
        user_id: localStorage.getItem('user_id')
    };
    console.log("PARAMS:", params);
    if (params) {
        params.split('&').forEach(i => {
            let [key, value] = i.split('=');
            p[key] = value
        })
    }
    console.log("Show page with params:", p);
    get_api_data("get_page", p, data => {
        document.getElementById('content').innerHTML = data.page;
        if (data.call_func) {
            eval(data.call_func + "(data)");
        }
        fix_link();
    })
}

function fix_link() {
    console.log("Started fix...");
    // Fix link
    let q = (document.querySelectorAll("a"));
    //console.log(q);
    let quest_count = 0;
    q.forEach(elem => {
        elem.setAttribute('tab_link', elem.getAttribute('href'));
        elem.setAttribute('href', '');
        elem.removeAttribute('href');
        let href = elem.getAttribute('tab_link');
        switch (href) {
            case '/quest_page.html':
                elem.setAttribute('tab_link',
                    '/quest_page');
                quest_count++;
                elem.setAttribute('params',
                    'quest_id=' + quest_count + '&user_id=' + localStorage.getItem('user_id'))
        }

        elem.onclick = ev => {
            ev.preventDefault();
            console.log("Link to", elem.getAttribute('tab_link'));
            show_page(elem.getAttribute('tab_link').slice(1).replace('.html', ''),
                elem.getAttribute('params'));
            return false;
        };
    })
}

function quest_init(raw_data) {
    let data = raw_data.data;
    let body = document.getElementById('text');
    document.getElementById('header_main').innerText = data.header;
    data.body.forEach(elem => {
        body.innerHTML += '<div class="fact">' + elem.header + '</div>' +
            '<div class="fact2">' + elem.text + '</div> <br />'
    });
    document.getElementById('header_fix').innerText = data.howto.header;
    document.getElementById('content_fix').innerText = data.howto.text;
    console.log(data)
}

// SLIDES
/* Индекс слайда по умолчанию */
var slideIndex = 1;

/* Функция увеличивает индекс на 1, показывает следующй слайд*/
function plusSlide() {
    showSlides(slideIndex += 1);
}

/* Функция уменьшяет индекс на 1, показывает предыдущий слайд*/
function minusSlide() {
    showSlides(slideIndex -= 1);
}

/* Устанавливает текущий слайд */
function currentSlide(n) {
    showSlides(slideIndex = n);
}

/* Основная функция сладера */
function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("item");
    var dots = document.getElementsByClassName("slider-dots_item");
    console.log(n);
    console.log(slides);
    console.log(dots);
    if (n > slides.length) {
      slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
    // var d = data[Object.keys(data)[slideIndex-1]];
    // var problem = document.getElementsByClassName('text')[0];
    // var solution = document.getElementsByClassName('text')[1];
    // problem.innerHTML = d.problem;
    // solution.innerHTML = d.solution;
}

function init_slider(data) {
    let n = data.data;
    let dots = document.getElementsByClassName("slider-dots_item");
    let [slider_button_back, slider_button_next] = document.getElementsByClassName('slider-button');
    console.log(slider_button_back, slider_button_next);

    for (i = 0; i < dots.length; i++) {
        dots[i].addEventListener('click', d => currentSlide(i));
    }
    slider_button_next.addEventListener('click', plusSlide);
    slider_button_back.addEventListener('click', minusSlide);
    showSlides(n);
}

fix_link();