var items = document.getElementsByClassName('item');
for(let i=0;i<items.length;i++){
	let item = new Hammer(items[i]);
	item.on('swipeleft',function(e){
		console.log('swipeleft');
		minusSlide();
	});
	item.on('swiperight',function(e){
		console.log('swiperight');
		plusSlide();
	});
}