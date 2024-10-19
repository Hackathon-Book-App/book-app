import { useState } from "react"

export default function Login(){

    const [user_credentials,setUsercredentials]=useState({
        username: "",
        password: "",
    })

    function handleUsernameChange(e: { target: { value: any } }) {
        setUsercredentials({
            ...user_credentials,
            username:e.target.value
        })
    }

    function handlePasswordChange(e:{target:{value:any}}){
        setUsercredentials({
            ...user_credentials,
            password:e.target.value
        })
    }
    return (
        <>   
            <form className="text-black">
                <h1 className="text-white">Login </h1>
                <input type="text" placeholder='username'
                    onChange={handleUsernameChange}/>
                <input type="password" placeholder='password'
                    onChange={handlePasswordChange}/>
                <button className='bg-yellow-400 px-3 rounded-full text-white' 
                    type="submit">Login</button>
            </form>  
        </>
    )
}