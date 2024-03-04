import {Helmet} from "react-helmet";
import styles from "./LoginPage.module.css";

import OvenIcon from "./images/OvenIcon.svg";

export function LoginPage(){
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
                        <form>
                            <h1>User login</h1>
                            <input type="text" placeholder="Username"></input> 
                            <input type="text" placeholder="Password"></input> 
                            <button className={styles.loginButtom}>Login</button>
                            <button className={styles.createAccountButtom}>Create an account</button>
                        </form>
                    </div>
                </section>
            </section>
            
            <div className={styles.footer}>
                a
            </div>
        </>    
    );
}