// footer component
import React, { useState, useEffect } from "react";

function Footer() {

    // creating a useState hook for the server side year
    const [serverYear, setServerYear] = useState(2022);

    // getting the current year from the server side
    // Using useEffect for single rendering
    useEffect( () => {
        try{
            // Using fetch to fetch the api from 
            // flask server it will be redirected to proxy
            fetch("/get-current-year")
                .then((res) => res.json())
                .then((data) => {
                    if ('currentYear' in data) {
                        // Setting the year from the server from api
                        setServerYear(data['currentYear']);
                    } 
                })
        } catch(error) {
            console.log(error);
        }
    }, []);

    return (
        <footer>
            Copyright ©{serverYear}. The Free Dictionary.
        </footer>
    );
}

export default Footer;