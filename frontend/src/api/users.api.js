import axios from "axios";

const userProfilesApi=axios.create({
    baseURL:"http://localhost:8000/users/api/user-profiles/"

});


export const getAllUserProfiles=()=>userProfilesApi.get("/");
export const createUserProfile=(userProfile)=>userProfilesApi.post("/",userProfile);
export const getUserProfile = (userProfileId) => userProfilesApi.get(`/${userProfileId}`);