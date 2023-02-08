// Search component
import React, { useState, useEffect } from "react";
import CardView from "./CardView";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
import { fontSize } from "@mui/system";
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';


function Search() {
    
    // word that the user seach for
    const [serachWord, setsearchWord] = useState("");
    // indication if a word was found
    const [wordFound, setwordFound] = useState(true);
    // sets to true while the search process is running . else is false
    const [processingSearch, setProcessingSearch] = useState(false);
    // extracted data from the request of the word
    const [wordData, setWordData] = useState({
        pronunciation: " ",
        search_word : " ",
        definitions: [],
        // list of objects with the given atributes
        // definition: "provide with shelter or accommodation.",
        // emoji: null,
        // example: "they converted a disused cinema to house twelve employees",
        // image_url: null,
        // type: "verb"
    });


    const handleInputChange = (event) => {
        // const name = event.target.name
        // const value = event.target.value
        const {name, value} = event.target;

        setsearchWord(value);
    };

    const handleFormSubmission = (event) => {
        // this will cause that the normal form behaviour
        // will be prevented, whihc is the refreshing
        // of the website - it wont happen
        event.preventDefault();  
        
        const wordToSearch = serachWord;
        // console.log(serachWord)
        fetchData(wordToSearch);
        
        // reseting the word in the search box
        setsearchWord("");
    };


    const fetchData = (word) => {
        // disable the search button
        setProcessingSearch(true);
        try{
            // Using fetch to fetch the api from 
            // flask server it will be redirected to proxy
            fetch(`/get/${word}`)
                .then((res) => { 
                    if (res.status===200){
                        return res.json();
                    } else {
                        console.log(`Error: cant fetch /get/${word} : status code ${res.status}`);
                        // return an empty object
                        return {};
                    }
                })
                .then((data) => {
                    // getting the data from the server
                    // checking if the main data is in the data
                    if ('data' in data) {
                        // checking if the data was returned with the correct code
                        // on withouth any errors 
                        if (data.data.status_code === 200 && data.data.search_word && !data.data.exception && !data.data.error_message) {
                            // setting the word object that we will pass to the card
                            setWordData({
                                pronunciation: data.data.pronunciation,
                                search_word : data.data.search_word,
                                definitions: data.data.definitions,
                            });
                            // marker for sucesful found a word
                            setwordFound(true);
                            // console.log(wordData);

                        } else {
                            // empty the data 
                            setWordData({
                                pronunciation: "",
                                search_word : "",
                                definitions: [],
                            });
                            // marker for error 
                            setwordFound(false);
                        }
                    }
                })
        } catch(error) {
            console.log(error);
        }

        // enable the search button after 1,5 seconds
        setTimeout(function(){
            setProcessingSearch(false);
        }, 1500);
     
    };


    return (
        <div>
            <form className="center-element" onSubmit={handleFormSubmission}>
                <Box sx={{ boxShadow: 3,  width: '28rem', height: '10rem', backgroundColor: '#ebf7ff'}} className="center-element">
                    {/* <input 
                        name="searchWord"
                        placeholder="Serach for Word..."
                        value={serachWord}
                        onChange={handleInputChange}
                        className="input-search-box"
                    /> */}
                    <TextField 
                        id="outlined-basic" 
                        label="Serach for a Word.." 
                        variant="outlined" value={serachWord} 
                        onChange={handleInputChange}
                    />
                    <IconButton type="submit" aria-label="search" disabled={!processingSearch ? false : true}>
                        <SearchIcon sx={{fontSize:"50px"}}/>
                    </IconButton>
                </Box>
            </form>
            <div className="center-element serach-results">
                <Box sx={{ boxShadow: 3,  width: '28rem', height: '6rem', backgroundColor: 'white', textAlign: 'center'}}>
                    <Typography variant="h5" sx={{ paddingTop: '15px'}}>
                        Searched for: 
                        <Typography variant="inherit" sx={{ display:'inline', fontWeight:'bold', p:'5px'}}>
                         {wordFound ? wordData.search_word : "Not Found!"}
                        </Typography>
                    </Typography>      
                    <Typography variant="h5" sx={{ paddingBottom: '15px'}}>
                        Pronunciation: 
                        <Typography variant="inherit" sx={{ display:'inline', fontWeight:'bold', p:'5px'}}>
                        {wordData.pronunciation ?  wordData.pronunciation : "Not Defined"}
                        </Typography>
                    </Typography> 
                </Box>
            </div>
            <div>
                <CardView dataWord = {wordData}/>
            </div>
        </div>
    )
}


export default Search;