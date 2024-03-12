/*
<div class="product" data-index="0">
    <img src="https://via.placeholder.com/150" alt="product" />
    <h2>Product 1</h2>
    <p>Price: 100$</p>
    <div class="buttons">
    <button class="heart"><i class="fas fa-heart"></i></button>
    <button class="add"><i class="fas fa-shopping-cart"></i></button>
    </div>
</div>
*/

let products = document.getElementById('products');

for (let i = 0; i < 27; i++) {
    let product = document.createElement('div');
    product.classList.add('product');
    product.setAttribute('data-index', i);

    let img = document.createElement('img');
    img.src = 'https://via.placeholder.com/150';
    img.alt = 'product';
    product.appendChild(img);

    let h2 = document.createElement('h2');
    h2.textContent = `Product ${i + 1}`;
    product.appendChild(h2);

    let p = document.createElement('p');
    p.textContent = `Price: ${Math.floor(Math.random()*50+10)}$`;
    product.appendChild(p);

    let buttons = document.createElement('div');
    buttons.classList.add('buttons');
    product.appendChild(buttons);

    let heart = document.createElement('button');
    heart.classList.add('heart');
    let iHeart = document.createElement('i');
    iHeart.classList.add('fas', 'fa-heart');
    heart.appendChild(iHeart);
    buttons.appendChild(heart);

    let add = document.createElement('button');
    add.classList.add('add');
    let iAdd = document.createElement('i');
    iAdd.classList.add('fas', 'fa-shopping-cart');
    add.appendChild(iAdd);
    buttons.appendChild(add);


    products.appendChild(product);
}