function removeCol() {
    document.querySelector('.column-dh').remove();
    document.querySelectorAll('.field-dh').forEach(e => e.remove());
    document.querySelector('.column-ngay').remove();
    document.querySelectorAll('.field-ngay').forEach(e => e.remove());
    document.querySelector('.column-id').remove();
    document.querySelectorAll('.field-id').forEach(e => e.remove());

    let cnts = document.querySelectorAll('.field-ct_soluong');
    let products = document.querySelectorAll('.field-sp');
    let info = {};
    for (let i = 0; i < products.length; ++i) {
        let product = products[i];

        if (!info[product.innerHTML]) {
            info[product.innerHTML] = {
                cnt: parseInt(cnts[i].innerHTML),
                dom: product.parentNode
            }
        } else {
            info[product.innerHTML].cnt += parseInt(cnts[i].innerHTML);

            product.parentNode.remove();
        }
    };

    for (let [key, value] of Object.entries(info)) {
        value.dom.querySelector('.field-ct_soluong').innerHTML = value.cnt;
    }
}

let url = new URL(window.location.href);
if (url.searchParams.get("dh__ngay__range__gte")) {
    if (url.searchParams.get("o")) {
        setTimeout(removeCol, 200);
    } else {
        window.location.href += '&o=3';
    }
} else {
    setTimeout( () => {
        document.querySelector('.column-id_sp').remove();
        document.querySelectorAll('.field-id_sp').forEach(e => e.remove());
    }, 200);
}