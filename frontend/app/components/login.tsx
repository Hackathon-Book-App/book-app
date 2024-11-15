import { FormEvent, useState } from "react"

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
            headers:{"content-type":"application/x-www-form-urlencoded",
            },
            body: urlencoded,
        }).then(response =>{
            if (!response.ok){
                throw new Error('Failed to login');
            }
            return response.json();
        })
        .then(data=>{
            const accessToken=data.access_token;
            localStorage.setItem('Access Token',accessToken)

            const tokenType=data.token_type;
            localStorage.setItem('Token Type',tokenType)
            
            setIsLogged({
                message:'Login Succesfully'
            })
     })
        .catch(error => setIsLogged({message:error.toString()}))
    }
    
    const [is_logged,setIsLogged]=useState({
            message:""
        })

    return (  
        <div className="w-52 flex justify-self-end text-black ">  
            <form onSubmit={checkAccount}>
                <input type="text" placeholder='username'
                    onChange={handleUsernameChange}/>
                <input type="password" placeholder='password'
                    onChange={handlePasswordChange}/>
                <button className='bg-yellow-400 px-4 py-2 rounded-full text-white' 
                    type="submit">Login</button>
                <p className="text-white">{is_logged.message}</p>
            </form>
        </div>  
    )
}

