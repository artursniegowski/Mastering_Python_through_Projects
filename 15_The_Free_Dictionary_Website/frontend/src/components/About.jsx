// the about component
import Typography from '@mui/material/Typography';

function About() {
    return (
    <Typography variant="h4" sx={{ p:25, fontWeight:'bold' }}>
  The Owlbot Dictionary API (https://owlbot.info/) is used to power this free dictionary. It will search the given word in the English dictionary and return the meaning and any other information provided on the searched word. Head to the main page and start looking up the word you want to check!
    </Typography>
    )
}

export default About;