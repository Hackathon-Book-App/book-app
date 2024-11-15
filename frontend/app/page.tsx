'use client'
import SearchBooks from "./components/search_books"
import Header from "./components/header";
import GetImage from "./components/get_image";
import UserReadBooks from "./components/user_read_books";

export default function Home() {
    return(
        <>
        
            <Header/>
            
            <div className="flex items-center justify-center">
                <SearchBooks/>

                <GetImage/>

                <UserReadBooks/>
            </div>     
   
        </>

    )
}
