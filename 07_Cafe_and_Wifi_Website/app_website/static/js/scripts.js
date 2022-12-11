"use strict";
// sending a DELETE request for deleting a cafe
const deleteCafeElement = document.getElementById('jsCafeDelete');
// if element exists
if (deleteCafeElement) {
	// sending the request based on presed element
	deleteCafeElement.addEventListener('click', async (event) => {
		// disablign natural behaviour
		event.preventDefault();
		// getting the csrf token
		// if we dont add crsf fotken into the request
		// we will get a bad request - this is a protection for
		// cross site forgery
		let crsf_token = document.getElementById('csrf_token').value;
		// sending the DELETE request
		try{
			await fetch(deleteCafeElement.dataset.deleteUrl, {
				method: "DELETE",
				headers: {
					'X-CSRF-TOKEN': crsf_token,
				}
			})
			.then(response => response.json())
			.then(response => {
				// redirecting after succsess
				if ('success' in response) {
					if (response['success'] === 'true') {
						console.log(
							// if cant read value change to default '/'
							// and redirect
							window.location.href = response.url_redirect || '/'
						)
					}
				}
			})
		}catch(error){
			
			console.log(error);
		}
	})
}
// adjusting padding of content element base on the size of sidebar
const sidebarElement = document.getElementById('sidebarElementJS');
const mainContent = document.getElementById('mainContent');
// function for adding padding based on the size
const resize_ob = new ResizeObserver(function(entries) {
	// since we are observing only a single element, so we access the first element in entries array
	let rect = entries[0].contentRect;
	// current width & height
	let width = rect.width;
	// let height = rect.height;
    // width *= 1.1;
    // adjusting the padding for the ocntent
    mainContent.style.padding = `0 0 0 ${width}px`;
});
// start observing for resize
resize_ob.observe(sidebarElement);