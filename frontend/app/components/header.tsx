import { useState } from "react";
import Login from "./login";
import SignUp from "./sign_up"



export default function Header(){

    const [page,setPage]=useState("")

    return (
        <>
            <div className="bg-blue-950 font-mono font-bold grid grid-cols-3 content-center gap-4  w-full
                           text-white h-28">
                <div>
                    <button className="bg-yellow-500 hover:bg-blue-700 text-white 
                                        border-radius font-bold py-2 px-4 rounded-full"
                                        onClick={()=>setPage("SignUp")} >Sign Up</button>   
                    <button className="bg-black hover:bg-gray-500 text-white
                                        border-radius font-bold py-2 px-4   rounded-full"
                                        onClick={()=>setPage("")} >x</button>     
                </div>
                <div>
                    <h1 className="text-4xl ">Welcome to Book-App</h1>
                </div>
                <Login/>
            </div>
            
            {page==="SignUp" && <SignUp/>}
                
        </>
    )
}