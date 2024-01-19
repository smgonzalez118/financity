import React, { useRef, useState } from 'react';
import Select from 'react-select';
import axios from 'axios';

const Portfolio = () => {
	const [selected, setSelected] = useState([]);
	const [asset, setAsset] = useState('');
	const [repited, setRepited] = useState(false);
	const [carteraOpt, setCarteraOpt] = useState();
	const [metric, setMetric] = useState();

	const activos = [
		{ value: 'KO', label: 'Coca Cola Company' },
		{ value: 'MSFT', label: 'Microsoft Inc' },
		{ value: 'V', label: 'Visa Inc' },
		{ value: 'TSLA', label: 'Tesla Company' },
	];

	const metrics = [
		{ value: 'riesgo', label: 'Minimizar el riesgo' },
		{ value: 'rentabilidad', label: 'Maximizar la rentabilidad' },
		{ value: 'sharpe', label: 'Optimizar relación rentabilidad-riesgo' },
		{
			value: 'sortino',
			label: 'Optimizar relación rentabilidad-riesgo a la baja',
		},
	];

	const agregar = (e) => {
		e.preventDefault();
		if (!selected.includes(e.target.selector.value)) {
			setSelected([...selected, e.target.selector.value]);
			setRepited(false);
			setMetric(e.target.metric.value);
		} else {
			setRepited(true);
		}
		console.log(`${e.target.selector.value} agregado!`);
	};

	const handlePost = (e) => {
		e.preventDefault();
		axios
			.post('http://127.0.0.1:8000/cartera/', {
				activos: selected,
				metrica: metric,
			})
			.then((response) => {
				const save = JSON.parse(response.data.carteraOptima);
				setCarteraOpt(save);
				console.log(carteraOpt);
			});
	};

	const handleReset = () => {
		setActive(false);
		setCarteraOpt([]);
		setSelected([]);
	};

	return (
		<>
			<h1>OPTIMIZA TU PORTAFOLIO</h1>
			<h3>
				Selecciona los activos de renta variable a incluir en tu portafolio y la
				métrica a optimizar (riesgo, rentabilidad, relación riesgo-rentabilidad){' '}
			</h3>

			<form id='form-port' onSubmit={(e) => agregar(e)}>
				<div className='up-container'>
					<label htmlFor='metric'>Selecciona la métrica </label>
					<select name='metric' id='metric'>
						{metrics.map((metrica, i) => (
							<option value={metrica.value} key={i}>
								{' '}
								{metrica.label}
							</option>
						))}
					</select>

					<select name='selector' id='selector'>
						{activos.map((activo, i) => (
							<option value={activo.value} key={i}>
								{' '}
								{activo.label}
							</option>
						))}
					</select>
					<input type='submit' value='Agregar!' />
				</div>
			</form>
			<button type='button' onClick={(e) => handlePost(e)}>
				OBTENER PORTAFOLIO OPTIMIZADO
			</button>

			{repited ? <h5 className='redf'>Activo ya agregado </h5> : ''}

			<div className='container'>
				<div>
					<h4 id='informative'>Activos agregados al portafolio: </h4>
					<ul>
						{selected.map((elem, i) => (
							<li key={i}>{elem}</li>
						))}
					</ul>
					<div>Data a enviar {JSON.stringify(selected)}</div>
				</div>

				<div className='results'>
					<table className='results-table'>
						<tr>
							<th>Activo</th>
							<th>Ponderacion %</th>
						</tr>
						<tbody>
							{carteraOpt &&
								Object.keys(carteraOpt).map((activo, i) => (
									<tr key={i}>
										<td>{activo}</td>
										<td>{carteraOpt[activo]}</td>
									</tr>
								))}
						</tbody>
					</table>
				</div>
			</div>
		</>
	);
};

export default Portfolio;
