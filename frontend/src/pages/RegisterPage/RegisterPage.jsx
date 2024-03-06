import {Helmet} from "react-helmet";
import {useForm} from "react-hook-form";
import {useNavigate} from "react-router-dom";

import styles from "./RegisterPage.module.css";
import ChefIcon from "./images/ChefIcon.svg";

import {createUserProfile} from "../../api/users.api";




export function RegisterPage(){

    const navigate=useNavigate();
    const {register,handleSubmit}=useForm();




    const onSubmit=handleSubmit (data=>{
        createUserProfile(data);
    });

    function handleLogin(){
        navigate("/login");
    };



    return(
        <>
            <Helmet>
                <title>Register • DessertMaker</title>
            </Helmet>

            <section className={styles.contentContainer}>
                <section className={styles.content}>
                    <div className={styles.imgContainer}>
                        <img src={ChefIcon}/>  
                    </div>

                    <div className={styles.formContainer}>
                        <div className={styles.backgroundDecoration}>
                            
                        </div>
                        <form onSubmit={onSubmit}>
                            <h1>Register</h1>

                            <input type="text" 
                            placeholder="Name"
                            {...register("name",{required:true})}>
                            </input> 

                            <input type="text" 
                            placeholder="Username"
                            {...register("username",{required:true})}>
                            </input> 

                            <input type="password" 
                            placeholder="Password"
                            {...register("password",{required:true})}>
                            </input> 

                            <p>Aditional information</p>

                            <input type="email" 
                            placeholder="Email"
                            {...register("email",{required:false})}>
                            </input> 

                            <input type="date" 
                            {...register("date",{required:false})}>
                            </input> 

                            <button type="submit" className={styles.registerButtom}>Register</button>

                            <button className={styles.loginButtom} onClick={handleLogin}>Login</button>
                        </form>
                    </div>
                </section>
            </section>
            
            <div className={styles.footer}>
                DessertMaker logo
            </div>
        </>    
    );
}