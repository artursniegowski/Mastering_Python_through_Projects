"use strict";

const clicked_to_delete = (event) => { 
    if(!confirm('Are you sure?'))
    {   
        event.preventDefault();
    }
}

const appearSpinner = (checkBoxElement, spinnerElement) => {
    checkBoxElement.classList.add("d-none");
    spinnerElement.classList.remove("d-none");
} 

const hideSpinner = (checkBoxElement, spinnerElement) => {
    spinnerElement.classList.add("d-none");
    checkBoxElement.classList.remove("d-none");
} 

// marking the task as done in the database
// sending a patch request to server and saving the data
async function mark_it_done(checkBoxId) {
    const checkedBoxElement = document.getElementById(checkBoxId);
    const checkedBoxSpinerElement = document.getElementById(checkBoxId.replace("taskCheckbox","taskCheckboxSpinner"));
    const crsf_token = document.getElementById('csrf_token').value;
    let redirectURL = checkedBoxElement.dataset.redirectUrlNext;

    appearSpinner(checkedBoxElement,checkedBoxSpinerElement);

    // selecting to set value as checked 
    try{
        await fetch(checkedBoxElement.dataset.markUrl, {
            method: "PATCH",
            headers: {
                'X-CSRF-TOKEN': crsf_token,
            }
        })
        .then(response => response.json())
        .then(response => {

            redirectURL = response.url_redirect
        })

    } catch(error){
        console.log(error)
    }

    hideSpinner(checkedBoxElement,checkedBoxSpinerElement);

    window.location.href = redirectURL
}