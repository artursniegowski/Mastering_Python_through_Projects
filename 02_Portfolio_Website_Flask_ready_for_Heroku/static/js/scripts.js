"use strict";

const clearDataFormContact = () => {
    const inputsForm = document.querySelectorAll('#name, #email, #phone, #message');
    inputsForm.forEach( inputForm =>{
        inputForm.value = '';
    })
}

const contactForm = document.getElementById('contactFormPortfolio');
const sucessMessageForm = document.getElementById('submitPortfolioSuccessMessage');
const errorMessageForm = document.getElementById('submiPortfoliotErrorMessage');
const submitButton = document.getElementById('submitButton');

contactForm.addEventListener('submit',async (event) => {
    event.preventDefault(); 

    submitButton.textContent = "Sending...";
    let messageSentSucess = false
    let formData = new FormData(contactForm);
    let csrf_token =  document.getElementById('csrf_token').value;
    // it will be appende automatically bc it is part of conctactForm
    // just to update the value - it is not neccessary
    formData.append('csrf_token', csrf_token);

    try {

        await fetch(contactForm.dataset.contactUrl ,{
            method: "POST",
            // this is not neccessary since we have csrf_token in the data !
            // headers: {
            //     'X-CSRF-TOKEN': csrf_token,
            //   },
            body: formData,
        })
        .then(response => response.json())
        .then(response => {

            // console.log(response);

            if ('success' in response){
                if(response['success']==='true'){
                    // message was sent sucessfuly
                    messageSentSucess = true;

                }
            }
        })

    }catch(error){
        console.log("Error occurred during communication with the Server!");
    }
        
    if (messageSentSucess){
        // message was sent sucessfuly
        sucessMessageForm.classList.remove('d-none');
        setInterval(() => {
            sucessMessageForm.classList.add('d-none')
        }, 6000);
        
        setTimeout(clearDataFormContact, 6000);

    }else{
        // message was not sent sucessfuly
        errorMessageForm.classList.remove('d-none');
        setInterval(() => {
            errorMessageForm.classList.add('d-none')
        }, 6000);  
    }

    submitButton.textContent = "Send";
});



window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    let navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 72,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});
