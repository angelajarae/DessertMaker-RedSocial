import {Helmet} from "react-helmet";
import styles from "./RegisterPage.module.css";
import ChefIcon from "./images/ChefIcon.svg";

export function RegisterPage(){
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
                        <form>
                            <h1>Register</h1>
                            <input type="text" placeholder="Name"></input> 
                            <input type="text" placeholder="Username"></input> 
                            <input type="text" placeholder="Password"></input> 
                            <p>Aditional information</p>
                            <input type="email" placeholder="Email"></input> 
                            <input type="date" placeholder="aaa"></input> 
                            <button className={styles.registerButtom}>Register</button>
                            <button className={styles.loginButtom}>Login</button>
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