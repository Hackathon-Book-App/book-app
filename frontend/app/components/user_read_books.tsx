import { useState } from "react"

export default function UserReadBooks(){
    //const [readBooks,setreadBooks]=useState("")
    //var [isLogged,setisLogged]=useState(true)
    
    const [readBooks,setReadBooks]=useState("")
    async function GetReadBooks(){
        const tokenType = localStorage.getItem('Token Type');
        const accessToken = localStorage.getItem('Access Token');
        fetch('http://localhost:8000/getUserBooks',{
                method:'POST',
                headers:{"content-type":"application/json",
                        "Authorization":tokenType??""+accessToken??""
                },
                body: null
        })       
        .then(response=>response.json())
        .then(data=>setReadBooks(data))
        .catch(error=>setReadBooks("eroroaer")
        )}

    //if(isLogged==true)
        return(
            <>
                <div className="w-30 drop-shadow-2xl border-blue-950 
                                rounded-3xl border-8 bg-blue-50 h-auto w-80
                                flex items-center justify-center">
                    <p>Read Books</p>

                    <p onLoadStart={GetReadBooks} onLoad={GetReadBooks}>{readBooks}</p>

                </div>
            </>
        )
    }