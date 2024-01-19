import React, { useRef, useState } from 'react';
import Select from 'react-select';

const Portfolio = () => {
	const activos = [
		{ value: 'KO', label: 'Coca Cola Company' },
		{ value: 'MSFT', label: 'Microsoft Inc' },
		{ value: 'V', label: 'Visa Inc' },
		{ value: 'TSLA', label: 'Tesla Company' },
	];

	const [selected, setSelected] = useState([]);
	const [asset, setAsset] = useState('');
	const [repited, setRepited] = useState(false);

	const agregar = (e) => {
		e.preventDefault();
		if (!selected.includes(e.target.selector.value)) {
			setSelected([...selected, e.target.selector.value]);
			setRepited(false);
		} else {
			setRepited(true);
		}
		console.log(`${e.target.selector.value} agregado!`);
	};

	return (
		<>
			<h1>OPTIMIZA TU PORTAFOLIO</h1>
			<h3>
				Selecciona los activos de renta variable a incluir en tu portafolio y la
				métrica a optimizar (riesgo, rentabilidad, relación riesgo-rentabilidad){' '}
			</h3>

			<form id='form-port' onSubmit={(e) => agregar(e)}>
				<select name='selector' id='selector'>
					{activos.map((activo, i) => (
						<option value={activo.value} key={i}>
							{' '}
							{activo.label}
						</option>
					))}
				</select>
				<input type='submit' value='Agregar!' />
			</form>

			<div>
				{repited ? <h5 className='redf'>Activo ya agregado </h5> : ''}
				<h4 id='informative'>Activos agregados al portafolio: </h4>
				<ul>
					{selected.map((elem, i) => (
						<li key={i}>{elem}</li>
					))}
				</ul>
				<div>Data a enviar {JSON.stringify(selected)}</div>
			</div>
		</>
	);
};

export default Portfolio;
