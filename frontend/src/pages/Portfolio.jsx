import React, { useRef, useState } from 'react';
import Select from 'react-select';
import axios from 'axios';
import { companies } from '../assets/companies';

const Portfolio = () => {
	const [selected, setSelected] = useState([]);
	const [asset, setAsset] = useState('');
	const [repited, setRepited] = useState(false);
	const [carteraOpt, setCarteraOpt] = useState();
	const [metric, setMetric] = useState();
	const [loader, setLoader] = useState();

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
		setLoader(true);
		axios
			.post('https://smgonzalez118.pythonanywhere.com/cartera/', {
				activos: selected,
				metrica: metric,
			})
			.then((response) => {
				const save = JSON.parse(response.data.carteraOptima);
				setCarteraOpt(save);
				console.log(carteraOpt);
				setLoader(false);
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
			{loader && (
				<>
					<div class='spinner'></div>
					<span id='text-loader'>Obteniendo cartera óptima ...</span>
				</>
			)}

			<form id='form-port' onSubmit={(e) => agregar(e)}>
				<div className='up-container'>
					<label htmlFor='metric'>Selecciona la métrica </label>
					<select name='metric' id='metric' className='selectors'>
						{metrics.map((metrica, i) => (
							<option value={metrica.value} key={i}>
								{' '}
								{metrica.label}
							</option>
						))}
					</select>

					<label htmlFor='selector'>Selecciona los activos </label>
					<select name='selector' id='selector' className='selectors'>
						{companies.map((activo, i) => (
							<option value={activo.ticker} key={i}>
								{' '}
								{activo.name}
							</option>
						))}
					</select>
					<input type='submit' value='Agregar activo' id='submit' />
					{repited ? <h5 className='redf'>Activo ya agregado </h5> : ''}
				</div>
			</form>

			<button type='button' id='final-button' onClick={(e) => handlePost(e)}>
				OBTENER PORTAFOLIO OPTIMIZADO
			</button>

			<div className='down-container'>
				<div>
					<h4 id='informative'>Activos agregados al portafolio: </h4>
					<ul>
						{selected.map((elem, i) => (
							<li key={i}>
								{companies.map((dic, i) => {
									if (dic['ticker'] == elem) {
										return dic['name'];
									}
								})}
							</li>
						))}
					</ul>
				</div>
				<div className='results'>
					{carteraOpt && (
						<table className='results-table'>
							<tr>
								<th>Activo</th>
								<th>Ponderacion %</th>
							</tr>
							<tbody>
								{carteraOpt &&
									Object.keys(carteraOpt).map((activo, i) => (
										<tr key={i}>
											<td>
												{companies.map((dic, i) => {
													if (dic['ticker'] == activo) {
														return dic['name'];
													}
												})}
											</td>
											<td>{carteraOpt[activo]}</td>
										</tr>
									))}
							</tbody>
						</table>
					)}
				</div>
			</div>
		</>
	);
};

export default Portfolio;
