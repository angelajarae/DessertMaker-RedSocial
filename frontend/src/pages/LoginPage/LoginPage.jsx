import {Helmet} from "react-helmet";
import { useEffect,useState } from "react";
import {useForm} from "react-hook-form";
import {useNavigate} from "react-router-dom";

import styles from "./LoginPage.module.css";
import OvenIcon from "./images/OvenIcon.svg";

import {getAllUserProfiles} from "../../api/users.api";




export function LoginPage(){

    const {register,handleSubmit}=useForm();
    const [userProfiles,setUserProfiles]=useState([]);
    const navigate=useNavigate();



     
    useEffect(()=>{
        async function loadUserProfiles(){
            const res= await getAllUserProfiles();
            setUserProfiles(res.data);
            console.log(res);
        }

        loadUserProfiles();

    },[]);

    const onSubmit=handleSubmit(data=>{
        if(userProfiles.some(userProfile=>userProfile.username==data.username&&userProfile.password==data.password)){
            console.log("login");
            navigate('/home');
        }
        else{
            console.log("no login");
        }
    });

    function handleCreateAccount(){
        navigate('/register');
    }



    return(
        <>
            <Helmet>
                <title>Login • DessertMaker</title>
            </Helmet>

            <section className={styles.contentContainer}>
                <section className={styles.content}>

                    <div className={styles.imgContainer}>
                        <img src={OvenIcon}/>
                    </div>

                    <div className={styles.formContainer}>
                        <div className={styles.backgroundDecoration}>
                            
                        </div>

                        <form onSubmit={onSubmit}>
                            <h1>User login</h1>

                            <input type="text" 
                            placeholder="Username"
                            {...register("username",{required:true})}>
                            </input> 

                            <input type="password" 
                            placeholder="Password"
                            {...register("password",{required:true})}>
                            </input> 

                            <button type="submit" className={styles.loginButtom}>Login</button>
                            <button onClick={handleCreateAccount} className={styles.createAccountButtom}>Create an account</button>
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