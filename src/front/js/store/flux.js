const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			people: [],

			favourites: [],

			token: null,

			user: {}

		},
		actions: {

			// getAllPeople: async () => {
			// 	const response = await fetch(process.env.BACKEND_URL + "/api/favorites/people");
			// 	const data = await response.json();
			// 	setStore({ favourites: data.favourite_people })
			// },

			getFavourite: async () => {
				const response = await fetch(process.env.BACKEND_URL + "/api/favourites", {
					headers: {
						"Authorization": "Bearer " + localStorage.getItem("token")
					}
				});
				const data = await response.json();
				setStore({ favourites: data.favourites })

			},

			login: async (email, password) => {
				const response = await fetch(process.env.BACKEND_URL + "/api/login", {
					method: "POST",
					headers: {
						"Content-Type": "application/json"
					},
					body: JSON.stringify({
						email: email,
						password: password
					})
				});
				if (response.ok) {
					const data = await response.json();
					localStorage.setItem("token", data.token);
					setStore({ token: data.token })
					return true;
				}
			}

		}
	}
}


export default getState;
