import {Link} from "react-router-dom";

import styles from "./SideBar.module.css";

import chefIcon from "./images/chefIcon.svg"; 
import exitIcon from "./images/exitIcon.svg"; 
import homeIcon from "./images/homeIcon.svg"; 

export function SideBar(){
    return(
        <>
            <aside className={styles.sideBarContainer}>
                <div className={styles.sideBar}>
                    <div className={styles.buttomsBar}>
                        <Link to="/home"><img src={homeIcon}></img></Link>
                        <Link to="/profile"><img src={chefIcon}></img></Link>
                        <Link to="/login"><img src={exitIcon}></img></Link>
                        
                    </div>
                    <div className={styles.contentBar}>
                        a
                    </div>
                </div>
            </aside>
            
            
        </>
    );
}