import { FormEvent, useState } from "react"

export default function SignIn(){
    
    async function onUserDataSubmit(event:FormEvent<HTMLFormElement>){
        event.preventDefault()

        fetch('http://localhost:8000/signup',{
            method:'POST',
            headers:{'content-type':"application/json"},
            body: JSON.stringify(user_data),
        }).then(response =>response.json())
        .then(data =>{setSignUpRespone(data)})
        .catch(error => setSignUpRespone({message_from_db:error.toString()}))
    }

    const [user_data,setUserData]=useState({
        username:"",
        fullname:"",
        password:"",
        email:""
    }) 

    const  [sign_up_response,setSignUpRespone]=useState({
        message_from_db:""
        })


    function handleUsernameChange(e: { target: { value: any } }){
        setUserData({
            ...user_data,
            username:e.target.value
        })
    }
    function handleFullnameChangej(e: { target: { value: any } }){
        setUserData({
            ...user_data,
            fullname:e.target.value
        })
    } 
    function handlePasswordChange(e: { target: { value: any } }){
        setUserData({
            ...user_data,
            password:e.target.value
        })
    } 
    function handleEmailChange(e: { target: { value: any } }){
        setUserData({
            ...user_data,
            email:e.target.value
        })
    }





    return(
    <div className="border-blue-500 bg-blue-100 border-8 rounded-3xl flex items-center justify-center 
                        w-80 h-auto">
        <form onSubmit={onUserDataSubmit}>
            <h1>Sign In</h1>

            <p>Username:</p>
            <input type="text" placeholder="username"
                onChange={handleUsernameChange}/>
            
            <p>Fullname:</p>
            <input type="text" placeholder="Your Name"
                onChange={handleFullnameChangej}/>
            
            <p>Password:</p>
            <input type="password" placeholder="password"
                onChange={handlePasswordChange}/>
            
            <p>Email:</p>
            <input type="email" placeholder="email"
                onChange={handleEmailChange}/>
            <p> </p>
            <button className="bg-blue-500 hover:bg-blue-700 text-white 
                border-radius font-bold py-2 px-4 rounded-full" 
                type="submit">Sign Up</button>
            <p>Response: {sign_up_response.message_from_db}</p>
        </form>
    </div>
    )
}