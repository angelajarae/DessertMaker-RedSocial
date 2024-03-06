import styles from "./RecipePost.module.css";

import decoration from "./Images/decoration.svg";
import recipeImage from "./Images/recipeImage.svg";
import like from "./Images/like.svg";
import repost from "./Images/repost.svg";
import save from "./Images/save.svg";
import { useState ,useEffect} from "react";
import { getUserProfile } from "../../api/users.api";
import { getPost } from "../../api/posts.api.";



export function RecipePost({recipePost}){
    
const [userProfile,setUserProfile]=useState({});



useEffect(() => {
    async function fetchUserProfile() {
        
            const post = await getPost(recipePost.post);
            const user = await getUserProfile(post.user);
            setUserProfile(user.data);
   
    }
    fetchUserProfile();
}, [recipePost]);



    return(
        <>  
            <div className={styles.recipePostsContainer}>
                
                <p className={styles.username}>@{userProfile.username}</p>
                <div className={styles.header}> </div>
                <img className={styles.decoration}src={decoration}></img>

                
                
                <div div className={styles.recipePost}>
                    <h1>Recipe name</h1>
                    <img className={styles.recipeImage} src={recipeImage}></img>

                    <div className={styles.reactions}>
                        <span><img src={like}></img> 2</span>
                        <span><img src={repost}></img> 2</span>
                        <span><img src={save}></img> 2</span>
                        
                        
                    </div>
                    <p>Description</p>
                    <p>Ingredients</p>
                </div>
                
            </div>
        </>
    );
}