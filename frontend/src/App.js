import {useEffect, useState} from "react";
import axios from "axios";

const App = () => {
    const [cars, setCars] = useState([])

    useEffect(() => {
        axios.get('/api/cars').then(({data}) => {
            setCars(data.data)
            // console.log(data.data)
        })
    }, []);

    return (
        <div>
            <h1>Cars</h1>
            {cars.map(car =>
                    <div key={car.id}>
                        <h3>ID: {car.id}</h3>
                        <div>MODEL: {car.model}</div>
                        <div>PRICE: {car.price}</div>
                        <div>YEAR: {car.year}</div>
                        <img src={car.photo} alt={car.model} width='150px'/>
                    </div>
            )}
        </div>
    );
};

export {App};