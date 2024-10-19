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
            <div className="w-96 flex justify-self-end text-black ">  
                <form>
                    <input type="text" placeholder='username'
                        onChange={handleUsernameChange}/>
                    <input type="password" placeholder='password'
                        onChange={handlePasswordChange}/>
                    <button className='bg-yellow-400 px-3 rounded-full text-white' 
                        type="submit">Login</button>
                </form>
            </div>  
        </>
    )
}