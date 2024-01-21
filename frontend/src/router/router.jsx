// This is a React Router v6 app
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Portfolio from '../components/Portfolio.jsx';

const Router = () => {
	return (
		<BrowserRouter>
			<Aside></Aside>
			<Routes>
				<Route path='#portfolio' element={<Portfolio />} />
				<Route path='/' element={<Portfolio />} />
			</Routes>
		</BrowserRouter>
	);
};
