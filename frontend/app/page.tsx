'use client'
import SignIn from "./components/sign_in"
import SearchBooks from "./components/search_books"
import Header from "./components/header";

var isLogged=true;

export default function Home() {
    return(
        <>
            <Header/>

            <div className="flex justify-center">
                {isLogged?<SearchBooks/>:<SignIn/>}
            </div>
        </>
    )
}
