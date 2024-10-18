import book_properties from '@/app/page'
export default function Login(){
    return (
        <>
            
            <form>
                <h1>Login </h1>
                <input type="text" placeholder='username'/>
                <input type="password" placeholder='password'/>
                <button className='bg-blue-800' 
                    type="submit">Login</button>
            </form>
            
        </>
    )
}