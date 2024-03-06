import {Helmet} from "react-helmet";
import { useEffect,useState } from "react";

import writeRecipePost from "./images/writeRecipePost.svg"
import styles from "./HomePage.module.css";

import {RecipePost} from "../../components/RecipePost/RecipePost";
import {SearchBar} from "../../components/SearchBar/SearchBar";

import {getPost,getAllRecipePosts} from "../../api/posts.api.";



export function HomePage(){


    const [recipePosts,setRecipePosts]=useState([]);

    


    useEffect(()=>{

        async function loadRecipePosts(){
            const res=await getAllRecipePosts();
            setRecipePosts(res.data);
        }
        loadRecipePosts();
        
    
    },[]);




    
    return(
        <>
            <Helmet>
                <title>Home • DessertMaker</title>
            </Helmet>

            
            <section className={styles.contentContainer}>
                <SearchBar></SearchBar>

                <div className={styles.postsContainer}>
                    {recipePosts.map((recipePost)=>{
                        return <RecipePost key={recipePost.id} recipePost={recipePost}/>;
                    })}
                    
                    <img className={styles.writeRecipePost} src={writeRecipePost}></img>
                </div>
            </section>
        </>
    );
}