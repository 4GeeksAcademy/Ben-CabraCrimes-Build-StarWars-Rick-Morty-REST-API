import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Card } from "../component/card";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container d-flex mx-auto row text-center mt-5">

			<h1>Home Page</h1>



			<div className="d-flex overflow-auto">
				{store.favourites.map((favourite, index) => {
					return <Card key={index} favourites={favourite} />
				})}
			</div>

		</div>
	);
};
