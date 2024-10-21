import { FormEvent, useState } from "react"

const is_logged=false

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

    async function checkAccount(event:FormEvent<HTMLFormElement>){
        event.preventDefault()
        const urlencoded = new URLSearchParams();
        urlencoded.append("username", user_credentials.username);
        urlencoded.append("password", user_credentials.password);

        fetch('http://localhost:8000/login',{
            method:'POST',
            headers:{"content-type":"application/x-www-form-urlencoded"},
            body: urlencoded,
        }).then(response =>response.json())
        .then(data => setIsLogged(data))
        .catch(error => setIsLogged({message:error.toString()}))
    }

    const [is_logged,setIsLogged]=useState({
        message:""
    })

    return (  
        <div className="w-96 flex justify-self-end text-black ">  
            <form onSubmit={checkAccount}>
                <input type="text" placeholder='username'
                    onChange={handleUsernameChange}/>
                <input type="password" placeholder='password'
                    onChange={handlePasswordChange}/>
                <button className='bg-yellow-400 px-3 rounded-full text-white' 
                    type="submit">Login</button>
                <p>message: {is_logged.message}</p>
            </form>
        </div>  
    )
}