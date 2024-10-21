import { FormEvent, useState } from "react"

export default function SearchBooks(){
    
    async function onSubmit(event:FormEvent<HTMLFormElement>){
        event.preventDefault() 
  
        fetch('http://localhost:8000/',{
          method:'POST',
          headers:{"content-type":"application/json"},
          body: JSON.stringify(book_properties),
        }).then(response => response.json())
        .then(data =>{ setRecomandation(data)})
        .catch(error => setRecomandation({message:error.toString()}))
    }

    const[recomandation,setRecomandation]=useState({
        message:""
        })
        
    const [book_properties,setBookProperties]=useState({
        topic:"",    
        style:"",
        language:"",
        min_pages:"",
        max_pages:""
      })

    function handleTopicChange(e: { target: { value: any } }){
        setBookProperties({
            ... book_properties,
            topic:e.target.value
    })
    }
    function handleStyleChange(e: { target: { value: any } }){
        setBookProperties({
            ... book_properties,
            style:e.target.value
    })
    }
    function handleLanguageChange(e: { target: { value: any } }){
        setBookProperties({
            ... book_properties,
            language:e.target.value
    })
    }
    function handleMinPagechange(e: { target: { value: any } }){
        setBookProperties({
            ... book_properties,
            min_pages:e.target.value
    })
    }
    function handleOnMaxChange(e: { target: { value: any } }){
        setBookProperties({
            ... book_properties,
            max_pages:e.target.value
    })
    }

    return(
        <div className="w-30 drop-shadow-2xl border-blue-500 
                        rounded-3xl border-8 bg-blue-100 h-auto w-80
                        flex items-center justify-center
                         ">
            <form  onSubmit={onSubmit} >
                <p >Enter the topic of the Book </p>
                <input 
                    type="text"  placeholder="topic here"
                    onChange={handleTopicChange} />
                <p>Enter the style of the book</p>
                <input type="text" placeholder="style here"
                    onChange={handleStyleChange}/>
                
                <p>Enter the language here</p>
                <input type="text" placeholder="language here"
                    onChange={handleLanguageChange}/>
                
                <p>Enter the minimum number of pages</p>
                <input type="text" defaultValue="0"
                    onChange={handleMinPagechange}/>

                <p>Enter the maximum number of pages</p>
                <input type="text" defaultValue="1000"
                    onChange={handleOnMaxChange}/>
                <p> </p>
                <button className="bg-blue-500 hover:bg-blue-700 text-white 
                    border-radius font-bold py-2 px-4 rounded-full"
                    type='submit'>Submit</button>  
                <p>Response: {recomandation.message}</p>
            </form>
        </div>
    )
}
