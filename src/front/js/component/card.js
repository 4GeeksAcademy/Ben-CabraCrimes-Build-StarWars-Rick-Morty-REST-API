import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

export const Card = ({ favourites }) => {
    const { store, actions } = useContext(Context);

    return (
        <div className="card mx-1 col" style={{ minWidth: "16rem" }}>
            <div className="card-body">
                <h5 className="card-title">User: {favourites.user_id}</h5>
                <p className="card-text">Location: {favourites.location_id}</p>

            </div>
        </div>
    )
}