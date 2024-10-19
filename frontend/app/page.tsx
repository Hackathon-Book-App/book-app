'use client'
import Login from "./components/login"
import SignIn from "./components/sign_in"
import SearchBooks from "./components/search_books"

var isLogged=true;

export default function Home() {
    return(
        <>
            {/* header*/}
            <div className="bg-blue-500 font-mono font-bold grid grid-cols-3 content-center gap-4  w-full
                           text-white h-28">
                <div>
                    <button className="bg-yellow-500 hover:bg-blue-700 text-white 
                                        border-radius font-bold py-2 px-4 rounded-full">Sign In</button>
                </div>
                <div>
                    <h1 className="text-4xl ">Welcome to book app</h1>
                </div>
                <div className="w-48 flex justify-self-end">
                    <Login/>
                </div>
            </div>

            {/* */}
            <div className="flex justify-center">
                <div className="w-30 drop-shadow-2xl border-blue-500 
                                rounded-3xl border-8 bg-blue-100 h-auto w-96 
                                flex justify-center ">
                    <SearchBooks/>
                </div>
                <div className=" border-blue-500 bg-blue-100 border-8 rounded-3xl flex items-center justify-center w-96 ">
                    <SignIn/>
                </div>
            </div>
        </>
    )
}
