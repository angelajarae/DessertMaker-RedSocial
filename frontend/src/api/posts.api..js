import axios from "axios";

const postsApi=axios.create({
    baseURL:"http://localhost:8000/posts/api/posts/"

});
const recipePostsApi=axios.create({
    baseURL:"http://localhost:8000/posts/api/recipe-posts/"

});


export const getAllPosts=()=>postsApi.get("/");
export const createPosts=(post)=>postsApi.post("/",post);
export const getPost = (postId) => postsApi.get(`/${postId}`);


export const getAllRecipePosts=()=>recipePostsApi.get("/");