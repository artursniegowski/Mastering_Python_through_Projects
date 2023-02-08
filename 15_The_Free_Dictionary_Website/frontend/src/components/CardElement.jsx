// Card component
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';

function CardElement(props) {

    return (
        <Card sx={{ maxWidth: 300 }} className="card-element">
            {props.data.image_url && 
            <CardMedia
                sx={{ height: 300,  backgroundSize:'contain'  }}
                image={ props.data.image_url }
                title={ props.word }
            />}
            <CardContent>
                <Typography gutterBottom variant="h4" component="div">
                    { props.word } { props.data.emoji }
                </Typography>
                <Typography sx={{ mb: 1.5 }} variant="h6" color="text.secondary">
                    { props.data.type }
                </Typography>
                { props.data.definition &&
                <Typography variant="body2" sx={{ mb: 1.5 }}>
                    { props.data.definition }
                </Typography>}
                { props.data.example &&
                <Typography variant="body1" color="text.secondary">
                    "{ props.data.example }"
                </Typography>}
            </CardContent>
        </Card>
    );
}

export default CardElement;