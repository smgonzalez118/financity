import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import Portfolio from './pages/Portfolio.jsx';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Aside from './components/Aside.jsx';
import Analytics from './pages/Analytics.jsx';
import SourceCode from './pages/SourceCode.jsx';

function App() {
	return (
		<>
			<BrowserRouter>
				<Aside></Aside>
				<Routes>
					<Route path='/home' element={<Portfolio />} />
					<Route path='/analytics' element={<Analytics />} />
					<Route path='/sourcecode' element={<SourceCode />} />
					<Route path='/' element={<Portfolio />} />
				</Routes>
			</BrowserRouter>
		</>
	);
}

export default App;
