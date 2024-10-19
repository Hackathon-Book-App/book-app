import Login from "./login";

export default function Header(){
    return (
        <>
            <div className="bg-blue-500 font-mono font-bold grid grid-cols-3 content-center gap-4  w-full
                           text-white h-28">
                <div>
                    <button className="bg-yellow-500 hover:bg-blue-700 text-white 
                                        border-radius font-bold py-2 px-4 rounded-full">Sign In</button>
                    
                </div>
                <div>
                    <h1 className="text-4xl ">Welcome to book app</h1>
                </div>
                <Login/>
            </div>
        </>
    )
}