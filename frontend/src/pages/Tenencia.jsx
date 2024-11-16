import axios from 'axios';
import React, { useEffect, useState } from 'react';

const Tenencia = () => {
	const [data, setData] = useState('');
    
    useEffect(() => {
        axios.get('https://smgonzalez118.pythonanywhere.com/tenencia/')
        .then(response => {
            setData(response.data);
        })
        .catch(e => {
            setData(e)
        })

      }
    , [])
    

    return (
		<>
			<h1>Tenencia</h1>
			<h3>
				{data? data : "Cargando..."}
			</h3>
		</>
	);
};

export default Tenencia;
