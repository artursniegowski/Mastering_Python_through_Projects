// header component
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { BrowserRouter, Link, Routes, Route } from "react-router-dom";
import About from './About';
import Search from './Search';

function Header() {
    return(
        <BrowserRouter>
            <Box sx={{ flexGrow: 1 }}>
                <AppBar position="static" className="my-header" sx={{ p:2 }}>
                    <Toolbar sx={{justifyContent: "space-between"}}>
                        <Typography variant="h2" sx={{ paddingLeft:2, paddingRight:2 }}>
                            <Link to="/" className='link-header'>
                                The Free Dictionary
                            </Link>
                        </Typography>
                        <Typography variant="h4" sx={{ paddingRight:10, paddingLeft:2 }}>
                            <Link to="/about" className='link-header'>
                                About
                            </Link>
                        </Typography>
                    </Toolbar>
                </AppBar>
            </Box>
        <Routes>
            <Route exact path="/" element={<Search />} /> 
            <Route path="/about" element={<About />} />
        </Routes>
        </BrowserRouter>
    ); 
}

export default Header;