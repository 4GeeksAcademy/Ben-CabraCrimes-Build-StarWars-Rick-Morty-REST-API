import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import { Card } from "../component/card";

export const Home = () => {
	const { store, actions } = useContext(Context);

	useEffect(() => {
		actions.getFavourite();
	}, [store.token])

	return (
		<div className="container d-flex mx-auto row text-center mt-5">

			<h1>Home Page</h1>

			{/* <div className="d-flex overflow-auto"> */}
			<div>
				{store.favourites ? store.favourites.map((favourite, index) => {
					return <Card key={index} favourites={favourite} />
				}) : <div className="d-flex "> <h5 className="mt-5 fw-light">Welcome, please login or register</h5>
				</div>}
			</div>

		</div>
	);
};
