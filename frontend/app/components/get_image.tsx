import { FormEvent, useState } from 'react';
import Image from 'next/image';
import carti from '@/app/CartiRaul.jpg'

export default function UploadImage() {

    const [image, setImage] = useState(null);
    const [message, setMessage] = useState("");

    async function onSubmit(event:FormEvent<HTMLFormElement>){
        event.preventDefault()

        if(!image){
            setMessage("Please select a file")
            return
        }

        const user_data=new FormData()
        user_data.append('image',image)

        fetch('http://localhost:8000/image',{
            method:'POST',
            body:user_data
        })
        .then(response =>{
            if (!response.ok){
                throw new Error('Failed send');
            }
            return response.json();
        })
        .then(data=>{console.debug(data)})
        .catch(error=>setMessage(error.toString()))
    }

    const handleFileChange = (event:any) => {
        setImage(event.target.files[0]);
        console.debug("image"+image)
    }

    return (  
        <div className="w-30 drop-shadow-2xl border-blue-500 
                        rounded-3xl border-8 bg-blue-100 h-auto w-80
                        flex items-center justify-center">
            <form onSubmit={onSubmit}>
                <h2>Upload an Image</h2>
                <input type="file" onChange={handleFileChange} accept="image/*"/>
                <button type="submit"
                    className="bg-yellow-400 hover:bg-blue-700 text-white 
                    border-radius font-bold py-2 px-6 rounded-full">
                    Get Recommandation
                </button>
                <p>Response:{message}</p>
            </form>
        </div>
  )
}   
