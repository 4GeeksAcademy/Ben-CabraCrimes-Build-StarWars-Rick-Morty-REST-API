const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			people: [],

			favourites: []

		},
		actions: {

			getAllPeople: async () => {
				const response = await fetch(process.env.BACKEND_URL + "/api/favorites/people");
				const data = await response.json();
				setStore({ favourite: data.people_favourites_serialized })
			},

			getAllFavouriteUserLocations: async () => {
				const response = await fetch(process.env.BACKEND_URL + "/api/user_1/favourites/location");
				const data = await response.json();
				setStore({ favourites: data.location_favourite })

			}

		}
	}

};

export default getState;
