'use client'
import SearchBooks from "./components/search_books"
import Header from "./components/header";
import GetImage from "./components/get_image";

export default function Home() {
    return(
        <>
            <Header/>
            
            <SearchBooks/>

            <GetImage/>
        </>
    )
}
