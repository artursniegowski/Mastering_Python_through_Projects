// Card component
import CardElement from './CardElement';
import { useState, useEffect } from 'react';

function CardView(props) {

    // setting the card elements
    const [cardItem, setCardItems] = useState();
    
    // render all the card items
    const getCardItems = () => {
        setCardItems(
            props.dataWord.definitions.map((data, index)=>(
                <CardElement data={data} word={props.dataWord.search_word} key={index} />
            ))
        )
    };

    // calling getCardItems whenever dataWord from props will change
    useEffect(() => {
        getCardItems();
    }, [props.dataWord]);

    return (
        <div className="card-element-center">
            {cardItem}
        </div>
    );
}

export default CardView;