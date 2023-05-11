import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<button className="btn btn-primary">Home</button>
				</Link>
				<div className="ml-auto">
					<Link to="/login">
						<button className="btn btn-success me-3">Login</button>
					</Link>
					<Link to="/register">
						<button className="btn btn-primary">Register</button>
					</Link>
				</div>
			</div>
		</nav>
	);
};
