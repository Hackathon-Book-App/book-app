import { useEffect, useState } from "react";

export default function UserReadBooks() {
    const [readBooks, setReadBooks] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function GetReadBooks() {
            try {
                const tokenType = localStorage.getItem("Token Type") || "";
                const accessToken = localStorage.getItem("Access Token") || "";
                const response = await fetch("http://localhost:8000/getUserBooks", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": accessToken,
                    },
                    body: null,
                });

                if (!response.ok) {
                    throw new Error("Failed to fetch books");
                }

                const data = await response.json();
                setReadBooks(data);
            } catch (err:any) {
                setError(err.message);
            }
        }

        GetReadBooks();
    }, []); // The empty dependency array ensures the fetch happens only on component mount.

    return (
        <div
            className="w-30 drop-shadow-2xl border-blue-950 
                        rounded-3xl border-8 bg-blue-50 h-auto w-80
                        flex flex-col items-center justify-center p-4"
        >
            <p className="text-lg font-bold">Read Books</p>
            {error ? (
                <p className="text-red-500">Error: {error}</p>
            ) : readBooks.length > 0 ? (
                <ul className="list-disc list-inside">
                    {readBooks.map((book, index) => (
                        <li key={index} className="text-blue-900">
                            {book || "Unknown Title"} {/* Update based on your API response */}
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No books read yet.</p>
            )}
        </div>
    );
}
