import React, { useInsertionEffect, useRef } from 'react';
import { NavLink } from 'react-router-dom';
import portfolio from '../assets/portfolio.svg';
import chevron from '../assets/chevron.svg';
import dashboard from '../assets/dashboard.svg';
import logo from '../assets/logo.png';
import reports from '../assets/reports.svg';
import analytics from '../assets/analytics.svg';

const Aside = () => {
	const handleExpand = () => {
		document.body.classList.toggle('collapsed');
	};

	const handleActive = (event) => {
		const links = document.querySelectorAll('.sidebar-links a');
		links.forEach((elem) => {
			elem.classList.remove('active');
		});
		event.currentTarget.classList.toggle('active');
	};

	return (
		<nav>
			<div className='sidebar-top'>
				<span className='expand-btn' onClick={handleExpand}>
					<img src={chevron} alt='arrow' />
				</span>
				<img src={logo} className='logo' alt='Laplace Logo' />
				<h3 className='hide'> Financity </h3>
			</div>
			<div className='sidebar-links'>
				<ul>
					<li>
						<NavLink to='/home' onClick={(event) => handleActive(event)}>
							<div className='icon'>
								<img src={portfolio} title='Portfolio Icon' />
							</div>
							<span className='link hide'>Portfolio</span>
						</NavLink>
					</li>
					<li>
						<NavLink to='/analytics' onClick={(event) => handleActive(event)}>
							<div className='icon'>
								<img src={analytics} title='Analytics Icon' />
							</div>
							<span className='link hide'>Analytics</span>
						</NavLink>
					</li>
					<li>
						<a
							href='#dashboard'
							title='Performance link'
							onClick={(event) => handleActive(event)}
						>
							<div className='icon'>
								<img src={dashboard} title='Performance Icon' />
							</div>
							<span className='link hide'>Performance</span>
						</a>
					</li>
					<li>
						<a
							href='#reports'
							title='Reports Link'
							onClick={(event) => handleActive(event)}
						>
							<div className='icon'>
								<img src={reports} title='Reports Icon' />
							</div>
							<span className='link hide'>Reports</span>
						</a>
					</li>
				</ul>
			</div>
		</nav>
	);
};

export default Aside;
