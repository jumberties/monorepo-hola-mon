// App.jsx
import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [message, setMessage] = useState('Carregant...')
  
  // Usa la variable d'entorn o localhost per defecte
  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
  
  useEffect(() => {
    axios.get(`${API_URL}/api/message`)
      .then(res => setMessage(res.data.message))
      .catch(err => {
        console.error('Error:', err)
        setMessage('Error connectant amb el backend')
      })
  }, [])
  
  return (
    <div style={{ textAlign: 'center', marginTop: '4rem' }}>
      <h1>Reactaaaaaaaaaaaaaa + FastAPI + PostgreSQL</h1>
      <p>{message}</p>
    </div>
  )
}

export default App
