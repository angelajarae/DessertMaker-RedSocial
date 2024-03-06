import styles from "./SearchBar.module.css";


export function SearchBar(){
    return(
        <>
            <div className={styles.searchBarContainer}>
                <input type="text" placeholder="Search"></input>
            </div>
            
        </>
    );
}