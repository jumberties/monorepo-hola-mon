// App.jsx
import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [message, setMessage] = useState('Carregant...')
  
  // Detecta automàticament l'entorn
  const API_URL = import.meta.env.VITE_API_URL || 
    (import.meta.env.DEV 
      ? 'http://localhost:8000'  // URL local del backend
      : 'https://app-988a10f6-32df-4301-992f-53192fbeede8.cleverapps.io'  // URL producció
    )
  
  useEffect(() => {
    axios.get(`${API_URL}/api/message`)
      .then(res => setMessage(res.data.message))
      .catch(err => {
        console.error('Error:', err)
        setMessage('Error connectant amb el backend')
      })
  }, [])

  return (
    <div>
      <h1>React + FastAPI + PostgreSQL</h1>
      <p>{message}</p>
    </div>
  )
}

export default App
