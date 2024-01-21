import React, { useInsertionEffect, useRef } from 'react';
import { NavLink } from 'react-router-dom';

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
					<img src='assets/chevron.svg' alt='Chevron' />
				</span>
				<img src='assets/logo.png' className='logo' alt='Laplace Logo' />
				<h3 className='hide'> Financity </h3>
			</div>
			<div className='sidebar-links'>
				<ul>
					<li>
						<NavLink to='/home' onClick={(event) => handleActive(event)}>
							<div className='icon'>
								<img src='src/assets/portfolio.svg' title='Portfolio Icon' />
							</div>
							<span className='link hide'>Portfolio</span>
						</NavLink>
					</li>
					<li>
						<NavLink to='/analytics' onClick={(event) => handleActive(event)}>
							<div className='icon'>
								<img src='src/assets/analytics.svg' title='Analytics Icon' />
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
								<img src='src/assets/dashboard.svg' title='Performance Icon' />
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
								<img src='src/assets/reports.svg' title='Reports Icon' />
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
